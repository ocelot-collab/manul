from ocelot import *
# drifts
d1_1 = Drift(l=206.100754, eid='D_1')
d1_2 = Drift(l=0.254587, eid='D_2')
d1_3 = Drift(l=1.319557, eid='D_3')
d1_4 = Drift(l=0.15065, eid='D_4')
d1_5 = Drift(l=0.13165, eid='D_5')
d1_6 = Drift(l=1.23165, eid='D_6')
d1_7 = Drift(l=0.68965, eid='D_7')
d1_8 = Drift(l=0.181, eid='D_8')
d1_9 = Drift(l=2.584, eid='D_9')
d1_10 = Drift(l=0.1483, eid='D_10')
d1_11 = Drift(l=0.1543, eid='D_11')
d1_12 = Drift(l=0.4253, eid='D_12')
d1_13 = Drift(l=0.724, eid='D_13')

# quadrupoles
qd_231_b1d = Quadrupole(l=0.2367, k1=-3.0, tilt=0.0, eid='QD.231.B1D')
qd_232_b1d = Quadrupole(l=0.2367, k1=0.0, tilt=0.0, eid='QD.232.B1D')

# bending magnets
bb_229_b1d = SBend(l = 0.5, angle=0.2094395102, e1=0.0, e2=0.20943951, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BB.229.B1D')

# correctors
ccy_231_b1d = Vcor(l=0.1, angle=0.0, eid='CCY.231.B1D')
ccx_233_b1d = Hcor(l=0.1, angle=0.0, eid='CCX.233.B1D')

# markers
stsec_229_b1d = Marker(eid='STSEC.229.B1D')
otrc_236_b1d = Marker(eid='OTRC.236.B1D')
tora_236_b1d = Marker(eid='TORA.236.B1D')
duflange_237_b1d = Marker(eid='DUFLANGE.237.B1D')
duabsorb_237_b1d = Marker(eid='DUABSORB.237.B1D')
ensec_237_b1d = Marker(eid='ENSEC.237.B1D')

# monitor
bpma_231_b1d = Monitor(eid='BPMA.231.B1D')
bpma_233_b1d = Monitor(eid='BPMA.233.B1D')
bpma_236_b1d = Monitor(eid='BPMA.236.B1D')


cell = (stsec_229_b1d, d1_2, bb_229_b1d, d1_3, bpma_231_b1d, d1_4,
qd_231_b1d, d1_5, ccy_231_b1d, d1_6, qd_232_b1d, d1_7, bpma_233_b1d, d1_8,
ccx_233_b1d, d1_9, otrc_236_b1d, d1_10, tora_236_b1d, d1_11, bpma_236_b1d, d1_12,
duflange_237_b1d, d1_13, duabsorb_237_b1d, ensec_237_b1d)
# power supplies

qd_231_b1d.ps_id = 'QD.25.B1D'
qd_232_b1d.ps_id = 'QD.26.B1D'

bb_229_b1d.ps_id = 'BB.1.B1D'