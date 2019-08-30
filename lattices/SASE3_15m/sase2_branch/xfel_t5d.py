from ocelot import * 

# drifts 
d_2 = Drift(l=1.0, eid='D_2')
d_3 = Drift(l=12.4714, eid='D_3')
d_4 = Drift(l=15.515, eid='D_4')
d_5 = Drift(l=0.20895, eid='D_5')
d_6 = Drift(l=0.15395, eid='D_6')
d_7 = Drift(l=11.205, eid='D_7')
d_10 = Drift(l=60.205, eid='D_10')
d_13 = Drift(l=5.36, eid='D_13')
d_15 = Drift(l=0.26395, eid='D_15')
d_16 = Drift(l=0.096, eid='D_16')
d_17 = Drift(l=0.1108, eid='D_17')
d_18 = Drift(l=0.515822, eid='D_18')
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
qe_3052_t5d = Quadrupole(l=0.24, k1=0.17809234820000003, tilt=0.0, eid='QE.3052.T5D')
qf_3068_t5d = Quadrupole(l=0.5321, k1=-0.17605704040030068, tilt=0.0, eid='QF.3068.T5D')
qf_3081_t5d = Quadrupole(l=0.5321, k1=0.04029504314038714, tilt=0.0, eid='QF.3081.T5D')
qf_3142_t5d = Quadrupole(l=0.5321, k1=0.15224861069911672, tilt=0.0, eid='QF.3142.T5D')
qf_3148_t5d = Quadrupole(l=0.5321, k1=-0.08140032835933093, tilt=0.0, eid='QF.3148.T5D')
qk_3158_t5d = Quadrupole(l=1.0552, k1=-0.172994430300417, tilt=0.0, eid='QK.3158.T5D')
qk_3163_t5d = Quadrupole(l=1.0552, k1=-0.172994430300417, tilt=0.0, eid='QK.3163.T5D')
qk_3172_t5d = Quadrupole(l=1.0552, k1=-0.18509466829984839, tilt=0.0, eid='QK.3172.T5D')
qk_3174_t5d = Quadrupole(l=1.0552, k1=-0.18509466829984839, tilt=0.0, eid='QK.3174.T5D')
qk_3175_t5d = Quadrupole(l=1.0552, k1=-0.18509466829984839, tilt=0.0, eid='QK.3175.T5D')
qk_3177_t5d = Quadrupole(l=1.0552, k1=-0.18509466829984839, tilt=0.0, eid='QK.3177.T5D')

# bending magnets 
bv_3151_t5d = SBend(l = 2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BV.3151.T5D')
bv_3154_t5d = SBend(l = 2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BV.3154.T5D')
bv_3167_t5d = SBend(l = 2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BV.3167.T5D')
bv_3170_t5d = SBend(l = 2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BV.3170.T5D')
sweep_3178_t5d = RBend(l = 0.64, angle=0.0, e1=0.0, e2=0.0, gap=0, tilt=-1.570796327, fint=0.0, fintx=0.0, eid='SWEEP.3178.T5D')
sweep_3179_t5d = RBend(l = 0.64, angle=0.0, e1=0.0, e2=0.0, gap=0, tilt=0, fint=0.0, fintx=0.0, eid='SWEEP.3179.T5D')

# correctors 
cfy_3069_t5d = Vcor(l=0.1, angle=0.0, eid='CFY.3069.T5D')
cfx_3081_t5d = Hcor(l=0.1, angle=0.0, eid='CFX.3081.T5D')
cfx_3142_t5d = Hcor(l=0.1, angle=0.0, eid='CFX.3142.T5D')
cfy_3148_t5d = Vcor(l=0.1, angle=0.0, eid='CFY.3148.T5D')
cnx_3157_t5d = Hcor(l=0.3, angle=0.0, eid='CNX.3157.T5D')
cny_3164_t5d = Vcor(l=0.3, angle=0.0, eid='CNY.3164.T5D')

# markers 
stsec_3039_t5d = Marker(eid='STSEC.3039.T5D')
stsub_3039_t5d = Marker(eid='STSUB.3039.T5D')
tora_3040_t5d = Marker(eid='TORA.3040.T5D')
mpbpmf_3149_t5d = Marker(eid='MPBPMF.3149.T5D')
tora_3149_t5d = Marker(eid='TORA.3149.T5D')
ensub_3149_t5d = Marker(eid='ENSUB.3149.T5D')
stsub_3149_t5d = Marker(eid='STSUB.3149.T5D')
otrd_3160_t5d = Marker(eid='OTRD.3160.T5D')
otrd_3181_t5d = Marker(eid='OTRD.3181.T5D')
torc_3181_t5d = Marker(eid='TORC.3181.T5D')
bhm_3181_t5d = Marker(eid='BHM.3181.T5D')
scrw_3186_t5d = Marker(eid='SCRW.3186.T5D')
duwindow_3186_t5d = Marker(eid='DUWINDOW.3186.T5D')
duflange_3186_t5d = Marker(eid='DUFLANGE.3186.T5D')
duconcrete_3187_t5d = Marker(eid='DUCONCRETE.3187.T5D')
duabsorb_3189_t5d = Marker(eid='DUABSORB.3189.T5D')
ensec_3189_t5d = Marker(eid='ENSEC.3189.T5D')

# monitor 
bpma_3068_t5d = Monitor(eid='BPMA.3068.T5D')
bpma_3080_t5d = Monitor(eid='BPMA.3080.T5D')
bpma_3141_t5d = Monitor(eid='BPMA.3141.T5D')
bpmf_3149_t5d = Monitor(eid='BPMF.3149.T5D')
bpmd_3159_t5d = Monitor(eid='BPMD.3159.T5D')
bpmd_3162_t5d = Monitor(eid='BPMD.3162.T5D')
bpmd_3172_t5d = Monitor(eid='BPMD.3172.T5D')
bpmd_3177_t5d = Monitor(eid='BPMD.3177.T5D')
bpmd_3180_t5d = Monitor(eid='BPMD.3180.T5D')
bpmw_3185_t5d = Monitor(eid='BPMW.3185.T5D')

# sextupoles 
sk_3159_t5d = Sextupole(l=0.343, k2=2.020228531, tilt=1.570796327, eid='SK.3159.T5D')
sk_3161_t5d = Sextupole(l=0.343, k2=2.020228531, tilt=1.570796327, eid='SK.3161.T5D')

# octupole 

# undulator 

# cavity 

# UnknowElement 

# Matrices 

# Solenoids 

# lattice 
cell = ( stsec_3039_t5d, stsub_3039_t5d, d_2, tora_3040_t5d, d_3, qe_3052_t5d,
d_4, bpma_3068_t5d, d_5, qf_3068_t5d, d_6, cfy_3069_t5d, d_7, bpma_3080_t5d, 
d_5, qf_3081_t5d, d_6, cfx_3081_t5d, d_10, bpma_3141_t5d, d_5, qf_3142_t5d, 
d_6, cfx_3142_t5d, d_13, cfy_3148_t5d, d_6, qf_3148_t5d, d_15, bpmf_3149_t5d, 
d_16, mpbpmf_3149_t5d, d_17, tora_3149_t5d, d_18, ensub_3149_t5d, stsub_3149_t5d, d_19, 
bv_3151_t5d, d_20, bv_3154_t5d, d_21, cnx_3157_t5d, d_22, qk_3158_t5d, d_23, 
bpmd_3159_t5d, d_24, sk_3159_t5d, d_25, otrd_3160_t5d, d_26, sk_3161_t5d, d_24, 
bpmd_3162_t5d, d_23, qk_3163_t5d, d_22, cny_3164_t5d, d_21, bv_3167_t5d, d_31, 
bv_3170_t5d, d_32, bpmd_3172_t5d, d_33, qk_3172_t5d, d_34, qk_3174_t5d, d_34, 
qk_3175_t5d, d_34, qk_3177_t5d, d_37, bpmd_3177_t5d, d_38, sweep_3178_t5d, d_39, 
sweep_3179_t5d, d_40, bpmd_3180_t5d, d_41, otrd_3181_t5d, d_42, torc_3181_t5d, d_43, 
bhm_3181_t5d, d_44, bpmw_3185_t5d, d_45, scrw_3186_t5d, duwindow_3186_t5d, d_46, duflange_3186_t5d, 
d_47, duconcrete_3187_t5d, d_48, duabsorb_3189_t5d, ensec_3189_t5d)
# power supplies 

#  
qe_3052_t5d.ps_id = 'QE.1.T5D'
qf_3068_t5d.ps_id = 'QF.1.T5D'
qf_3081_t5d.ps_id = 'QF.2.T5D'
qf_3142_t5d.ps_id = 'QF.3.T5D'
qf_3148_t5d.ps_id = 'QF.4.T5D'
qk_3158_t5d.ps_id = 'QK.1.T5D'
qk_3163_t5d.ps_id = 'QK.1.T5D'
qk_3172_t5d.ps_id = 'QK.6.T5D'
qk_3174_t5d.ps_id = 'QK.6.T5D'
qk_3175_t5d.ps_id = 'QK.6.T5D'
qk_3177_t5d.ps_id = 'QK.6.T5D'

#  
sk_3159_t5d.ps_id = 'SK.1.T5D'
sk_3161_t5d.ps_id = 'SK.1.T5D'

#  

#  

#  
bv_3151_t5d.ps_id = 'BV.1.T5D'
bv_3154_t5d.ps_id = 'BV.1.T5D'
bv_3167_t5d.ps_id = 'BV.1.T5D'
bv_3170_t5d.ps_id = 'BV.1.T5D'
sweep_3178_t5d.ps_id = 'SWEEP.1.T5D'
sweep_3179_t5d.ps_id = 'SWEEP.2.T5D'
