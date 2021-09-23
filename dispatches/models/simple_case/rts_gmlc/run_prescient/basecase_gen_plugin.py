import pyomo.environ as pyo
import math

startup_cost_data = { 'yellow' : [ (0.75, 94.00023429), (2.5, 135.2230393), (3, 147.0001888) ],
                      'blue'   : [ (0.375, 93.99890632), (1.375, 101.4374234), (7.5, 146.9986814) ],
                      'brown'  : [ (0.166666667, 58.99964891), (0.25, 61.09068702), (2, 104.9994673) ], 
                      'dark_blue': [ (0.111111111, 35.00249986), (0.222222222, 49.66991167), (0.444444444, 79.00473527) ],
                     }
startup_cost_profiles = [ startup_cost_data['yellow'], 
                          startup_cost_data['blue'], 
                          startup_cost_data['brown'],
                          startup_cost_data['dark_blue'],
                          [ (1.0, 0.) ]]

#Base Case settings
# p_min_multis = [ 0., 0.15, 0.30, 0.45 ]
# ramp_multis = [ 0.5, 0.75, 1. ]
# min_ups = [ 1, 2, 4, 8, 16 ]
# min_dn_multis = [ 0.5, 1., 2. ]
# marginal_costs = [ 5., 10., 15., 20., 25., 30. ] #$/MWh
# no_load_costs = [ 0., 1., 2.5 ]

pmax = 355
pmin = 0.3*pmax 
ramp_rate = 0.5*(pmax-pmin)
min_up_time = 4 
min_down_time = int(math.ceil(1.0*min_up_time))
marginal_cost = 25.0
fixed_run_cost = 1.0
startup_cost_profile = startup_cost_profiles[1]

## THE CONSTANTS FOR THIS RUN
gen = '123_STEAM_3'

def change_gen_123_STEAM_3(data, market):
    hr_ramp_rate = ramp_rate
    startup_shutdown_rate = min(pmin+0.5*hr_ramp_rate, pmax)

    min_up = min_up_time
    min_dn = min_down_time

    #Get data dictionary
    data_none = data[None]
    ## change the p_max
    data_none['MaximumPowerOutput'][gen] = pmax 

    ## change the p_min
    data_none['MinimumPowerOutput'][gen] = pmin

    ## fix the initial state, if needed (for the initial inital conditions)
    power_gen_t0 = pyo.value(data_none['PowerGeneratedT0'][gen])
    unit_on_t0 = pyo.value(data_none['UnitOnT0'][gen])

    if unit_on_t0:
        if power_gen_t0 > pmax:
            data_none['PowerGeneratedT0'][gen] = pmax
        if power_gen_t0 < pmin:
            data_none['PowerGeneratedT0'][gen] = pmin

    ## change the ramp rate
    data_none['NominalRampUpLimit'][gen] = hr_ramp_rate
    data_none['NominalRampDownLimit'][gen] = hr_ramp_rate

    ## change the startup/shutdown ramp rate
    data_none['StartupRampLimit'][gen] = startup_shutdown_rate
    data_none['ShutdownRampLimit'][gen] = startup_shutdown_rate
    
    ## change the cost
    data_none['CostPiecewisePoints'][gen] = [pmin, pmax]
    data_none['CostPiecewiseValues'][gen] = [pmax*fixed_run_cost + pmin*marginal_cost, 
                                            pmax*fixed_run_cost + pmax*marginal_cost]

    ## change the uptime/downtime
    data_none['MinimumUpTime'][gen] = min_up
    data_none['MinimumDownTime'][gen] = min_dn

    raw_startup_costs = [ [min_dn*time_over_min_dn, pmax*cost_over_capacity] \
                        for time_over_min_dn, cost_over_capacity in startup_cost_profile ]

    for idx, (startup_time, _) in enumerate(raw_startup_costs):
        if startup_time > min_dn:
            ## go back to the index before this was the case
            idx -= 1
            break
    startup_costs = raw_startup_costs[idx:]

    startup_costs[0][0] = min_dn

    startup_costs_rounded = [ (int(math.ceil(lag)), cost) for lag, cost in startup_costs ]

    startup_costs = []
    ## eliminate duplicates from math.ceil
    for idx, (lag, cost) in enumerate(startup_costs_rounded[:-1]):
        next_lag = startup_costs_rounded[idx+1][0]
        if lag == next_lag:
            continue
        else:
            startup_costs.append((lag,cost))
    ## put on the last cost
    startup_costs.append(startup_costs_rounded[-1])

    data_none['StartupLags'][gen] = [ lag for lag, _ in startup_costs ]
    data_none['StartupCosts'][gen] = [ cost for _, cost in startup_costs ]
    print("MODIFIED 123 STEAM 3")

data_dict_callback = change_gen_123_STEAM_3

print("PARSED PLUGIN")