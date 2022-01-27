import numpy as np
def f(*X):
    pmax= X[0]
    pmin_multi= X[1]
    ramp_multi= X[2]
    min_up_time= X[3]
    min_down_multi= X[4]
    marg_cst= X[5]
    no_load_cst= X[6]
    startup_cst= X[7]
    return  0.34287414811367711298118 * pmax - 0.30118155887217884503215 * pmin_multi - 1169.5604330873009075731 * ramp_multi + 0.86300433734636514127025E-001 * min_up_time + 0.95750744036338358150529E-002 * min_down_multi - 0.34779283879178951588429 * marg_cst - 0.20333230879525951428910 * no_load_cst - 0.16343790040781558392524 * startup_cst - 0.66439172812552738101033E-001 * pmax**2 - 0.35730964893043754004864E-001 * pmin_multi**2 + 1.3136673333920880768488 * ramp_multi**2 - 0.17428357753538632757273E-001 * min_up_time**2 - 0.20141869237308191072089E-002 * min_down_multi**2 - 0.52727431084507059289024 * marg_cst**2 - 0.58865516565448819386042E-001 * no_load_cst**2 - 0.17710989276949912207826 * startup_cst**2 + 0.39798800134954494256423E-001 * pmax**3 - 0.48851534232322475770349E-001 * pmin_multi**3 + 779.57938014991157160694 * ramp_multi**3 - 0.21081887556498001001781E-001 * min_up_time**3 - 0.13785318554398701129671 * marg_cst**3 + 0.79831992526046571811982E-001 * startup_cst**3 - 0.50161128264844818958057E-001 * pmax*pmin_multi + 0.62512040888767893970224E-002 * pmax*min_up_time - 0.10156595481759890520213 * pmax*marg_cst - 0.49543665405607742457939E-001 * pmax*no_load_cst - 0.48300600805554087802118E-001 * pmax*startup_cst + 0.14915157962233267091579E-001 * pmin_multi*ramp_multi - 0.56286302289948894617133E-001 * pmin_multi*marg_cst + 0.45596134890495285119094E-001 * pmin_multi*no_load_cst + 0.26527286611914318442684E-001 * pmin_multi*startup_cst + 0.17519457359562964904320E-001 * ramp_multi*marg_cst + 0.13622889734707420775206E-001 * ramp_multi*startup_cst + 0.43957964652960174190000E-001 * min_up_time*marg_cst + 0.15995888512760784994082E-001 * min_up_time*no_load_cst - 0.30870540405653561222277E-001 * min_up_time*startup_cst - 0.46939616075900331138016 * marg_cst*no_load_cst - 0.14894045862032781468720 * marg_cst*startup_cst + 0.26692442358925008022430E-001 * no_load_cst*startup_cst + 0.18249591976943660420751E-001 * (pmax*pmin_multi)**2 + 0.47198612840429456094515E-001 * (pmin_multi*marg_cst)**2 + 0.84791820357838967175956E-002 * (pmin_multi*startup_cst)**2 + 0.88976117715212684616821E-002 * (ramp_multi*min_up_time)**2 + 0.15976283451018938319699E-001 * (ramp_multi*marg_cst)**2 + 0.15480861034384672467179E-001 * (ramp_multi*no_load_cst)**2 - 0.35620592753070723368580E-001 * (ramp_multi*startup_cst)**2 - 0.10726582524892107339820E-001 * (min_up_time*marg_cst)**2 + 0.24958655397748989723805E-001 * (min_up_time*startup_cst)**2 + 0.70166644308415293540548E-001 * (marg_cst*no_load_cst)**2 + 0.12453592051693049280736 * (marg_cst*startup_cst)**2 - 0.16289314782438533285580E-001 * (pmax*pmin_multi)**3 - 0.18379951799345435603517E-001 * (pmax*marg_cst)**3 + 0.84894875253025640221560E-002 * (pmax*startup_cst)**3 + 0.18610033603189052309190E-001 * (pmin_multi*marg_cst)**3 + 0.12229027466454557224185E-001 * (pmin_multi*no_load_cst)**3 - 0.50202607266767694527143E-002 * (pmin_multi*startup_cst)**3 + 0.10528945273568023760502E-001 * (ramp_multi*marg_cst)**3 - 0.10621839609922302874456E-001 * (ramp_multi*startup_cst)**3 - 0.67413954112285640746238E-002 * (min_up_time*marg_cst)**3 - 0.36497628638421301776329E-002 * (min_up_time*startup_cst)**3 + 0.12452915871543929204890 * (marg_cst*no_load_cst)**3 + 0.55752875357402151626496E-002 * (marg_cst*startup_cst)**3 