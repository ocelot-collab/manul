from ocelot import * 

# drifts 
d_1 = Drift(l=1.3805, eid='D_1')
d_2 = Drift(l=4.4067, eid='D_2')
d_3 = Drift(l=0.15395, eid='D_3')
d_4 = Drift(l=14.40535, eid='D_4')
d_5 = Drift(l=0.20895, eid='D_5')
d_7 = Drift(l=11.205, eid='D_7')
d_10 = Drift(l=83.305, eid='D_10')
d_13 = Drift(l=5.36, eid='D_13')
d_15 = Drift(l=0.26395, eid='D_15')
d_16 = Drift(l=0.096, eid='D_16')
d_17 = Drift(l=0.1108, eid='D_17')
d_18 = Drift(l=0.53894, eid='D_18')
d_19 = Drift(l=9.9e-05, eid='D_19')
d_20 = Drift(l=0.500198, eid='D_20')
d_21 = Drift(l=1.930099, eid='D_21')
d_22 = Drift(l=0.1424, eid='D_22')
d_23 = Drift(l=0.1974, eid='D_23')
d_24 = Drift(l=0.5535, eid='D_24')
d_25 = Drift(l=0.9035, eid='D_25')
d_26 = Drift(l=0.8535, eid='D_26')
d_31 = Drift(l=0.500199, eid='D_31')
d_32 = Drift(l=0.611799, eid='D_32')
d_33 = Drift(l=0.1607, eid='D_33')
d_34 = Drift(l=0.3448, eid='D_34')
d_37 = Drift(l=0.2144, eid='D_37')
d_38 = Drift(l=0.558, eid='D_38')
d_39 = Drift(l=0.5, eid='D_39')
d_40 = Drift(l=0.822, eid='D_40')
d_41 = Drift(l=0.2, eid='D_41')
d_42 = Drift(l=0.45, eid='D_42')
d_43 = Drift(l=0.313, eid='D_43')
d_44 = Drift(l=3.87, eid='D_44')
d_45 = Drift(l=0.3223, eid='D_45')
d_46 = Drift(l=0.8578, eid='D_46')
d_47 = Drift(l=1.07324, eid='D_47')
d_48 = Drift(l=2.0144, eid='D_48')

# quadrupoles 
qf_2946_t4d = Quadrupole(l=0.5321, k1=0.0686747244, tilt=0.0, eid='QF.2946.T4D')
qf_2962_t4d = Quadrupole(l=0.5321, k1=-0.1424602565, tilt=0.0, eid='QF.2962.T4D')
qf_2974_t4d = Quadrupole(l=0.5321, k1=0.1381313234, tilt=0.0, eid='QF.2974.T4D')
qf_3058_t4d = Quadrupole(l=0.5321, k1=0.1523752421, tilt=0.0, eid='QF.3058.T4D')
qf_3065_t4d = Quadrupole(l=0.5321, k1=-0.076732752, tilt=0.0, eid='QF.3065.T4D')
qk_3074_t4d = Quadrupole(l=1.0552, k1=-0.1729944303, tilt=0.0, eid='QK.3074.T4D')
qk_3079_t4d = Quadrupole(l=1.0552, k1=-0.1729944303, tilt=0.0, eid='QK.3079.T4D')
qk_3089_t4d = Quadrupole(l=1.0552, k1=-0.1699986517, tilt=0.0, eid='QK.3089.T4D')
qk_3090_t4d = Quadrupole(l=1.0552, k1=-0.1699986517, tilt=0.0, eid='QK.3090.T4D')
qk_3092_t4d = Quadrupole(l=1.0552, k1=-0.1699986517, tilt=0.0, eid='QK.3092.T4D')
qk_3093_t4d = Quadrupole(l=1.0552, k1=-0.1699986517, tilt=0.0, eid='QK.3093.T4D')

# bending magnets 
bv_3067_t4d = SBend(l = 2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BV.3067.T4D')
bv_3070_t4d = SBend(l = 2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BV.3070.T4D')
bv_3083_t4d = SBend(l = 2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BV.3083.T4D')
bv_3086_t4d = SBend(l = 2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BV.3086.T4D')
sweep_3095_t4d = RBend(l = 0.64, angle=0.0, e1=0.0, e2=0.0, gap=0, tilt=-1.570796327, fint=0.0, fintx=0.0, eid='SWEEP.3095.T4D')
sweep_3096_t4d = RBend(l = 0.64, angle=0.0, e1=0.0, e2=0.0, gap=0, tilt=0, fint=0.0, fintx=0.0, eid='SWEEP.3096.T4D')

# correctors 
cfx_2947_t4d = Hcor(l=0.1, angle=0.0, eid='CFX.2947.T4D')
cfy_2962_t4d = Vcor(l=0.1, angle=0.0, eid='CFY.2962.T4D')
cfx_2975_t4d = Hcor(l=0.1, angle=0.0, eid='CFX.2975.T4D')
cfx_3059_t4d = Hcor(l=0.1, angle=0.0, eid='CFX.3059.T4D')
cfy_3064_t4d = Vcor(l=0.1, angle=0.0, eid='CFY.3064.T4D')
cnx_3074_t4d = Hcor(l=0.3, angle=0.0, eid='CNX.3074.T4D')
cny_3080_t4d = Vcor(l=0.3, angle=0.0, eid='CNY.3080.T4D')

# markers 
stsec_2940_t4d = Marker(eid='STSEC.2940.T4D')
stsub_2940_t4d = Marker(eid='STSUB.2940.T4D')
tora_2942_t4d = Marker(eid='TORA.2942.T4D')
mpbpmf_3065_t4d = Marker(eid='MPBPMF.3065.T4D')
tora_3065_t4d = Marker(eid='TORA.3065.T4D')
ensub_3066_t4d = Marker(eid='ENSUB.3066.T4D')
stsub_3066_t4d = Marker(eid='STSUB.3066.T4D')
otrd_3077_t4d = Marker(eid='OTRD.3077.T4D')
otrd_3097_t4d = Marker(eid='OTRD.3097.T4D')
torc_3098_t4d = Marker(eid='TORC.3098.T4D')
bhm_3098_t4d = Marker(eid='BHM.3098.T4D')
scrw_3102_t4d = Marker(eid='SCRW.3102.T4D')
duwindow_3102_t4d = Marker(eid='DUWINDOW.3102.T4D')
duflange_3103_t4d = Marker(eid='DUFLANGE.3103.T4D')
duconcrete_3104_t4d = Marker(eid='DUCONCRETE.3104.T4D')
duabsorb_3106_t4d = Marker(eid='DUABSORB.3106.T4D')
ensub_3106_t4d = Marker(eid='ENSUB.3106.T4D')
ensec_3106_t4d = Marker(eid='ENSEC.3106.T4D')

# monitor 
bpma_2961_t4d = Monitor(eid='BPMA.2961.T4D')
bpma_2974_t4d = Monitor(eid='BPMA.2974.T4D')
bpma_3058_t4d = Monitor(eid='BPMA.3058.T4D')
bpmf_3065_t4d = Monitor(eid='BPMF.3065.T4D')
bpmd_3075_t4d = Monitor(eid='BPMD.3075.T4D')
bpmd_3079_t4d = Monitor(eid='BPMD.3079.T4D')
bpmd_3088_t4d = Monitor(eid='BPMD.3088.T4D')
bpmd_3094_t4d = Monitor(eid='BPMD.3094.T4D')
bpmd_3097_t4d = Monitor(eid='BPMD.3097.T4D')
bpmw_3102_t4d = Monitor(eid='BPMW.3102.T4D')

# sextupoles 
sk_3076_t4d = Sextupole(l=0.343, k2=2.020228531, tilt=1.570796327, eid='SK.3076.T4D')
sk_3078_t4d = Sextupole(l=0.343, k2=2.020228531, tilt=1.570796327, eid='SK.3078.T4D')

# octupole 

# undulator 

# cavity 

# UnknowElement 

# Matrices 

# Solenoids 

# lattice 
cell = (stsec_2940_t4d, stsub_2940_t4d, d_1, tora_2942_t4d, d_2, qf_2946_t4d, d_3, 
cfx_2947_t4d, d_4, bpma_2961_t4d, d_5, qf_2962_t4d, d_3, cfy_2962_t4d, d_7, 
bpma_2974_t4d, d_5, qf_2974_t4d, d_3, cfx_2975_t4d, d_10, bpma_3058_t4d, d_5, 
qf_3058_t4d, d_3, cfx_3059_t4d, d_13, cfy_3064_t4d, d_3, qf_3065_t4d, d_15, 
bpmf_3065_t4d, d_16, mpbpmf_3065_t4d, d_17, tora_3065_t4d, d_18, ensub_3066_t4d, stsub_3066_t4d, 
d_19, bv_3067_t4d, d_20, bv_3070_t4d, d_21, cnx_3074_t4d, d_22, qk_3074_t4d, 
d_23, bpmd_3075_t4d, d_24, sk_3076_t4d, d_25, otrd_3077_t4d, d_26, sk_3078_t4d, 
d_24, bpmd_3079_t4d, d_23, qk_3079_t4d, d_22, cny_3080_t4d, d_21, bv_3083_t4d, 
d_31, bv_3086_t4d, d_32, bpmd_3088_t4d, d_33, qk_3089_t4d, d_34, qk_3090_t4d, 
d_34, qk_3092_t4d, d_34, qk_3093_t4d, d_37, bpmd_3094_t4d, d_38, sweep_3095_t4d, 
d_39, sweep_3096_t4d, d_40, bpmd_3097_t4d, d_41, otrd_3097_t4d, d_42, torc_3098_t4d, 
d_43, bhm_3098_t4d, d_44, bpmw_3102_t4d, d_45, scrw_3102_t4d, duwindow_3102_t4d, d_46, 
duflange_3103_t4d, d_47, duconcrete_3104_t4d, d_48, duabsorb_3106_t4d, ensub_3106_t4d, ensec_3106_t4d)
# power supplies 

#  
qf_2946_t4d.ps_id = 'QF.1.T4D'
qf_2962_t4d.ps_id = 'QF.2.T4D'
qf_2974_t4d.ps_id = 'QF.3.T4D'
qf_3058_t4d.ps_id = 'QF.4.T4D'
qf_3065_t4d.ps_id = 'QF.5.T4D'
qk_3074_t4d.ps_id = 'QK.1.T4D'
qk_3079_t4d.ps_id = 'QK.1.T4D'
qk_3089_t4d.ps_id = 'QK.6.T4D'
qk_3090_t4d.ps_id = 'QK.6.T4D'
qk_3092_t4d.ps_id = 'QK.6.T4D'
qk_3093_t4d.ps_id = 'QK.6.T4D'

#  
sk_3076_t4d.ps_id = 'SK.1.T4D'
sk_3078_t4d.ps_id = 'SK.1.T4D'

#  

#  

#  
bv_3067_t4d.ps_id = 'BV.1.T4D'
bv_3070_t4d.ps_id = 'BV.1.T4D'
bv_3083_t4d.ps_id = 'BV.1.T4D'
bv_3086_t4d.ps_id = 'BV.1.T4D'
sweep_3095_t4d.ps_id = 'SWEEP.1.T4D'
sweep_3096_t4d.ps_id = 'SWEEP.2.T4D'
