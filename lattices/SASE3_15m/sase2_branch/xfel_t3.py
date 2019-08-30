from ocelot import * 

# drifts 
d_2 = Drift(l=1.3805, eid='D_2')
d_3 = Drift(l=5.678, eid='D_3')
d_4 = Drift(l=0.205, eid='D_4')
d_5 = Drift(l=0.14, eid='D_5')
d_6 = Drift(l=11.925, eid='D_6')
d_15 = Drift(l=19.01, eid='D_15')
d_18 = Drift(l=21.065, eid='D_18')
d_21 = Drift(l=18.72, eid='D_21')
d_22 = Drift(l=0.21045, eid='D_22')
d_23 = Drift(l=0.15545, eid='D_23')
d_24 = Drift(l=1.545, eid='D_24')
d_27 = Drift(l=9.06, eid='D_27')
d_28 = Drift(l=0.185, eid='D_28')
d_29 = Drift(l=0.182, eid='D_29')
d_30 = Drift(l=0.21845, eid='D_30')
d_31 = Drift(l=0.38545, eid='D_31')
d_32 = Drift(l=2.5e-05, eid='D_32')
d_33 = Drift(l=1.070175, eid='D_33')
d_34 = Drift(l=3.59515, eid='D_34')
d_35 = Drift(l=0.34515, eid='D_35')
d_36 = Drift(l=0.29015, eid='D_36')
d_37 = Drift(l=0.6718, eid='D_37')
d_38 = Drift(l=2.1168, eid='D_38')
d_41 = Drift(l=1.3218, eid='D_41')
d_42 = Drift(l=1.0768, eid='D_42')
d_43 = Drift(l=0.19, eid='D_43')
d_45 = Drift(l=0.370175, eid='D_45')
d_46 = Drift(l=0.875025, eid='D_46')
d_49 = Drift(l=9.835, eid='D_49')
d_55 = Drift(l=18.61, eid='D_55')
d_67 = Drift(l=13.515, eid='D_67')
d_68 = Drift(l=0.391, eid='D_68')
d_69 = Drift(l=7.139, eid='D_69')
d_78 = Drift(l=9.676, eid='D_78')

# quadrupoles 
qe_2430_t3 = Quadrupole(l=0.24, k1=0.2237922517, tilt=0.0, eid='QE.2430.T3')
qe_2443_t3 = Quadrupole(l=0.24, k1=-0.2040914523, tilt=0.0, eid='QE.2443.T3')
qe_2455_t3 = Quadrupole(l=0.24, k1=0.24059635850000002, tilt=0.0, eid='QE.2455.T3')
qe_2468_t3 = Quadrupole(l=0.24, k1=-0.23065976070000002, tilt=0.0, eid='QE.2468.T3')
qe_2487_t3 = Quadrupole(l=0.24, k1=0.19227955160000001, tilt=0.0, eid='QE.2487.T3')
qe_2509_t3 = Quadrupole(l=0.24, k1=-0.19227955160000001, tilt=0.0, eid='QE.2509.T3')
qh_2529_t3 = Quadrupole(l=1.0291, k1=0.19651887780001945, tilt=0.0, eid='QH.2529.T3')
qh_2532_t3 = Quadrupole(l=1.0291, k1=-0.19651370810028182, tilt=0.0, eid='QH.2532.T3')
qh_2544_t3 = Quadrupole(l=1.0291, k1=0.29487653610047615, tilt=0.0, eid='QH.2544.T3')
qm_2549_t3 = Quadrupole(l=1.0597, k1=-0.28678140370010374, tilt=0.0, eid='QM.2549.T3')
qm_2554_t3 = Quadrupole(l=1.0597, k1=0.2879068968000377, tilt=0.0, eid='QM.2554.T3')
qm_2559_t3 = Quadrupole(l=1.0597, k1=-0.28678140370010374, tilt=0.0, eid='QM.2559.T3')
qm_2564_t3 = Quadrupole(l=1.0597, k1=0.2879068968000377, tilt=0.0, eid='QM.2564.T3')
qh_2569_t3 = Quadrupole(l=1.0291, k1=-0.2946863598999126, tilt=0.0, eid='QH.2569.T3')
qh_2580_t3 = Quadrupole(l=1.0291, k1=0.19651887780001945, tilt=0.0, eid='QH.2580.T3')
qh_2583_t3 = Quadrupole(l=1.0291, k1=-0.19651370810028182, tilt=0.0, eid='QH.2583.T3')
qe_2603_t3 = Quadrupole(l=0.24, k1=0.19227955160000001, tilt=0.0, eid='QE.2603.T3')
qe_2625_t3 = Quadrupole(l=0.24, k1=-0.19227955160000001, tilt=0.0, eid='QE.2625.T3')
qe_2646_t3 = Quadrupole(l=0.24, k1=0.19227955160000001, tilt=0.0, eid='QE.2646.T3')
qe_2668_t3 = Quadrupole(l=0.24, k1=-0.19227955160000001, tilt=0.0, eid='QE.2668.T3')
qe_2690_un1 = Quadrupole(l=0.24, k1=0.19227955160000001, tilt=0.0, eid='QE.2690.UN1')
qe_2712_un1 = Quadrupole(l=0.24, k1=-0.19227955160000001, tilt=0.0, eid='QE.2712.UN1')
qe_2733_un1 = Quadrupole(l=0.24, k1=0.19227955160000001, tilt=0.0, eid='QE.2733.UN1')

# bending magnets 
be_2546_t3 = SBend(l = 2.5, angle=0.0218803, e1=0.01094015, e2=0.01094015, gap=0, tilt=0.0, fint=0.0, fintx=0.0, eid='BE.2546.T3')
be_2566_t3 = SBend(l = 2.5, angle=0.0218803, e1=0.01094015, e2=0.01094015, gap=0, tilt=0.0, fint=0.0, fintx=0.0, eid='BE.2566.T3')

# correctors 
cex_2430_t3 = Hcor(l=0.1, angle=0.0, eid='CEX.2430.T3')
cey_2443_t3 = Vcor(l=0.1, angle=0.0, eid='CEY.2443.T3')
cex_2455_t3 = Hcor(l=0.1, angle=0.0, eid='CEX.2455.T3')
cey_2468_t3 = Vcor(l=0.1, angle=0.0, eid='CEY.2468.T3')
cex_2488_t3 = Hcor(l=0.1, angle=0.0, eid='CEX.2488.T3')
cey_2509_t3 = Vcor(l=0.1, angle=0.0, eid='CEY.2509.T3')
chx_2530_t3 = Hcor(l=0.2, angle=0.0, eid='CHX.2530.T3')
chy_2533_t3 = Vcor(l=0.2, angle=0.0, eid='CHY.2533.T3')
chx_2542_t3 = Hcor(l=0.2, angle=0.0, eid='CHX.2542.T3')
chy_2543_t3 = Vcor(l=0.2, angle=0.0, eid='CHY.2543.T3')
chx_2554_t3 = Hcor(l=0.2, angle=0.0, eid='CHX.2554.T3')
chy_2559_t3 = Vcor(l=0.2, angle=0.0, eid='CHY.2559.T3')
chx_2562_t3 = Hcor(l=0.2, angle=0.0, eid='CHX.2562.T3')
chy_2569_t3 = Vcor(l=0.2, angle=0.0, eid='CHY.2569.T3')
chx_2581_t3 = Hcor(l=0.2, angle=0.0, eid='CHX.2581.T3')
chy_2584_t3 = Vcor(l=0.2, angle=0.0, eid='CHY.2584.T3')
cex_2603_t3 = Hcor(l=0.1, angle=0.0, eid='CEX.2603.T3')
cey_2625_t3 = Vcor(l=0.1, angle=0.0, eid='CEY.2625.T3')
cex_2647_t3 = Hcor(l=0.1, angle=0.0, eid='CEX.2647.T3')
cey_2668_t3 = Vcor(l=0.1, angle=0.0, eid='CEY.2668.T3')
cex_2690_un1 = Hcor(l=0.1, angle=0.0, eid='CEX.2690.UN1')
cey_2712_un1 = Vcor(l=0.1, angle=0.0, eid='CEY.2712.UN1')
cex_2734_un1 = Hcor(l=0.1, angle=0.0, eid='CEX.2734.UN1')

# markers 
stsec_2423_t3 = Marker(eid='STSEC.2423.T3')
stsub_2423_t3 = Marker(eid='STSUB.2423.T3')
tora_2424_t3 = Marker(eid='TORA.2424.T3')
ensub_2544_t3 = Marker(eid='ENSUB.2544.T3')
stsub_2544_t3 = Marker(eid='STSUB.2544.T3')
tora_2682_t3 = Marker(eid='TORA.2682.T3')
ensec_2682_t3 = Marker(eid='ENSEC.2682.T3')
stsec_2682_un1 = Marker(eid='STSEC.2682.UN1')
ensec_2743_un1 = Marker(eid='ENSEC.2743.UN1')
stsec_2743_t5 = Marker(eid='STSEC.2743.T5')

# monitor 
bpma_2430_t3 = Monitor(eid='BPMA.2430.T3')
bpma_2442_t3 = Monitor(eid='BPMA.2442.T3')
bpma_2455_t3 = Monitor(eid='BPMA.2455.T3')
bpma_2467_t3 = Monitor(eid='BPMA.2467.T3')
bpma_2487_t3 = Monitor(eid='BPMA.2487.T3')
bpma_2509_t3 = Monitor(eid='BPMA.2509.T3')
bpma_2528_t3 = Monitor(eid='BPMA.2528.T3')
bpma_2531_t3 = Monitor(eid='BPMA.2531.T3')
bpma_2543_t3 = Monitor(eid='BPMA.2543.T3')
bpma_2553_t3 = Monitor(eid='BPMA.2553.T3')
bpma_2558_t3 = Monitor(eid='BPMA.2558.T3')
bpma_2563_t3 = Monitor(eid='BPMA.2563.T3')
bpma_2568_t3 = Monitor(eid='BPMA.2568.T3')
bpma_2579_t3 = Monitor(eid='BPMA.2579.T3')
bpma_2582_t3 = Monitor(eid='BPMA.2582.T3')
bpma_2603_t3 = Monitor(eid='BPMA.2603.T3')
bpma_2624_t3 = Monitor(eid='BPMA.2624.T3')
bpma_2646_t3 = Monitor(eid='BPMA.2646.T3')
bpma_2668_t3 = Monitor(eid='BPMA.2668.T3')
bpma_2690_un1 = Monitor(eid='BPMA.2690.UN1')
bpma_2711_un1 = Monitor(eid='BPMA.2711.UN1')
bpma_2733_un1 = Monitor(eid='BPMA.2733.UN1')

# sextupoles 
saox_2555_t3 = Sextupole(l=0.3164, k2=12.57269279, tilt=0.0, eid='SAOX.2555.T3')
sao_2561_t3 = Sextupole(l=0.3164, k2=4.465865992000632, tilt=0.0, eid='SAO.2561.T3')

# octupole 

# undulator 

# cavity 

# UnknowElement 

# Matrices 

# Solenoids 

# lattice 
cell = (stsec_2423_t3, stsub_2423_t3, d_2, tora_2424_t3, d_3, bpma_2430_t3,
d_4, qe_2430_t3, d_5, cex_2430_t3, d_6, bpma_2442_t3, d_4, qe_2443_t3, 
d_5, cey_2443_t3, d_6, bpma_2455_t3, d_4, qe_2455_t3, d_5, cex_2455_t3, 
d_6, bpma_2467_t3, d_4, qe_2468_t3, d_5, cey_2468_t3, d_15, bpma_2487_t3, 
d_4, qe_2487_t3, d_5, cex_2488_t3, d_18, bpma_2509_t3, d_4, qe_2509_t3, 
d_5, cey_2509_t3, d_21, bpma_2528_t3, d_22, qh_2529_t3, d_23, chx_2530_t3, 
d_24, bpma_2531_t3, d_22, qh_2532_t3, d_23, chy_2533_t3, d_27, chx_2542_t3, 
d_28, chy_2543_t3, d_29, bpma_2543_t3, d_30, qh_2544_t3, d_31, ensub_2544_t3, 
stsub_2544_t3, d_32, be_2546_t3, d_33, qm_2549_t3, d_34, bpma_2553_t3, d_35, 
qm_2554_t3, d_36, chx_2554_t3, d_37, saox_2555_t3, d_38, bpma_2558_t3, d_35, 
qm_2559_t3, d_36, chy_2559_t3, d_41, sao_2561_t3, d_42, chx_2562_t3, d_43, 
bpma_2563_t3, d_35, qm_2564_t3, d_45, be_2566_t3, d_46, bpma_2568_t3, d_22, 
qh_2569_t3, d_23, chy_2569_t3, d_49, bpma_2579_t3, d_22, qh_2580_t3, d_23, 
chx_2581_t3, d_24, bpma_2582_t3, d_22, qh_2583_t3, d_23, chy_2584_t3, d_55, 
bpma_2603_t3, d_4, qe_2603_t3, d_5, cex_2603_t3, d_18, bpma_2624_t3, d_4, 
qe_2625_t3, d_5, cey_2625_t3, d_18, bpma_2646_t3, d_4, qe_2646_t3, d_5, 
cex_2647_t3, d_18, bpma_2668_t3, d_4, qe_2668_t3, d_5, cey_2668_t3, d_67, 
tora_2682_t3, d_68, ensec_2682_t3, stsec_2682_un1, d_69, bpma_2690_un1, d_4, qe_2690_un1, 
d_5, cex_2690_un1, d_18, bpma_2711_un1, d_4, qe_2712_un1, d_5, cey_2712_un1, 
d_18, bpma_2733_un1, d_4, qe_2733_un1, d_5, cex_2734_un1, d_78, ensec_2743_un1, 
stsec_2743_t5)
# power supplies 

#  
qe_2430_t3.ps_id = 'QE.3.T3'
qe_2443_t3.ps_id = 'QE.4.T3'
qe_2455_t3.ps_id = 'QE.5.T3'
qe_2468_t3.ps_id = 'QE.6.T3'
qe_2487_t3.ps_id = 'QE.1.T3'
qe_2509_t3.ps_id = 'QE.2.T3'
qh_2529_t3.ps_id = 'QH.3.T3'
qh_2532_t3.ps_id = 'QH.4.T3'
qh_2544_t3.ps_id = 'QH.1.T3'
qm_2549_t3.ps_id = 'QM.2.T3'
qm_2554_t3.ps_id = 'QM.1.T3'
qm_2559_t3.ps_id = 'QM.2.T3'
qm_2564_t3.ps_id = 'QM.1.T3'
qh_2569_t3.ps_id = 'QH.2.T3'
qh_2580_t3.ps_id = 'QH.3.T3'
qh_2583_t3.ps_id = 'QH.4.T3'
qe_2603_t3.ps_id = 'QE.1.T3'
qe_2625_t3.ps_id = 'QE.2.T3'
qe_2646_t3.ps_id = 'QE.1.T3'
qe_2668_t3.ps_id = 'QE.2.T3'
qe_2690_un1.ps_id = 'QE.1.UN1'
qe_2712_un1.ps_id = 'QE.2.UN1'
qe_2733_un1.ps_id = 'QE.1.UN1'

#  
saox_2555_t3.ps_id = 'SAOX.1.T3'
sao_2561_t3.ps_id = 'SAO.2.T3'

#  

#  

#  
be_2546_t3.ps_id = 'BE.1.T3'
be_2566_t3.ps_id = 'BE.1.T3'
