from ocelot import * 

# drifts 
dtl_2 = Drift(l=2.000002, eid='D_2')
dtl_3 = Drift(l=0.5, eid='D_3')
dtl_5 = Drift(l=8.050009, eid='D_5')
dtl_6 = Drift(l=0.1483, eid='D_6')
dtl_7 = Drift(l=0.1543, eid='D_7')
dtl_8 = Drift(l=0.38135, eid='D_8')
dtl_9 = Drift(l=4.23795, eid='D_9')
dtl_10 = Drift(l=0.2, eid='D_10')
dtl_11 = Drift(l=3.546001, eid='D_11')
dtl_12 = Drift(l=0.500002, eid='D_12')
dtl_14 = Drift(l=0.31235, eid='D_14')
dtl_15 = Drift(l=0.20895, eid='D_15')
dtl_16 = Drift(l=0.15395, eid='D_16')
dtl_17 = Drift(l=6.0218, eid='D_17')
dtl_18 = Drift(l=0.260793, eid='D_18')
dtl_21 = Drift(l=3.88, eid='D_21')
dtl_23 = Drift(l=0.1418, eid='D_23')
dtl_24 = Drift(l=1.962924, eid='D_24')
dtl_25 = Drift(l=9.801347, eid='D_25')
dtl_28 = Drift(l=2.1218, eid='D_28')
dtl_29 = Drift(l=1.500337, eid='D_29')
dtl_30 = Drift(l=5.525001, eid='D_30')
dtl_33 = Drift(l=11.57414, eid='D_33')
dtl_36 = Drift(l=6.313742, eid='D_36')
dtl_37 = Drift(l=1.225001, eid='D_37')
dtl_40 = Drift(l=6.493894, eid='D_40')
dtl_43 = Drift(l=9.764269, eid='D_43')
dtl_44 = Drift(l=0.500173, eid='D_44')
dtl_46 = Drift(l=0.622486, eid='D_46')
dtl_47 = Drift(l=0.2509, eid='D_47')
dtl_48 = Drift(l=0.1935, eid='D_48')
dtl_49 = Drift(l=0.835, eid='D_49')
dtl_50 = Drift(l=0.15, eid='D_50')
dtl_51 = Drift(l=3.1577, eid='D_51')
dtl_54 = Drift(l=0.622487, eid='D_54')
dtl_55 = Drift(l=0.500172, eid='D_55')
dtl_57 = Drift(l=0.611786, eid='D_57')
dtl_58 = Drift(l=0.1607, eid='D_58')
dtl_59 = Drift(l=0.3448, eid='D_59')
dtl_62 = Drift(l=0.2144, eid='D_62')
dtl_63 = Drift(l=0.558, eid='D_63')
dtl_65 = Drift(l=0.822, eid='D_65')
dtl_67 = Drift(l=0.45, eid='D_67')
dtl_68 = Drift(l=0.313, eid='D_68')
dtl_69 = Drift(l=3.87, eid='D_69')
dtl_70 = Drift(l=0.3223, eid='D_70')
dtl_71 = Drift(l=0.8578, eid='D_71')
dtl_72 = Drift(l=1.08149, eid='D_72')
dtl_73 = Drift(l=2.00615, eid='D_73')

# quadrupoles 
qf_1996_tld = Quadrupole(l=0.5321, k1=-0.17071419800037585, tilt=0.0, eid='QF.1996.TLD')
qf_2009_tld = Quadrupole(l=0.5321, k1=0.3253644447998496, tilt=0.0, eid='QF.2009.TLD')
qf_2016_tld = Quadrupole(l=0.5321, k1=-0.33304205750046983, tilt=0.0, eid='QF.2016.TLD')
qf_2024_tld = Quadrupole(l=0.5321, k1=0.3373289400996053, tilt=0.0, eid='QF.2024.TLD')
qf_2034_tld = Quadrupole(l=0.5321, k1=-0.30482150999999996, tilt=0.0, eid='QF.2034.TLD')
qf_2046_tld = Quadrupole(l=0.5321, k1=0.17452716339973687, tilt=0.0, eid='QF.2046.TLD')
qf_2058_tld = Quadrupole(l=0.5321, k1=-0.09725015276075925, tilt=0.0, eid='QF.2058.TLD')
qf_2068_tld = Quadrupole(l=0.5321, k1=0.00800000000 , tilt=0.0, eid='QF.2068.TLD')
qf_2075_tld = Quadrupole(l=0.5321, k1=0.000000000, tilt=0.0, eid='QF.2075.TLD')
qk_2095_tld = Quadrupole(l=1.0552, k1=-0.1812652541, tilt=0.0, eid='QK.2095.TLD')
qk_2103_tld = Quadrupole(l=1.0552, k1=-0.1812652541, tilt=0.0, eid='QK.2103.TLD')
qk_2113_tld = Quadrupole(l=1.0552, k1=0.02, tilt=0.0, eid='QK.2113.TLD')
qk_2115_tld = Quadrupole(l=1.0552, k1=0.02, tilt=0.0, eid='QK.2115.TLD')
qk_2116_tld = Quadrupole(l=1.0552, k1=0.0, tilt=0.0, eid='QK.2116.TLD')
qk_2117_tld = Quadrupole(l=1.0552, k1=0.0, tilt=0.0, eid='QK.2117.TLD')



# bending magnets 
bz_1980_tld = SBend(l = 1.0, angle=-0.00550002773, e1=0.0, e2=-0.005500028, gap=0, tilt=1.351193237, fint=0.0, fintx=0.0, eid='BZ.1980.TLD')
bz_1983_tld = SBend(l = 1.0, angle=-0.005499885903, e1=-0.002749943, e2=-0.002749943, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BZ.1983.TLD')
bz_1985_tld = SBend(l = 1.0, angle=-0.005499885903, e1=-0.002749943, e2=-0.002749943, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BZ.1985.TLD')
bz_1986_tld = SBend(l = 1.0, angle=-0.005499885903, e1=-0.002749943, e2=-0.002749943, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BZ.1986.TLD')
bd_2005_tld = SBend(l = 1.0, angle=0.007145035231, e1=0.003572518, e2=0.003572518, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BD.2005.TLD')
bd_2006_tld = SBend(l = 1.0, angle=0.007145035231, e1=0.003572518, e2=0.003572518, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BD.2006.TLD')
bd_2008_tld = SBend(l = 1.0, angle=-0.006696413191, e1=-0.003348207, e2=-0.003348207, gap=0, tilt=0.0, fint=0.0, fintx=0.0, eid='BD.2008.TLD')
bd_2039_tld = SBend(l = 1.0, angle=-0.006696413191, e1=-0.003348207, e2=-0.003348207, gap=0, tilt=0.0, fint=0.0, fintx=0.0, eid='BD.2039.TLD')
bd_2066_tld = SBend(l = 1.0, angle=0.008354779726, e1=0.00417739, e2=0.00417739, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BD.2066.TLD')
bv_2087_tld = SBend(l = 2.5, angle=0.04072434921, e1=0.020362175, e2=0.020362175, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BV.2087.TLD')
bv_2090_tld = SBend(l = 2.5, angle=0.04072434921, e1=0.020362175, e2=0.020362175, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BV.2090.TLD')
bv_2093_tld = SBend(l = 2.5, angle=0.04072434921, e1=0.020362175, e2=0.020362175, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BV.2093.TLD')
bv_2105_tld = SBend(l = 2.5, angle=0.04072434921, e1=0.020362175, e2=0.020362175, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BV.2105.TLD')
bv_2108_tld = SBend(l = 2.5, angle=0.04072434921, e1=0.020362175, e2=0.020362175, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BV.2108.TLD')
bv_2111_tld = SBend(l = 2.5, angle=0.04072434921, e1=0.020362175, e2=0.020362175, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BV.2111.TLD')
sweep_2119_tld = RBend(l = 0.64, angle=0.0, e1=0.0, e2=0.0, gap=0, tilt=-1.570796327, fint=0.0, fintx=0.0, eid='SWEEP.2119.TLD')
sweep_2120_tld = RBend(l = 0.64, angle=0.0, e1=0.0, e2=0.0, gap=0, tilt=0, fint=0.0, fintx=0.0, eid='SWEEP.2120.TLD')

# correctors 
cfy_2000_tld = Vcor(l=0.1, angle=0.0, eid='CFY.2000.TLD')
cfx_2000_tld = Hcor(l=0.1, angle=0.0, eid='CFX.2000.TLD')
cfx_2009_tld = Hcor(l=0.1, angle=0.0, eid='CFX.2009.TLD')
cfy_2017_tld = Vcor(l=0.1, angle=0.0, eid='CFY.2017.TLD')
cfx_2021_tld = Hcor(l=0.1, angle=0.0, eid='CFX.2021.TLD')
cfy_2035_tld = Vcor(l=0.1, angle=0.0, eid='CFY.2035.TLD')
cfx_2046_tld = Hcor(l=0.1, angle=0.0, eid='CFX.2046.TLD')
cfy_2059_tld = Vcor(l=0.1, angle=0.0, eid='CFY.2059.TLD')
cfx_2068_tld = Hcor(l=0.1, angle=0.0, eid='CFX.2068.TLD')
cfy_2076_tld = Vcor(l=0.1, angle=0.0, eid='CFY.2076.TLD')
cnx_2098_tld = Hcor(l=0.3, angle=0.0, eid='CNX.2098.TLD')
cny_2098_tld = Vcor(l=0.3, angle=0.0, eid='CNY.2098.TLD')

# markers 
stsec_1980_tld = Marker(eid='STSEC.1980.TLD')
otrc_1995_tld = Marker(eid='OTRC.1995.TLD')
tora_1995_tld = Marker(eid='TORA.1995.TLD')
otrd_2121_tld = Marker(eid='OTRD.2121.TLD')
torc_2122_tld = Marker(eid='TORC.2122.TLD')
bhm_2122_tld = Marker(eid='BHM.2122.TLD')
scrw_2126_tld = Marker(eid='SCRW.2126.TLD')
duwindow_2126_tld = Marker(eid='DUWINDOW.2126.TLD')
duflange_2127_tld = Marker(eid='DUFLANGE.2127.TLD')
duconcrete_2128_tld = Marker(eid='DUCONCRETE.2128.TLD')
dustart_2130_tld = Marker(eid='DUSTART.2130.TLD')
duabsorb_2130_tld = Marker(eid='DUABSORB.2130.TLD')
ensec_2130_tld = Marker(eid='ENSEC.2130.TLD')

# monitor 
bpma_1995_tld = Monitor(eid='BPMA.1995.TLD')
bpma_2008_tld = Monitor(eid='BPMA.2008.TLD')
bpma_2016_tld = Monitor(eid='BPMA.2016.TLD')
bpma_2021_tld = Monitor(eid='BPMA.2021.TLD')
bpma_2034_tld = Monitor(eid='BPMA.2034.TLD')
bpma_2045_tld = Monitor(eid='BPMA.2045.TLD')
bpma_2058_tld = Monitor(eid='BPMA.2058.TLD')
bpma_2067_tld = Monitor(eid='BPMA.2067.TLD')
bpma_2075_tld = Monitor(eid='BPMA.2075.TLD')
bpmd_2097_tld = Monitor(eid='BPMD.2097.TLD')
bpmd_2101_tld = Monitor(eid='BPMD.2101.TLD')
bpmd_2113_tld = Monitor(eid='BPMD.2113.TLD')
bpmd_2118_tld = Monitor(eid='BPMD.2118.TLD')
bpmd_2121_tld = Monitor(eid='BPMD.2121.TLD')
bpmw_2126_tld = Monitor(eid='BPMW.2126.TLD')

# sextupoles 
sa_2016_tld = Sextupole(l=0.3164, k2=1.019615123428, tilt=0.401425728, eid='SA.2016.TLD')
sa_2021_tld = Sextupole(l=0.3164, k2=-1.938885234104, tilt=0.322885912, eid='SA.2021.TLD')
sa_2037_tld = Sextupole(l=0.3164, k2=-2.371252862297, tilt=0.628318531, eid='SA.2037.TLD')
sk_2096_tld = Sextupole(l=0.343, k2=0.540738342718, tilt=1.570796327, eid='SK.2096.TLD')
sk_2102_tld = Sextupole(l=0.343, k2=0.540738342718, tilt=1.570796327, eid='SK.2102.TLD')


# lattice 
cell = (stsec_1980_tld, bz_1980_tld, dtl_2, bz_1983_tld, dtl_3, bz_1985_tld,
dtl_3, bz_1986_tld, dtl_5, otrc_1995_tld, dtl_6, tora_1995_tld, dtl_7, bpma_1995_tld,
dtl_8, qf_1996_tld, dtl_9, cfy_2000_tld, dtl_10, cfx_2000_tld, dtl_11, bd_2005_tld,
dtl_12, bd_2006_tld, dtl_12, bd_2008_tld, dtl_14, bpma_2008_tld, dtl_15, qf_2009_tld,
dtl_16, cfx_2009_tld, dtl_17, sa_2016_tld, dtl_18, bpma_2016_tld, dtl_15, qf_2016_tld,
dtl_16, cfy_2017_tld, dtl_21, bpma_2021_tld, dtl_10, cfx_2021_tld, dtl_23, sa_2021_tld,
dtl_24, qf_2024_tld, dtl_25, bpma_2034_tld, dtl_15, qf_2034_tld, dtl_16, cfy_2035_tld,
dtl_28, sa_2037_tld, dtl_29, bd_2039_tld, dtl_30, bpma_2045_tld, dtl_15, qf_2046_tld,
dtl_16, cfx_2046_tld, dtl_33, bpma_2058_tld, dtl_15, qf_2058_tld, dtl_16, cfy_2059_tld,
dtl_36, bd_2066_tld, dtl_37, bpma_2067_tld, dtl_15, qf_2068_tld, dtl_16, cfx_2068_tld,
dtl_40, bpma_2075_tld, dtl_15, qf_2075_tld, dtl_16, cfy_2076_tld, dtl_43, bv_2087_tld,
dtl_44, bv_2090_tld, dtl_44, bv_2093_tld, dtl_46, qk_2095_tld, dtl_47, sk_2096_tld,
dtl_48, bpmd_2097_tld, dtl_49, cnx_2098_tld, dtl_50, cny_2098_tld, dtl_51, bpmd_2101_tld,
dtl_48, sk_2102_tld, dtl_47, qk_2103_tld, dtl_54, bv_2105_tld, dtl_55, bv_2108_tld,
dtl_44, bv_2111_tld, dtl_57, bpmd_2113_tld, dtl_58, qk_2113_tld, dtl_59, qk_2115_tld,
dtl_59, qk_2116_tld, dtl_59, qk_2117_tld, dtl_62, bpmd_2118_tld, dtl_63, sweep_2119_tld,
dtl_3, sweep_2120_tld, dtl_65, bpmd_2121_tld, dtl_10, otrd_2121_tld, dtl_67, torc_2122_tld,
dtl_68, bhm_2122_tld, dtl_69, bpmw_2126_tld, dtl_70, scrw_2126_tld, duwindow_2126_tld, dtl_71,
duflange_2127_tld, dtl_72, duconcrete_2128_tld, dtl_73, dustart_2130_tld, duabsorb_2130_tld, ensec_2130_tld)
# power supplies 

#  
qf_1996_tld.ps_id = 'QF.1.TLD'
qf_2009_tld.ps_id = 'QF.2.TLD'
qf_2016_tld.ps_id = 'QF.3.TLD'
qf_2024_tld.ps_id = 'QF.4.TLD'
qf_2034_tld.ps_id = 'QF.5.TLD'
qf_2046_tld.ps_id = 'QF.6.TLD'
qf_2058_tld.ps_id = 'QF.7.TLD'
qf_2068_tld.ps_id = 'QF.8.TLD'
qf_2075_tld.ps_id = 'QF.9.TLD'
qk_2095_tld.ps_id = 'QK.1.TLD'
qk_2103_tld.ps_id = 'QK.1.TLD'
qk_2113_tld.ps_id = 'QK.2.TLD'
qk_2115_tld.ps_id = 'QK.2.TLD'
qk_2116_tld.ps_id = 'QK.3.TLD'
qk_2117_tld.ps_id = 'QK.3.TLD'

#  
sa_2016_tld.ps_id = 'SA.1.TLD'
sa_2021_tld.ps_id = 'SA.2.TLD'
sa_2037_tld.ps_id = 'SA.3.TLD'
sk_2096_tld.ps_id = 'SK.1.TLD'
sk_2102_tld.ps_id = 'SK.1.TLD'

#  
bz_1980_tld.ps_id = 'BZ.1.TLD'
bz_1983_tld.ps_id = 'BZ.2.TLD'
bz_1985_tld.ps_id = 'BZ.2.TLD'
bz_1986_tld.ps_id = 'BZ.2.TLD'
bd_2005_tld.ps_id = 'BD.3.TLD'
bd_2006_tld.ps_id = 'BD.3.TLD'
bd_2008_tld.ps_id = 'BD.5.TLD'
bd_2039_tld.ps_id = 'BD.5.TLD'
bd_2066_tld.ps_id = 'BD.4.TLD'
bv_2087_tld.ps_id = 'BV.1.TLD'
bv_2090_tld.ps_id = 'BV.1.TLD'
bv_2093_tld.ps_id = 'BV.1.TLD'
bv_2105_tld.ps_id = 'BV.1.TLD'
bv_2108_tld.ps_id = 'BV.1.TLD'
bv_2111_tld.ps_id = 'BV.1.TLD'
sweep_2119_tld.ps_id = 'SWEEP.1.TLD'
sweep_2120_tld.ps_id = 'SWEEP.2.TLD'
