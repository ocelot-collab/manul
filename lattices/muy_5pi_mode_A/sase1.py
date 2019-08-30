from ocelot import * 
tws = Twiss()
tws.beta_x  = 10.7827828932
tws.beta_y  = 41.7741755441
tws.alpha_x = 0.718794795482
tws.alpha_y = -2.1359197603
tws.E = 14

# drifts 
d_1 = Drift(l=1.472401, eid='D_1')
d_2 = Drift(l=13.997421, eid='D_2')
d_3 = Drift(l=0.208951, eid='D_3')
d_4 = Drift(l=0.153951, eid='D_4')
d_5 = Drift(l=11.37, eid='D_5')
d_6 = Drift(l=0.17, eid='D_6')
d_7 = Drift(l=0.27, eid='D_7')
d_8 = Drift(l=1.742401, eid='D_8')
d_9 = Drift(l=0.472441, eid='D_9')
d_10 = Drift(l=13.525, eid='D_10')
d_11 = Drift(l=0.20895, eid='D_11')
d_12 = Drift(l=0.15395, eid='D_12')
d_13 = Drift(l=6.405, eid='D_13')
d_14 = Drift(l=6.6, eid='D_14')
d_17 = Drift(l=14.005, eid='D_17')
d_20 = Drift(l=14.0051, eid='D_20')
d_23 = Drift(l=14.705, eid='D_23')
d_26 = Drift(l=12.105, eid='D_26')
d_29 = Drift(l=15.205, eid='D_29')
d_32 = Drift(l=6.98, eid='D_32')
d_33 = Drift(l=7.025, eid='D_33')
d_43 = Drift(l=5.38, eid='D_43')
d_44 = Drift(l=5.425, eid='D_44')
d_47 = Drift(l=9.03255, eid='D_47')
d_48 = Drift(l=0.8065, eid='D_48')
d_49 = Drift(l=0.21815, eid='D_49')
d_50 = Drift(l=0.17815, eid='D_50')
d_51 = Drift(l=0.125, eid='D_51')
d_52 = Drift(l=2.1675, eid='D_52')
d_53 = Drift(l=1.8267, eid='D_53')
d_54 = Drift(l=0.15, eid='D_54')
d_55 = Drift(l=0.4323, eid='D_55')
d_56 = Drift(l=0.18665, eid='D_56')
d_57 = Drift(l=0.04015, eid='D_57')
d_58 = Drift(l=5.7595, eid='D_58')
d_60 = Drift(l=5.79965, eid='D_60')
d_63 = Drift(l=0.31772, eid='D_63')
d_64 = Drift(l=0.07278, eid='D_64')
d_65 = Drift(l=0.0717, eid='D_65')
d_66 = Drift(l=0.2973, eid='D_66')
d_68 = Drift(l=0.35787, eid='D_68')

# quadrupoles 
qk_2027_tl = Quadrupole(l=1.0552, k1=-0.0903596001, tilt=0.0, eid='QK.2027.TL')
qf_2042_tl = Quadrupole(l=0.5321, k1=0.1791908476, tilt=0.0, eid='QF.2042.TL')
qk_2057_tl = Quadrupole(l=1.0552, k1=-0.0903596001, tilt=0.0, eid='QK.2057.TL')
qf_2072_t2 = Quadrupole(l=0.5321, k1=0.1791908476, tilt=0.0, eid='QF.2072.T2')
qf_2087_t2 = Quadrupole(l=0.5321, k1=-0.1791908476, tilt=0.0, eid='QF.2087.T2')
qf_2102_t2 = Quadrupole(l=0.5321, k1=0.1791908476, tilt=0.0, eid='QF.2102.T2')
qf_2117_t2 = Quadrupole(l=0.5321, k1=-0.1791908476, tilt=0.0, eid='QF.2117.T2')
qf_2132_t2 = Quadrupole(l=0.5321, k1=0.1791908476, tilt=0.0, eid='QF.2132.T2')
qf_2145_t2 = Quadrupole(l=0.5321, k1=-0.1791908476, tilt=0.0, eid='QF.2145.T2')
qf_2162_t2 = Quadrupole(l=0.5321, k1=0.1791908476, tilt=0.0, eid='QF.2162.T2')
qf_2177_t2 = Quadrupole(l=0.5321, k1=-0.1525567278, tilt=0.0, eid='QF.2177.T2')
qf_2192_t2 = Quadrupole(l=0.5321, k1=0.1521721569, tilt=0.0, eid='QF.2192.T2')
qf_2207_t2 = Quadrupole(l=0.5321, k1=-0.1259982434, tilt=0.0, eid='QF.2207.T2')
qf_2218_t2 = Quadrupole(l=0.5321, k1=0.1191993195, tilt=0.0, eid='QF.2218.T2')
qa_2229_t2 = Quadrupole(l=0.1137, k1=-0.5445788788, tilt=0.0, eid='QA.2229.T2')
qa_2235_t2 = Quadrupole(l=0.1137, k1=0.5501622372, tilt=0.0, eid='QA.2235.T2')
qa_2241_sa1 = Quadrupole(l=0.1137, k1=-0.5445788788, tilt=0.0, eid='QA.2241.SA1')
qa_2247_sa1 = Quadrupole(l=0.1137, k1=0.5501622372, tilt=0.0, eid='QA.2247.SA1')
qa_2253_sa1 = Quadrupole(l=0.1137, k1=-0.5445788788, tilt=0.0, eid='QA.2253.SA1')
qa_2259_sa1 = Quadrupole(l=0.1137, k1=0.5501622372, tilt=0.0, eid='QA.2259.SA1')
qa_2266_sa1 = Quadrupole(l=0.1137, k1=-0.5445788788, tilt=0.0, eid='QA.2266.SA1')
qa_2272_sa1 = Quadrupole(l=0.1137, k1=0.5501622372, tilt=0.0, eid='QA.2272.SA1')
qa_2278_sa1 = Quadrupole(l=0.1137, k1=-0.5445788788, tilt=0.0, eid='QA.2278.SA1')
qa_2284_sa1 = Quadrupole(l=0.1137, k1=0.5501622372, tilt=0.0, eid='QA.2284.SA1')
qa_2290_sa1 = Quadrupole(l=0.1137, k1=-0.5445788788, tilt=0.0, eid='QA.2290.SA1')
qa_2296_sa1 = Quadrupole(l=0.1137, k1=0.5501622372, tilt=0.0, eid='QA.2296.SA1')
qa_2302_sa1 = Quadrupole(l=0.1137, k1=-0.5445788788, tilt=0.0, eid='QA.2302.SA1')
qa_2308_sa1 = Quadrupole(l=0.1137, k1=0.5501622372, tilt=0.0, eid='QA.2308.SA1')
qa_2314_sa1 = Quadrupole(l=0.1137, k1=-0.5445788788, tilt=0.0, eid='QA.2314.SA1')
qa_2320_sa1 = Quadrupole(l=0.1137, k1=0.5501622372, tilt=0.0, eid='QA.2320.SA1')
qa_2327_sa1 = Quadrupole(l=0.1137, k1=-0.5445788788, tilt=0.0, eid='QA.2327.SA1')
qa_2333_sa1 = Quadrupole(l=0.1137, k1=0.5501622372, tilt=0.0, eid='QA.2333.SA1')
qa_2339_sa1 = Quadrupole(l=0.1137, k1=-0.5445788788, tilt=0.0, eid='QA.2339.SA1')
qa_2345_sa1 = Quadrupole(l=0.1137, k1=0.5501622372, tilt=0.0, eid='QA.2345.SA1')
qa_2351_sa1 = Quadrupole(l=0.1137, k1=-0.5445788788, tilt=0.0, eid='QA.2351.SA1')
qa_2357_sa1 = Quadrupole(l=0.1137, k1=0.5501622372, tilt=0.0, eid='QA.2357.SA1')
qa_2363_sa1 = Quadrupole(l=0.1137, k1=-0.5445788788, tilt=0.0, eid='QA.2363.SA1')
qa_2369_sa1 = Quadrupole(l=0.1137, k1=0.5501622372, tilt=0.0, eid='QA.2369.SA1')
qa_2375_sa1 = Quadrupole(l=0.1137, k1=-0.5445788788, tilt=0.0, eid='QA.2375.SA1')
qa_2381_sa1 = Quadrupole(l=0.1137, k1=0.5501622372, tilt=0.0, eid='QA.2381.SA1')
qa_2388_sa1 = Quadrupole(l=0.1137, k1=-0.5445788788, tilt=0.0, eid='QA.2388.SA1')
qa_2394_sa1 = Quadrupole(l=0.1137, k1=0.5501622372, tilt=0.0, eid='QA.2394.SA1')
qa_2400_sa1 = Quadrupole(l=0.1137, k1=-0.5445788788, tilt=0.0, eid='QA.2400.SA1')
qa_2406_sa1 = Quadrupole(l=0.1137, k1=0.5501622372, tilt=0.0, eid='QA.2406.SA1')
qa_2412_sa1 = Quadrupole(l=0.1137, k1=-0.5445788788, tilt=0.0, eid='QA.2412.SA1')
qa_2418_sa1 = Quadrupole(l=0.1137, k1=0.5501622372, tilt=0.0, eid='QA.2418.SA1')
qa_2424_sa1 = Quadrupole(l=0.1137, k1=-0.5445788788, tilt=0.0, eid='QA.2424.SA1')
qa_2430_sa1 = Quadrupole(l=0.1137, k1=0.5501622372, tilt=0.0, eid='QA.2430.SA1')
qa_2436_sa1 = Quadrupole(l=0.1137, k1=-0.5445788788, tilt=0.0, eid='QA.2436.SA1')
qa_2442_sa1 = Quadrupole(l=0.1137, k1=0.5501622372, tilt=0.0, eid='QA.2442.SA1')
qa_2449_sa1 = Quadrupole(l=0.1137, k1=-0.5445788788, tilt=0.0, eid='QA.2449.SA1')
qa_2455_sa1 = Quadrupole(l=0.1137, k1=0.5501622372, tilt=0.0, eid='QA.2455.SA1')
qa_2461_sa1 = Quadrupole(l=0.1137, k1=-0.5445788788, tilt=0.0, eid='QA.2461.SA1')

# bending magnets 
bd_2079_t2 = RBend(l = 1.0, angle=0.0, e1=0.0, e2=0.0, gap=0, tilt=0, fint=0.0, fintx=0.0, eid='BD.2079.T2')

# correctors 
cfx_2042_tl = Hcor(l=0.1, angle=0.0, eid='CFX.2042.TL')
chx_2054_tl = Hcor(l=0.2, angle=0.0, eid='CHX.2054.TL')
chy_2054_tl = Vcor(l=0.2, angle=0.0, eid='CHY.2054.TL')
cfx_2072_t2 = Hcor(l=0.1, angle=0.0, eid='CFX.2072.T2')
cfy_2087_t2 = Vcor(l=0.1, angle=0.0, eid='CFY.2087.T2')
cfx_2102_t2 = Hcor(l=0.1, angle=0.0, eid='CFX.2102.T2')
cfy_2117_t2 = Vcor(l=0.1, angle=0.0, eid='CFY.2117.T2')
cfx_2133_t2 = Hcor(l=0.1, angle=0.0, eid='CFX.2133.T2')
cfy_2146_t2 = Vcor(l=0.1, angle=0.0, eid='CFY.2146.T2')
cfx_2162_t2 = Hcor(l=0.1, angle=0.0, eid='CFX.2162.T2')
cfy_2177_t2 = Vcor(l=0.1, angle=0.0, eid='CFY.2177.T2')
cfx_2192_t2 = Hcor(l=0.1, angle=0.0, eid='CFX.2192.T2')
cfy_2207_t2 = Vcor(l=0.1, angle=0.0, eid='CFY.2207.T2')
cfx_2219_t2 = Hcor(l=0.1, angle=0.0, eid='CFX.2219.T2')
cny_2229_t2 = Vcor(l=0.3, angle=0.0, eid='CNY.2229.T2')
cex_2230_t2 = Hcor(l=0.1, angle=0.0, eid='CEX.2230.T2')
cny_2234_t2 = Vcor(l=0.3, angle=0.0, eid='CNY.2234.T2')
cex_2234_t2 = Hcor(l=0.1, angle=0.0, eid='CEX.2234.T2')
cax_2248_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2248.SA1')
cay_2248_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2248.SA1')
cbx_2253_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2253.SA1')
cby_2253_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2253.SA1')
cax_2254_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2254.SA1')
cay_2254_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2254.SA1')
cbx_2259_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2259.SA1')
cby_2259_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2259.SA1')
cax_2260_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2260.SA1')
cay_2260_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2260.SA1')
cbx_2265_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2265.SA1')
cby_2265_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2265.SA1')
cax_2267_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2267.SA1')
cay_2267_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2267.SA1')
cbx_2271_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2271.SA1')
cby_2271_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2271.SA1')
cax_2273_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2273.SA1')
cay_2273_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2273.SA1')
cbx_2277_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2277.SA1')
cby_2277_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2277.SA1')
cax_2279_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2279.SA1')
cay_2279_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2279.SA1')
cbx_2283_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2283.SA1')
cby_2283_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2283.SA1')
cax_2285_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2285.SA1')
cay_2285_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2285.SA1')
cbx_2289_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2289.SA1')
cby_2289_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2289.SA1')
cax_2291_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2291.SA1')
cay_2291_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2291.SA1')
cbx_2296_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2296.SA1')
cby_2296_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2296.SA1')
cax_2297_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2297.SA1')
cay_2297_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2297.SA1')
cbx_2302_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2302.SA1')
cby_2302_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2302.SA1')
cax_2303_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2303.SA1')
cay_2303_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2303.SA1')
cbx_2308_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2308.SA1')
cby_2308_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2308.SA1')
cax_2309_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2309.SA1')
cay_2309_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2309.SA1')
cbx_2314_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2314.SA1')
cby_2314_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2314.SA1')
cax_2315_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2315.SA1')
cay_2315_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2315.SA1')
cbx_2320_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2320.SA1')
cby_2320_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2320.SA1')
cax_2321_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2321.SA1')
cay_2321_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2321.SA1')
cbx_2326_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2326.SA1')
cby_2326_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2326.SA1')
cax_2328_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2328.SA1')
cay_2328_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2328.SA1')
cbx_2332_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2332.SA1')
cby_2332_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2332.SA1')
cax_2334_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2334.SA1')
cay_2334_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2334.SA1')
cbx_2338_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2338.SA1')
cby_2338_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2338.SA1')
cax_2340_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2340.SA1')
cay_2340_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2340.SA1')
cbx_2344_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2344.SA1')
cby_2344_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2344.SA1')
cax_2346_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2346.SA1')
cay_2346_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2346.SA1')
cbx_2350_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2350.SA1')
cby_2350_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2350.SA1')
cax_2352_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2352.SA1')
cay_2352_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2352.SA1')
cbx_2357_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2357.SA1')
cby_2357_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2357.SA1')
cax_2358_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2358.SA1')
cay_2358_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2358.SA1')
cbx_2363_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2363.SA1')
cby_2363_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2363.SA1')
cax_2364_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2364.SA1')
cay_2364_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2364.SA1')
cbx_2369_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2369.SA1')
cby_2369_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2369.SA1')
cax_2370_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2370.SA1')
cay_2370_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2370.SA1')
cbx_2375_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2375.SA1')
cby_2375_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2375.SA1')
cax_2376_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2376.SA1')
cay_2376_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2376.SA1')
cbx_2381_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2381.SA1')
cby_2381_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2381.SA1')
cax_2382_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2382.SA1')
cay_2382_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2382.SA1')
cbx_2387_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2387.SA1')
cby_2387_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2387.SA1')
cax_2389_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2389.SA1')
cay_2389_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2389.SA1')
cbx_2393_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2393.SA1')
cby_2393_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2393.SA1')
cax_2395_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2395.SA1')
cay_2395_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2395.SA1')
cbx_2399_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2399.SA1')
cby_2399_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2399.SA1')
cax_2401_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2401.SA1')
cay_2401_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2401.SA1')
cbx_2405_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2405.SA1')
cby_2405_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2405.SA1')
cax_2407_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2407.SA1')
cay_2407_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2407.SA1')
cbx_2411_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2411.SA1')
cby_2411_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2411.SA1')
cax_2413_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2413.SA1')
cay_2413_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2413.SA1')
cbx_2418_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2418.SA1')
cby_2418_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2418.SA1')
cax_2419_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2419.SA1')
cay_2419_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2419.SA1')
cbx_2424_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2424.SA1')
cby_2424_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2424.SA1')
cax_2425_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2425.SA1')
cay_2425_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2425.SA1')
cbx_2430_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2430.SA1')
cby_2430_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2430.SA1')
cax_2431_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2431.SA1')
cay_2431_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2431.SA1')
cbx_2436_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2436.SA1')
cby_2436_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2436.SA1')
cax_2437_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2437.SA1')
cay_2437_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2437.SA1')
cbx_2442_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2442.SA1')
cby_2442_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2442.SA1')
cax_2443_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2443.SA1')
cay_2443_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2443.SA1')
cbx_2448_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2448.SA1')
cby_2448_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2448.SA1')
cax_2450_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2450.SA1')
cay_2450_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2450.SA1')
cbx_2454_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2454.SA1')
cby_2454_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2454.SA1')
cax_2456_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2456.SA1')
cay_2456_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2456.SA1')
cbx_2460_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2460.SA1')
cby_2460_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2460.SA1')

# markers 
stsub_2025_tl = Marker(eid='STSUB.2025.TL')
ensub_2058_tl = Marker(eid='ENSUB.2058.TL')
ensec_2058_tl = Marker(eid='ENSEC.2058.TL')
stsec_2058_t2 = Marker(eid='STSEC.2058.T2')
otrb_2169_t2 = Marker(eid='OTRB.2169.T2')
otrb_2199_t2 = Marker(eid='OTRB.2199.T2')
otrb_2212_t2 = Marker(eid='OTRB.2212.T2')
tora_2228_t2 = Marker(eid='TORA.2228.T2')
ensec_2235_t2 = Marker(eid='ENSEC.2235.T2')
stsec_2235_sa1 = Marker(eid='STSEC.2235.SA1')
match_2247_sa1 = Marker(eid='MATCH.2247.SA1')
ensec_2461_sa1 = Marker(eid='ENSEC.2461.SA1')
stsec_2461_t4 = Marker(eid='STSEC.2461.T4')

# monitor 
bpma_2041_tl = Monitor(eid='BPMA.2041.TL')
bpma_2054_tl = Monitor(eid='BPMA.2054.TL')
bpma_2071_t2 = Monitor(eid='BPMA.2071.T2')
bpma_2086_t2 = Monitor(eid='BPMA.2086.T2')
bpma_2101_t2 = Monitor(eid='BPMA.2101.T2')
bpma_2116_t2 = Monitor(eid='BPMA.2116.T2')
bpma_2132_t2 = Monitor(eid='BPMA.2132.T2')
bpma_2145_t2 = Monitor(eid='BPMA.2145.T2')
bpma_2161_t2 = Monitor(eid='BPMA.2161.T2')
bpma_2176_t2 = Monitor(eid='BPMA.2176.T2')
bpma_2191_t2 = Monitor(eid='BPMA.2191.T2')
bpma_2206_t2 = Monitor(eid='BPMA.2206.T2')
bpma_2218_t2 = Monitor(eid='BPMA.2218.T2')
bpme_2229_t2 = Monitor(eid='BPME.2229.T2')
bpme_2235_t2 = Monitor(eid='BPME.2235.T2')
bpme_2241_sa1 = Monitor(eid='BPME.2241.SA1')
bpme_2247_sa1 = Monitor(eid='BPME.2247.SA1')
bpme_2253_sa1 = Monitor(eid='BPME.2253.SA1')
bpme_2259_sa1 = Monitor(eid='BPME.2259.SA1')
bpme_2265_sa1 = Monitor(eid='BPME.2265.SA1')
bpme_2271_sa1 = Monitor(eid='BPME.2271.SA1')
bpme_2278_sa1 = Monitor(eid='BPME.2278.SA1')
bpme_2284_sa1 = Monitor(eid='BPME.2284.SA1')
bpme_2290_sa1 = Monitor(eid='BPME.2290.SA1')
bpme_2296_sa1 = Monitor(eid='BPME.2296.SA1')
bpme_2302_sa1 = Monitor(eid='BPME.2302.SA1')
bpme_2308_sa1 = Monitor(eid='BPME.2308.SA1')
bpme_2314_sa1 = Monitor(eid='BPME.2314.SA1')
bpme_2320_sa1 = Monitor(eid='BPME.2320.SA1')
bpme_2326_sa1 = Monitor(eid='BPME.2326.SA1')
bpme_2332_sa1 = Monitor(eid='BPME.2332.SA1')
bpme_2339_sa1 = Monitor(eid='BPME.2339.SA1')
bpme_2345_sa1 = Monitor(eid='BPME.2345.SA1')
bpme_2351_sa1 = Monitor(eid='BPME.2351.SA1')
bpme_2357_sa1 = Monitor(eid='BPME.2357.SA1')
bpme_2363_sa1 = Monitor(eid='BPME.2363.SA1')
bpme_2369_sa1 = Monitor(eid='BPME.2369.SA1')
bpme_2375_sa1 = Monitor(eid='BPME.2375.SA1')
bpme_2381_sa1 = Monitor(eid='BPME.2381.SA1')
bpme_2387_sa1 = Monitor(eid='BPME.2387.SA1')
bpme_2393_sa1 = Monitor(eid='BPME.2393.SA1')
bpme_2400_sa1 = Monitor(eid='BPME.2400.SA1')
bpme_2406_sa1 = Monitor(eid='BPME.2406.SA1')
bpme_2412_sa1 = Monitor(eid='BPME.2412.SA1')
bpme_2418_sa1 = Monitor(eid='BPME.2418.SA1')
bpme_2424_sa1 = Monitor(eid='BPME.2424.SA1')
bpme_2430_sa1 = Monitor(eid='BPME.2430.SA1')
bpme_2436_sa1 = Monitor(eid='BPME.2436.SA1')
bpme_2442_sa1 = Monitor(eid='BPME.2442.SA1')
bpme_2448_sa1 = Monitor(eid='BPME.2448.SA1')
bpme_2454_sa1 = Monitor(eid='BPME.2454.SA1')
bpme_2461_sa1 = Monitor(eid='BPME.2461.SA1')

# sextupoles 

# octupole 

# undulator
K = 3.
u40s_2232_t2 = Undulator(lperiod=0.04, nperiods=3, Kx=K, Ky=0.0, eid='U40S.2232.T2')
u40_2250_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2250.SA1')
u40_2256_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2256.SA1')
u40_2262_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2262.SA1')
u40_2269_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2269.SA1')
u40_2275_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2275.SA1')
u40_2281_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2281.SA1')
u40_2287_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2287.SA1')
u40_2293_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2293.SA1')
u40_2299_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2299.SA1')
u40_2305_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2305.SA1')
u40_2311_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2311.SA1')
u40_2317_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2317.SA1')
u40_2323_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2323.SA1')
u40_2330_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2330.SA1')
u40_2336_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2336.SA1')
u40_2342_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2342.SA1')
u40_2348_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2348.SA1')
u40_2354_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2354.SA1')
u40_2360_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2360.SA1')
u40_2366_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2366.SA1')
u40_2372_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2372.SA1')
u40_2378_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2378.SA1')
u40_2384_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2384.SA1')
u40_2391_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2391.SA1')
u40_2397_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2397.SA1')
u40_2403_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2403.SA1')
u40_2409_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2409.SA1')
u40_2415_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2415.SA1')
u40_2421_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2421.SA1')
u40_2427_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2427.SA1')
u40_2433_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2433.SA1')
u40_2439_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2439.SA1')
u40_2445_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2445.SA1')
u40_2452_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2452.SA1')
u40_2458_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=K, Ky=0.0, eid='U40.2458.SA1')

# cavity 

# UnknowElement 

# Matrices 

# Solenoids 

# lattice 
cell = (stsub_2025_tl, d_1, qk_2027_tl, d_2, bpma_2041_tl, d_3, qf_2042_tl, 
d_4, cfx_2042_tl, d_5, chx_2054_tl, d_6, chy_2054_tl, d_7, bpma_2054_tl, 
d_8, qk_2057_tl, d_9, ensub_2058_tl, ensec_2058_tl, stsec_2058_t2, d_10, bpma_2071_t2, 
d_11, qf_2072_t2, d_12, cfx_2072_t2, d_13, bd_2079_t2, d_14, bpma_2086_t2, 
d_11, qf_2087_t2, d_12, cfy_2087_t2, d_17, bpma_2101_t2, d_11, qf_2102_t2, 
d_12, cfx_2102_t2, d_20, bpma_2116_t2, d_11, qf_2117_t2, d_12, cfy_2117_t2, 
d_23, bpma_2132_t2, d_11, qf_2132_t2, d_12, cfx_2133_t2, d_26, bpma_2145_t2, 
d_11, qf_2145_t2, d_12, cfy_2146_t2, d_29, bpma_2161_t2, d_11, qf_2162_t2, 
d_12, cfx_2162_t2, d_32, otrb_2169_t2, d_33, bpma_2176_t2, d_11, qf_2177_t2, 
d_12, cfy_2177_t2, d_17, bpma_2191_t2, d_11, qf_2192_t2, d_12, cfx_2192_t2, 
d_32, otrb_2199_t2, d_33, bpma_2206_t2, d_11, qf_2207_t2, d_12, cfy_2207_t2, 
d_43, otrb_2212_t2, d_44, bpma_2218_t2, d_11, qf_2218_t2, d_12, cfx_2219_t2, 
d_47, tora_2228_t2, d_48, bpme_2229_t2, d_49, qa_2229_t2, d_50, cny_2229_t2, 
d_51, cex_2230_t2, d_52, u40s_2232_t2, d_53, cny_2234_t2, d_54, cex_2234_t2, 
d_55, bpme_2235_t2, d_56, qa_2235_t2, d_57, ensec_2235_t2, stsec_2235_sa1, d_58, 
bpme_2241_sa1, d_56, qa_2241_sa1, d_60, bpme_2247_sa1, d_56, qa_2247_sa1, d_57, 
match_2247_sa1, d_63, cax_2248_sa1, cay_2248_sa1, d_64, u40_2250_sa1, d_65, cbx_2253_sa1, 
cby_2253_sa1, d_66, bpme_2253_sa1, d_56, qa_2253_sa1, d_68, cax_2254_sa1, cay_2254_sa1, 
d_64, u40_2256_sa1, d_65, cbx_2259_sa1, cby_2259_sa1, d_66, bpme_2259_sa1, d_56, 
qa_2259_sa1, d_68, cax_2260_sa1, cay_2260_sa1, d_64, u40_2262_sa1, d_65, cbx_2265_sa1, 
cby_2265_sa1, d_66, bpme_2265_sa1, d_56, qa_2266_sa1, d_68, cax_2267_sa1, cay_2267_sa1, 
d_64, u40_2269_sa1, d_65, cbx_2271_sa1, cby_2271_sa1, d_66, bpme_2271_sa1, d_56, 
qa_2272_sa1, d_68, cax_2273_sa1, cay_2273_sa1, d_64, u40_2275_sa1, d_65, cbx_2277_sa1, 
cby_2277_sa1, d_66, bpme_2278_sa1, d_56, qa_2278_sa1, d_68, cax_2279_sa1, cay_2279_sa1, 
d_64, u40_2281_sa1, d_65, cbx_2283_sa1, cby_2283_sa1, d_66, bpme_2284_sa1, d_56, 
qa_2284_sa1, d_68, cax_2285_sa1, cay_2285_sa1, d_64, u40_2287_sa1, d_65, cbx_2289_sa1, 
cby_2289_sa1, d_66, bpme_2290_sa1, d_56, qa_2290_sa1, d_68, cax_2291_sa1, cay_2291_sa1, 
d_64, u40_2293_sa1, d_65, cbx_2296_sa1, cby_2296_sa1, d_66, bpme_2296_sa1, d_56, 
qa_2296_sa1, d_68, cax_2297_sa1, cay_2297_sa1, d_64, u40_2299_sa1, d_65, cbx_2302_sa1, 
cby_2302_sa1, d_66, bpme_2302_sa1, d_56, qa_2302_sa1, d_68, cax_2303_sa1, cay_2303_sa1, 
d_64, u40_2305_sa1, d_65, cbx_2308_sa1, cby_2308_sa1, d_66, bpme_2308_sa1, d_56, 
qa_2308_sa1, d_68, cax_2309_sa1, cay_2309_sa1, d_64, u40_2311_sa1, d_65, cbx_2314_sa1, 
cby_2314_sa1, d_66, bpme_2314_sa1, d_56, qa_2314_sa1, d_68, cax_2315_sa1, cay_2315_sa1, 
d_64, u40_2317_sa1, d_65, cbx_2320_sa1, cby_2320_sa1, d_66, bpme_2320_sa1, d_56, 
qa_2320_sa1, d_68, cax_2321_sa1, cay_2321_sa1, d_64, u40_2323_sa1, d_65, cbx_2326_sa1, 
cby_2326_sa1, d_66, bpme_2326_sa1, d_56, qa_2327_sa1, d_68, cax_2328_sa1, cay_2328_sa1, 
d_64, u40_2330_sa1, d_65, cbx_2332_sa1, cby_2332_sa1, d_66, bpme_2332_sa1, d_56, 
qa_2333_sa1, d_68, cax_2334_sa1, cay_2334_sa1, d_64, u40_2336_sa1, d_65, cbx_2338_sa1, 
cby_2338_sa1, d_66, bpme_2339_sa1, d_56, qa_2339_sa1, d_68, cax_2340_sa1, cay_2340_sa1, 
d_64, u40_2342_sa1, d_65, cbx_2344_sa1, cby_2344_sa1, d_66, bpme_2345_sa1, d_56, 
qa_2345_sa1, d_68, cax_2346_sa1, cay_2346_sa1, d_64, u40_2348_sa1, d_65, cbx_2350_sa1, 
cby_2350_sa1, d_66, bpme_2351_sa1, d_56, qa_2351_sa1, d_68, cax_2352_sa1, cay_2352_sa1, 
d_64, u40_2354_sa1, d_65, cbx_2357_sa1, cby_2357_sa1, d_66, bpme_2357_sa1, d_56, 
qa_2357_sa1, d_68, cax_2358_sa1, cay_2358_sa1, d_64, u40_2360_sa1, d_65, cbx_2363_sa1, 
cby_2363_sa1, d_66, bpme_2363_sa1, d_56, qa_2363_sa1, d_68, cax_2364_sa1, cay_2364_sa1, 
d_64, u40_2366_sa1, d_65, cbx_2369_sa1, cby_2369_sa1, d_66, bpme_2369_sa1, d_56, 
qa_2369_sa1, d_68, cax_2370_sa1, cay_2370_sa1, d_64, u40_2372_sa1, d_65, cbx_2375_sa1, 
cby_2375_sa1, d_66, bpme_2375_sa1, d_56, qa_2375_sa1, d_68, cax_2376_sa1, cay_2376_sa1, 
d_64, u40_2378_sa1, d_65, cbx_2381_sa1, cby_2381_sa1, d_66, bpme_2381_sa1, d_56, 
qa_2381_sa1, d_68, cax_2382_sa1, cay_2382_sa1, d_64, u40_2384_sa1, d_65, cbx_2387_sa1, 
cby_2387_sa1, d_66, bpme_2387_sa1, d_56, qa_2388_sa1, d_68, cax_2389_sa1, cay_2389_sa1, 
d_64, u40_2391_sa1, d_65, cbx_2393_sa1, cby_2393_sa1, d_66, bpme_2393_sa1, d_56, 
qa_2394_sa1, d_68, cax_2395_sa1, cay_2395_sa1, d_64, u40_2397_sa1, d_65, cbx_2399_sa1, 
cby_2399_sa1, d_66, bpme_2400_sa1, d_56, qa_2400_sa1, d_68, cax_2401_sa1, cay_2401_sa1, 
d_64, u40_2403_sa1, d_65, cbx_2405_sa1, cby_2405_sa1, d_66, bpme_2406_sa1, d_56, 
qa_2406_sa1, d_68, cax_2407_sa1, cay_2407_sa1, d_64, u40_2409_sa1, d_65, cbx_2411_sa1, 
cby_2411_sa1, d_66, bpme_2412_sa1, d_56, qa_2412_sa1, d_68, cax_2413_sa1, cay_2413_sa1, 
d_64, u40_2415_sa1, d_65, cbx_2418_sa1, cby_2418_sa1, d_66, bpme_2418_sa1, d_56, 
qa_2418_sa1, d_68, cax_2419_sa1, cay_2419_sa1, d_64, u40_2421_sa1, d_65, cbx_2424_sa1, 
cby_2424_sa1, d_66, bpme_2424_sa1, d_56, qa_2424_sa1, d_68, cax_2425_sa1, cay_2425_sa1, 
d_64, u40_2427_sa1, d_65, cbx_2430_sa1, cby_2430_sa1, d_66, bpme_2430_sa1, d_56, 
qa_2430_sa1, d_68, cax_2431_sa1, cay_2431_sa1, d_64, u40_2433_sa1, d_65, cbx_2436_sa1, 
cby_2436_sa1, d_66, bpme_2436_sa1, d_56, qa_2436_sa1, d_68, cax_2437_sa1, cay_2437_sa1, 
d_64, u40_2439_sa1, d_65, cbx_2442_sa1, cby_2442_sa1, d_66, bpme_2442_sa1, d_56, 
qa_2442_sa1, d_68, cax_2443_sa1, cay_2443_sa1, d_64, u40_2445_sa1, d_65, cbx_2448_sa1, 
cby_2448_sa1, d_66, bpme_2448_sa1, d_56, qa_2449_sa1, d_68, cax_2450_sa1, cay_2450_sa1, 
d_64, u40_2452_sa1, d_65, cbx_2454_sa1, cby_2454_sa1, d_66, bpme_2454_sa1, d_56, 
qa_2455_sa1, d_68, cax_2456_sa1, cay_2456_sa1, d_64, u40_2458_sa1, d_65, cbx_2460_sa1, 
cby_2460_sa1, d_66, bpme_2461_sa1, d_56, qa_2461_sa1, d_57, ensec_2461_sa1, stsec_2461_t4)
# power supplies 

#  
qk_2027_tl.ps_id = 'QK.2.TL'
qf_2042_tl.ps_id = 'QF.1.TL'
qk_2057_tl.ps_id = 'QK.2.TL'
qf_2072_t2.ps_id = 'QF.1.T2'
qf_2087_t2.ps_id = 'QF.1.T2'
qf_2102_t2.ps_id = 'QF.1.T2'
qf_2117_t2.ps_id = 'QF.1.T2'
qf_2132_t2.ps_id = 'QF.1.T2'
qf_2145_t2.ps_id = 'QF.2.T2'
qf_2162_t2.ps_id = 'QF.2.T2'
qf_2177_t2.ps_id = 'QF.3.T2'
qf_2192_t2.ps_id = 'QF.4.T2'
qf_2207_t2.ps_id = 'QF.5.T2'
qf_2218_t2.ps_id = 'QF.6.T2'
qa_2229_t2.ps_id = 'QA.1.T2'
qa_2235_t2.ps_id = 'QA.2.T2'
qa_2241_sa1.ps_id = 'QA.1.SA1'
qa_2247_sa1.ps_id = 'QA.2.SA1'
qa_2253_sa1.ps_id = 'QA.1.SA1'
qa_2259_sa1.ps_id = 'QA.2.SA1'
qa_2266_sa1.ps_id = 'QA.1.SA1'
qa_2272_sa1.ps_id = 'QA.2.SA1'
qa_2278_sa1.ps_id = 'QA.1.SA1'
qa_2284_sa1.ps_id = 'QA.2.SA1'
qa_2290_sa1.ps_id = 'QA.1.SA1'
qa_2296_sa1.ps_id = 'QA.2.SA1'
qa_2302_sa1.ps_id = 'QA.1.SA1'
qa_2308_sa1.ps_id = 'QA.2.SA1'
qa_2314_sa1.ps_id = 'QA.1.SA1'
qa_2320_sa1.ps_id = 'QA.2.SA1'
qa_2327_sa1.ps_id = 'QA.1.SA1'
qa_2333_sa1.ps_id = 'QA.2.SA1'
qa_2339_sa1.ps_id = 'QA.1.SA1'
qa_2345_sa1.ps_id = 'QA.2.SA1'
qa_2351_sa1.ps_id = 'QA.1.SA1'
qa_2357_sa1.ps_id = 'QA.2.SA1'
qa_2363_sa1.ps_id = 'QA.1.SA1'
qa_2369_sa1.ps_id = 'QA.2.SA1'
qa_2375_sa1.ps_id = 'QA.1.SA1'
qa_2381_sa1.ps_id = 'QA.2.SA1'
qa_2388_sa1.ps_id = 'QA.1.SA1'
qa_2394_sa1.ps_id = 'QA.2.SA1'
qa_2400_sa1.ps_id = 'QA.1.SA1'
qa_2406_sa1.ps_id = 'QA.2.SA1'
qa_2412_sa1.ps_id = 'QA.1.SA1'
qa_2418_sa1.ps_id = 'QA.2.SA1'
qa_2424_sa1.ps_id = 'QA.1.SA1'
qa_2430_sa1.ps_id = 'QA.2.SA1'
qa_2436_sa1.ps_id = 'QA.1.SA1'
qa_2442_sa1.ps_id = 'QA.2.SA1'
qa_2449_sa1.ps_id = 'QA.1.SA1'
qa_2455_sa1.ps_id = 'QA.2.SA1'
qa_2461_sa1.ps_id = 'QA.1.SA1'

#  

#  

#  

#  
bd_2079_t2.ps_id = 'BD.10.T2'
