from ocelot import *
# drifts

d2_2 = Drift(l=0.00145, eid='D_2')
d2_3 = Drift(l=0.58145, eid='D_3')
d2_4 = Drift(l=0.17395, eid='D_4')
d2_5 = Drift(l=0.18395, eid='D_5')
d2_6 = Drift(l=1.04372, eid='D_6')
d2_7 = Drift(l=0.13628, eid='D_7')
d2_8 = Drift(l=0.18, eid='D_8')
d2_9 = Drift(l=0.2, eid='D_9')
d2_10 = Drift(l=0.98395, eid='D_10')
d2_11 = Drift(l=0.43628, eid='D_11')
d2_12 = Drift(l=0.41912, eid='D_12')
d2_13 = Drift(l=0.516377, eid='D_13')
d2_14 = Drift(l=0.16902, eid='D_14')
d2_15 = Drift(l=0.25898, eid='D_15')
d2_16 = Drift(l=0.2249, eid='D_16')
d2_17 = Drift(l=0.23402, eid='D_17')
d2_18 = Drift(l=0.66368, eid='D_18')
d2_19 = Drift(l=0.225, eid='D_19')
d2_20 = Drift(l=0.125, eid='D_20')
d2_21 = Drift(l=0.28527, eid='D_21')
d2_22 = Drift(l=0.728, eid='D_22')

# quadrupoles
qf_469_b2d = Quadrupole(l=0.5321, k1=-2.19942871499906, tilt=0.0, eid='QF.469.B2D')
qe_471_b2d = Quadrupole(l=0.24, k1=1.335539651, tilt=0.0, eid='QE.471.B2D')
qf_472_b2d = Quadrupole(l=0.5321, k1=-2.19942871499906, tilt=0.0, eid='QF.472.B2D')
qf_476_b2d = Quadrupole(l=0.5321, k1=3.1309789299999995, tilt=0.0, eid='QF.476.B2D')
qf_477_b2d = Quadrupole(l=0.5321, k1=0.7703645572993798, tilt=0.0, eid='QF.477.B2D')

# bending magnets
bg_467_b2d = SBend(l = 1.5971, angle=0.2094395102, e1=0.0, e2=0.0, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BG.467.B2D')
bg_474_b2d = SBend(l = 1.5971, angle=-0.2094395102, e1=0.0, e2=0.0, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BG.474.B2D')

# correctors
cfy_468_b2d = Vcor(l=0.1, angle=0.0, eid='CFY.468.B2D')
cfx_470_b2d = Hcor(l=0.1, angle=0.0, eid='CFX.470.B2D')
cfy_471_b2d = Vcor(l=0.1, angle=0.0, eid='CFY.471.B2D')
cfy_476_b2d = Vcor(l=0.1, angle=0.0, eid='CFY.476.B2D')
cfx_477_b2d = Hcor(l=0.1, angle=0.0, eid='CFX.477.B2D')

# markers
stsec_466_b2d = Marker(eid='STSEC.466.B2D')
otra_473_b2d = Marker(eid='OTRA.473.B2D')
otrd_478_b2d = Marker(eid='OTRD.478.B2D')
torc_479_b2d = Marker(eid='TORC.479.B2D')
duflange_479_b2d = Marker(eid='DUFLANGE.479.B2D')
duabsorb_480_b2d = Marker(eid='DUABSORB.480.B2D')
ensec_480_b2d = Marker(eid='ENSEC.480.B2D')

# monitor
bpma_469_b2d = Monitor(eid='BPMA.469.B2D')
bpma_471_b2d = Monitor(eid='BPMA.471.B2D')
bpma_477_b2d = Monitor(eid='BPMA.477.B2D')
bpmd_479_b2d = Monitor(eid='BPMD.479.B2D')



# lattice
cell = (stsec_466_b2d, d2_2, bg_467_b2d, d2_3, cfy_468_b2d, d2_4,
qf_469_b2d, d2_5, bpma_469_b2d, d2_6, cfx_470_b2d, d2_7, qe_471_b2d, d2_8,
bpma_471_b2d, d2_9, cfy_471_b2d, d2_10, qf_472_b2d, d2_11, otra_473_b2d, d2_12,
bg_474_b2d, d2_13, cfy_476_b2d, d2_14, qf_476_b2d, d2_15, bpma_477_b2d, d2_16,
cfx_477_b2d, d2_17, qf_477_b2d, d2_18, otrd_478_b2d, d2_19, torc_479_b2d, d2_20,
bpmd_479_b2d, d2_21, duflange_479_b2d, d2_22, duabsorb_480_b2d, ensec_480_b2d)
# power supplies

#
qf_469_b2d.ps_id = 'QF.31.B2D'
qe_471_b2d.ps_id = 'QE.32.B2D'
qf_472_b2d.ps_id = 'QF.33.B2D'
qf_476_b2d.ps_id = 'QF.34.B2D'
qf_477_b2d.ps_id = 'QF.35.B2D'

bg_467_b2d.ps_id = 'BG.1.B2D'
bg_474_b2d.ps_id = 'BG.1.B2D'
