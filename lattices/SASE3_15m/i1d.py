
from ocelot import *

# drifts
di_2 = Drift(l=0.002879, eid='D_2')
di_3 = Drift(l=0.969029, eid='D_3')
di_4 = Drift(l=0.15615, eid='D_4')
di_5 = Drift(l=0.406, eid='D_5')
di_6 = Drift(l=0.15015, eid='D_6')
di_7 = Drift(l=0.24921, eid='D_7')
di_8 = Drift(l=0.225, eid='D_8')
di_9 = Drift(l=0.125, eid='D_9')
di_10 = Drift(l=0.28523, eid='D_10')
di_11 = Drift(l=0.252, eid='D_11')
di_12 = Drift(l=1.696, eid='D_12')
di_13 = Drift(l=0.098, eid='D_13')

# quadrupoles
qi_63_i1d = Quadrupole(l=0.2377, k1=4.401795, tilt=0.0, eid='QI.63.I1D')
qi_64_i1d = Quadrupole(l=0.2377, k1=0.0, tilt=0.0, eid='QI.64.I1D')

# bending magnets
bb_62_i1d = SBend(l = 0.5, angle=0.5235987756, e1=0.261799388, e2=0.261799388, gap=0, tilt=0.0, fint=0.0, fintx=0.0, eid='BB.62.I1D')

# correctors

# markers
stsec_62_i1d = Marker(eid='STSEC.62.I1D')
otrc_64_i1d = Marker(eid='OTRC.64.I1D')
otrd_64_i1d = Marker(eid='OTRD.64.I1D')
torc_64_i1d = Marker(eid='TORC.64.I1D')
duflange_65_i1d = Marker(eid='DUFLANGE.65.I1D')
duconcrete_65_i1d = Marker(eid='DUCONCRETE.65.I1D')
bhm_66_i1d = Marker(eid='BHM.66.I1D')
duabsorb_66_i1d = Marker(eid='DUABSORB.66.I1D')
ensec_66_i1d = Marker(eid='ENSEC.66.I1D')

# monitor
bpma_63_i1d = Monitor(eid='BPMA.63.I1D')
bpmd_64_i1d = Monitor(eid='BPMD.64.I1D')

# lattice
cell = (stsec_62_i1d, di_2, bb_62_i1d, di_3, qi_63_i1d, di_4,
bpma_63_i1d, di_5, otrc_64_i1d, di_6, qi_64_i1d, di_7, otrd_64_i1d, di_8,
torc_64_i1d, di_9, bpmd_64_i1d, di_10, duflange_65_i1d, di_11, duconcrete_65_i1d, di_12,
bhm_66_i1d, di_13, duabsorb_66_i1d, ensec_66_i1d)
# power supplies

#
qi_63_i1d.ps_id = 'QI.41.I1D'
qi_64_i1d.ps_id = 'QI.42.I1D'

bb_62_i1d.ps_id = 'BB.5.I1D'