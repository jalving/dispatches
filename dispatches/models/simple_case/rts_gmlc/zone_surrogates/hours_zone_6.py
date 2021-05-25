import numpy as np
def f(*X):
    pmax= X[0]
    pmin= X[1]
    ramp_rate= X[2]
    min_up_time= X[3]
    min_down_time= X[4]
    marg_cst= X[5]
    no_load_cst= X[6]
    st_time_hot= X[7]
    st_time_warm= X[8]
    st_time_cold= X[9]
    st_cst_hot= X[10]
    st_cst_warm= X[11]
    st_cst_cold= X[12]
    return  0.67944399816844991413234 * pmax - 0.78760589976555228641786 * pmin - 0.32096005050988468676465 * ramp_rate - 0.21386805196844629883834 * min_up_time - 0.25785692779282182174327 * min_down_time - 0.94469730171564925136352 * marg_cst - 0.34290441149544570453855 * no_load_cst + 38.390099377180405326726 * st_time_hot - 12.146775859122501017850 * st_time_warm + 1.2121971642388826850834 * st_time_cold - 0.28383699133346917964360 * st_cst_hot + 0.26773687806668672317656 * st_cst_warm - 0.62994867607125460979428E-003 * pmax**2 + 0.22745083373935347237360E-002 * pmin**2 + 0.14531385706794666592273E-002 * ramp_rate**2 - 0.88846144536607780939352E-002 * min_up_time**2 + 0.91281204293976892644169E-002 * min_down_time**2 + 0.27107223147126296991516E-001 * marg_cst**2 + 1.5059500576276469985260 * no_load_cst**2 + 0.11015272983439291354092E-005 * pmax**3 - 0.22670518492342160432336E-005 * pmin**3 - 0.60878482747400060608352E-006 * ramp_rate**3 - 0.92511825252777690276398E-004 * marg_cst**3 + 0.47951647913210251796684E-003 * pmax*pmin - 0.12603084105924464587006E-002 * pmax*ramp_rate - 0.95116818660710537609165E-003 * pmax*min_up_time - 0.48649734707381474393614E-003 * pmax*marg_cst - 0.17440518087866122703966E-001 * pmax*no_load_cst + 0.45617660913151732160475E-001 * pmax*st_time_hot - 0.14643977331828853319373E-001 * pmax*st_time_warm + 0.77004851255674168931248E-003 * pmin*ramp_rate + 0.16275726201185670462268E-002 * pmin*min_up_time - 0.63746999956065700070063E-003 * pmin*min_down_time - 0.46794215512323206543344E-002 * pmin*marg_cst + 0.27307341053408231562605E-001 * pmin*no_load_cst - 0.19927125226860017970232 * pmin*st_time_hot + 0.51010378151506309551966E-001 * pmin*st_time_warm + 0.48814931686801495873754E-003 * pmin*st_time_cold + 0.31129491198425597586752E-002 * ramp_rate*min_up_time + 0.57751206982276561546774E-002 * ramp_rate*marg_cst - 0.14469527519001834647838 * ramp_rate*st_time_hot + 0.95234716702163307172624E-002 * ramp_rate*st_time_warm + 0.69085242195841898953101E-003 * ramp_rate*st_cst_warm - 0.16328637997136382156715E-002 * min_up_time*marg_cst + 0.10078642805704308982317 * min_up_time*no_load_cst + 0.52180068632403642236994 * min_up_time*st_time_hot - 0.18536096741696492240514 * min_up_time*st_time_warm + 0.62025911042147004181846E-001 * min_up_time*st_time_cold - 0.59077879547885731384427E-002 * min_up_time*st_cst_hot + 0.19594981547376336128430E-001 * min_down_time*marg_cst + 0.15285786024783867831367 * min_down_time*no_load_cst + 1.7387001761812126421347 * min_down_time*st_time_hot - 0.38529712450139010082584E-001 * min_down_time*st_time_warm - 0.74752076522069076103261E-002 * min_down_time*st_cst_warm - 0.40395107348897896226703E-001 * marg_cst*no_load_cst - 2.0423576971969623627956 * marg_cst*st_time_hot - 0.39401717076307907206001 * marg_cst*st_time_warm - 0.73967441031767375281269E-001 * marg_cst*st_time_cold + 0.17448283333337248623973E-001 * marg_cst*st_cst_warm - 17.995116116054859389806 * no_load_cst*st_time_hot + 4.5235675616380008889905 * no_load_cst*st_time_warm - 0.66532603894727826432387 * no_load_cst*st_time_cold + 0.85152302687060657526708E-001 * no_load_cst*st_cst_hot - 0.74863709071477859038061E-008 * (pmax*pmin)**2 - 0.14257493264687146764748E-007 * (pmax*marg_cst)**2 + 0.19861332390098076964397E-005 * (pmax*no_load_cst)**2 + 0.39634897278275025240643E-008 * (pmin*ramp_rate)**2 - 0.66563471828202732300694E-006 * (pmin*marg_cst)**2 - 0.30789339375999301017146E-004 * (pmin*no_load_cst)**2 + 0.59715494427243836703112E-003 * (pmin*st_time_hot)**2 - 0.38288154926407684368068E-004 * (pmin*st_time_warm)**2 - 0.15275998255478025653303E-006 * (ramp_rate*min_up_time)**2 - 0.43449039344091544798221E-006 * (ramp_rate*marg_cst)**2 + 0.15126861784808050704482E-003 * (ramp_rate*st_time_hot)**2 - 0.78044882331137196485645E-005 * (ramp_rate*st_time_warm)**2 + 0.60039251452540368157815E-004 * (min_up_time*marg_cst)**2 + 0.76588030001295053991739E-002 * (min_up_time*st_time_hot)**2 + 0.90200350231849589759808E-003 * (min_up_time*st_time_warm)**2 - 0.24006203422761898235577E-004 * (min_down_time*marg_cst)**2 - 0.13524174315430849760422E-002 * (min_down_time*no_load_cst)**2 - 0.38544132852181993420526E-001 * (min_down_time*st_time_hot)**2 + 0.19826266053906247029126E-002 * (min_down_time*st_time_warm)**2 - 0.97110045166869888438876E-002 * (marg_cst*no_load_cst)**2 + 0.57636653091284545391559E-001 * (marg_cst*st_time_hot)**2 + 0.32961740926985881941502E-003 * (marg_cst*st_time_cold)**2 + 3.6172646098629499533672 * (no_load_cst*st_time_hot)**2 - 0.50823153293469258695580 * (no_load_cst*st_time_warm)**2 