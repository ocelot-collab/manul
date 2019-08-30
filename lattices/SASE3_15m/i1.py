from ocelot import * 
tws = Twiss()
tws.E = 0.005000000
tws.beta_x  = 55.7887190242
tws.beta_y  = 55.7887190242
tws.alpha_x = 18.185436973
tws.alpha_y = 18.185436973
# drifts 
d_1 = Drift(l=0.276, eid='D_1')
d_2 = Drift(l=0.316, eid='D_2')
d_3 = Drift(l=0.311, eid='D_3')
d_4 = Drift(l=0.047, eid='D_4')
d_5 = Drift(l=0.788, eid='D_5')
d_6 = Drift(l=0.313, eid='D_6')
d_7 = Drift(l=0.421, eid='D_7')
d_8 = Drift(l=0.8992, eid='D_8')
d_9 = Drift(l=0.3459, eid='D_9')
d_16 = Drift(l=0.2475, eid='D_16')
d_17 = Drift(l=0.0432, eid='D_17')
d_18 = Drift(l=0.085, eid='D_18')
d_19 = Drift(l=0.679, eid='D_19')
d_20 = Drift(l=0.1282, eid='D_20')
d_22 = Drift(l=0.202, eid='D_22')
d_23 = Drift(l=0.262, eid='D_23')
d_30 = Drift(l=2.4914, eid='D_30')
d_31 = Drift(l=0.33305, eid='D_31')
d_32 = Drift(l=0.30365, eid='D_32')
d_33 = Drift(l=0.33715, eid='D_33')
d_34 = Drift(l=0.132315, eid='D_34')
d_35 = Drift(l=0.100827, eid='D_35')
d_36 = Drift(l=0.188415, eid='D_36')
d_37 = Drift(l=0.27175, eid='D_37')
d_38 = Drift(l=0.164, eid='D_38')
d_40 = Drift(l=0.120165, eid='D_40')
d_41 = Drift(l=0.100828, eid='D_41')
d_43 = Drift(l=0.38964, eid='D_43')
d_44 = Drift(l=0.303, eid='D_44')
d_45 = Drift(l=0.1975, eid='D_45')
d_46 = Drift(l=0.18365, eid='D_46')
d_47 = Drift(l=0.05115, eid='D_47')
d_49 = Drift(l=0.7143, eid='D_49')
d_50 = Drift(l=0.75615, eid='D_50')
d_51 = Drift(l=0.175, eid='D_51')
d_52 = Drift(l=0.15, eid='D_52')
d_53 = Drift(l=0.13115, eid='D_53')
d_59 = Drift(l=0.275, eid='D_59')
d_60 = Drift(l=0.18115, eid='D_60')
d_61 = Drift(l=0.20115, eid='D_61')
d_62 = Drift(l=0.38, eid='D_62')
d_63 = Drift(l=0.28115, eid='D_63')
d_64 = Drift(l=0.26285, eid='D_64')
d_65 = Drift(l=0.74945, eid='D_65')
d_66 = Drift(l=0.53115, eid='D_66')

# quadrupoles 
q_37_i1 = Quadrupole(l=0.2136, k1=-1.114451709, tilt=0.0, eid='Q.37.I1')
q_38_i1 = Quadrupole(l=0.2136, k1=1.253402109, tilt=0.0, eid='Q.38.I1')
qi_46_i1 = Quadrupole(l=0.2377, k1=0.0801434791, tilt=0.0, eid='QI.46.I1')
qi_47_i1 = Quadrupole(l=0.2377, k1=0.3761428846, tilt=0.0, eid='QI.47.I1')
qi_50_i1 = Quadrupole(l=0.2377, k1=-0.8646623294, tilt=0.0, eid='QI.50.I1')
qi_52_i1 = Quadrupole(l=0.2377, k1=-0.352207614, tilt=0.0, eid='QI.52.I1')
qi_53_i1 = Quadrupole(l=0.2377, k1=2.104794186, tilt=0.0, eid='QI.53.I1')
qi_54_i1 = Quadrupole(l=0.2377, k1=0.7943661063, tilt=0.0, eid='QI.54.I1')
qi_55_i1 = Quadrupole(l=0.2377, k1=-3.526311, tilt=0.0, eid='QI.55.I1')
qi_57_i1 = Quadrupole(l=0.2377, k1=3.526311, tilt=0.0, eid='QI.57.I1')
qi_59_i1 = Quadrupole(l=0.2377, k1=-3.526311, tilt=0.0, eid='QI.59.I1')
qi_60_i1 = Quadrupole(l=0.2377, k1=2.145682287, tilt=0.0, eid='QI.60.I1')
qi_61_i1 = Quadrupole(l=0.2377, k1=0.8685937479, tilt=0.0, eid='QI.61.I1')

# bending magnets 
bl_48i_i1 = SBend(l=0.2, angle=-0.099484, e1=0.0, e2=-0.099484, gap=0, tilt=0.0, fint=0.0, fintx=0.0, eid='BL.48I.I1')
bl_48ii_i1 = SBend(l=0.2, angle=0.099484, e1=0.099484, e2=0.0, gap=0, tilt=0.0, fint=0.0, fintx=0.0, eid='BL.48II.I1')
bl_50i_i1 = SBend(l=0.2, angle=0.099484, e1=0.0, e2=0.099484, gap=0, tilt=0.0, fint=0.0, fintx=0.0, eid='BL.50I.I1')
bl_50ii_i1 = SBend(l=0.2, angle=-0.099484, e1=-0.099484, e2=0.0, gap=0, tilt=0.0, fint=0.0, fintx=0.0, eid='BL.50II.I1')

# correctors 
ckx_23_i1 = Hcor(l=0.025, angle=0.0, eid='CKX.23.I1')
cky_23_i1 = Vcor(l=0.025, angle=0.0, eid='CKY.23.I1')
ckx_24_i1 = Hcor(l=0.025, angle=0.0, eid='CKX.24.I1')
cky_24_i1 = Vcor(l=0.025, angle=0.0, eid='CKY.24.I1')
ckx_25_i1 = Hcor(l=0.025, angle=0.0, eid='CKX.25.I1')
cky_25_i1 = Vcor(l=0.025, angle=0.0, eid='CKY.25.I1')
cx_37_i1 = Hcor(l=0.0, angle=0.0, eid='CX.37.I1')
cy_37_i1 = Vcor(l=0.0, angle=0.0, eid='CY.37.I1')
cx_39_i1 = Hcor(l=0.0, angle=0.0, eid='CX.39.I1')
cy_39_i1 = Vcor(l=0.0, angle=0.0, eid='CY.39.I1')
ciy_51_i1 = Vcor(l=0.1, angle=0.0, eid='CIY.51.I1')
cix_51_i1 = Hcor(l=0.1, angle=0.0, eid='CIX.51.I1')
ciy_55_i1 = Vcor(l=0.1, angle=0.0, eid='CIY.55.I1')
cix_57_i1 = Hcor(l=0.1, angle=0.0, eid='CIX.57.I1')
ciy_58_i1 = Vcor(l=0.1, angle=0.0, eid='CIY.58.I1')

# markers 
stsec_23_i1 = Marker(eid='STSEC.23.I1')
tora_25_i1 = Marker(eid='TORA.25.I1')
tora_46_i1 = Marker(eid='TORA.46.I1')
otrl_48_i1 = Marker(eid='OTRL.48.I1')
otrl_50_i1 = Marker(eid='OTRL.50.I1')
otrc_55_i1 = Marker(eid='OTRC.55.I1')
otrc_56_i1 = Marker(eid='OTRC.56.I1')
otrc_58_i1 = Marker(eid='OTRC.58.I1')
otrc_59_i1 = Marker(eid='OTRC.59.I1')
tora_60_i1 = Marker(eid='TORA.60.I1')
ensub_62_i1 = Marker(eid='ENSUB.62.I1')

# monitor 
bpmg_24_i1 = Monitor(eid='BPMG.24.I1')
bpmg_25i_i1 = Monitor(eid='BPMG.25I.I1')
bpmc_38i_i1 = Monitor(eid='BPMC.38I.I1')
bpmr_38ii_i1 = Monitor(eid='BPMR.38II.I1')
bpmf_47_i1 = Monitor(eid='BPMF.47.I1')
bpmf_48_i1 = Monitor(eid='BPMF.48.I1')
bpmf_52_i1 = Monitor(eid='BPMF.52.I1')
bpma_55_i1 = Monitor(eid='BPMA.55.I1')
bpma_57_i1 = Monitor(eid='BPMA.57.I1')
bpma_59_i1 = Monitor(eid='BPMA.59.I1')

# sextupoles 

# octupole 

# undulator 
undu_49_i1 = Undulator(lperiod=0.074, nperiods=10.81, Kx=0.0, Ky=0.0, eid='UNDU.49.I1')

# cavity 
c_a1_1_1_i1 = Cavity(l=1.0377, v=0.018124987050000003, freq=1300000000.0, phi=0.0, eid='C.A1.1.1.I1')
c_a1_1_2_i1 = Cavity(l=1.0377, v=0.018124987050000003, freq=1300000000.0, phi=0.0, eid='C.A1.1.2.I1')
c_a1_1_3_i1 = Cavity(l=1.0377, v=0.018124987050000003, freq=1300000000.0, phi=0.0, eid='C.A1.1.3.I1')
c_a1_1_4_i1 = Cavity(l=1.0377, v=0.018124987050000003, freq=1300000000.0, phi=0.0, eid='C.A1.1.4.I1')
c_a1_1_5_i1 = Cavity(l=1.0377, v=0.018124987050000003, freq=1300000000.0, phi=0.0, eid='C.A1.1.5.I1')
c_a1_1_6_i1 = Cavity(l=1.0377, v=0.018124987050000003, freq=1300000000.0, phi=0.0, eid='C.A1.1.6.I1')
c_a1_1_7_i1 = Cavity(l=1.0377, v=0.018124987050000003, freq=1300000000.0, phi=0.0, eid='C.A1.1.7.I1')
c_a1_1_8_i1 = Cavity(l=1.0377, v=0.018124987050000003, freq=1300000000.0, phi=0.0, eid='C.A1.1.8.I1')
c3_ah1_1_1_i1 = Cavity(l=0.346, v=0.0024999884, freq=3900000000.0, phi=180.0, eid='C3.AH1.1.1.I1')
c3_ah1_1_2_i1 = Cavity(l=0.346, v=0.0024999884, freq=3900000000.0, phi=180.0, eid='C3.AH1.1.2.I1')
c3_ah1_1_3_i1 = Cavity(l=0.346, v=0.0024999884, freq=3900000000.0, phi=180.0, eid='C3.AH1.1.3.I1')
c3_ah1_1_4_i1 = Cavity(l=0.346, v=0.0024999884, freq=3900000000.0, phi=180.0, eid='C3.AH1.1.4.I1')
c3_ah1_1_5_i1 = Cavity(l=0.346, v=0.0024999884, freq=3900000000.0, phi=180.0, eid='C3.AH1.1.5.I1')
c3_ah1_1_6_i1 = Cavity(l=0.346, v=0.0024999884, freq=3900000000.0, phi=180.0, eid='C3.AH1.1.6.I1')
c3_ah1_1_7_i1 = Cavity(l=0.346, v=0.0024999884, freq=3900000000.0, phi=180.0, eid='C3.AH1.1.7.I1')
c3_ah1_1_8_i1 = Cavity(l=0.346, v=0.0024999884, freq=3900000000.0, phi=180.0, eid='C3.AH1.1.8.I1')

# tdcavity 
tdsa_52_i1 = Cavity(l=0.7, v=0.0, freq=2997000.0, phi=0.0, eid='TDSA.52.I1')

# UnknowElement 

# Matrices 

# Solenoids 
solb_23_i1 = Solenoid(l=0.0, k=0.0, eid='SOLB.23.I1')

# lattice 
cell = (stsec_23_i1, d_1, solb_23_i1, d_2, ckx_23_i1, cky_23_i1, d_3, 
ckx_24_i1, cky_24_i1, d_4, bpmg_24_i1, d_5, tora_25_i1, d_6, bpmg_25i_i1, 
d_7, ckx_25_i1, cky_25_i1, d_8, c_a1_1_1_i1, d_9, c_a1_1_2_i1, d_9, 
c_a1_1_3_i1, d_9, c_a1_1_4_i1, d_9, c_a1_1_5_i1, d_9, c_a1_1_6_i1, d_9, 
c_a1_1_7_i1, d_9, c_a1_1_8_i1, d_16, q_37_i1, d_17, cx_37_i1, cy_37_i1, 
d_18, bpmc_38i_i1, d_19, bpmr_38ii_i1, d_20, q_38_i1, d_17, cx_39_i1, 
cy_39_i1, d_22, c3_ah1_1_1_i1, d_23, c3_ah1_1_2_i1, d_23, c3_ah1_1_3_i1, d_23, 
c3_ah1_1_4_i1, d_23, c3_ah1_1_5_i1, d_23, c3_ah1_1_6_i1, d_23, c3_ah1_1_7_i1, d_23, 
c3_ah1_1_8_i1, d_30, tora_46_i1, d_31, qi_46_i1, d_32, bpmf_47_i1, d_33, 
qi_47_i1, d_34, bl_48i_i1, d_35, bl_48ii_i1, d_36, bpmf_48_i1, d_37, 
otrl_48_i1, d_38, undu_49_i1, d_38, otrl_50_i1, d_40, bl_50i_i1, d_41, 
bl_50ii_i1, d_34, qi_50_i1, d_43, ciy_51_i1, d_44, cix_51_i1, d_45, 
bpmf_52_i1, d_46, qi_52_i1, d_47, tdsa_52_i1, d_47, qi_53_i1, d_49, 
qi_54_i1, d_50, otrc_55_i1, d_51, ciy_55_i1, d_52, bpma_55_i1, d_53, 
qi_55_i1, d_50, otrc_56_i1, d_51, cix_57_i1, d_52, bpma_57_i1, d_53, 
qi_57_i1, d_50, otrc_58_i1, d_59, ciy_58_i1, d_60, qi_59_i1, d_61, 
bpma_59_i1, d_62, otrc_59_i1, d_63, qi_60_i1, d_64, tora_60_i1, d_65, 
qi_61_i1, d_66, ensub_62_i1)
# power supplies 

#  
q_37_i1.ps_id = 'Q.A1.1.I1'
q_38_i1.ps_id = 'Q.AH1.1.I1'
qi_46_i1.ps_id = 'QI.1.I1'
qi_47_i1.ps_id = 'QI.2.I1'
qi_50_i1.ps_id = 'QI.3.I1'
qi_52_i1.ps_id = 'QI.4.I1'
qi_53_i1.ps_id = 'QI.5.I1'
qi_54_i1.ps_id = 'QI.6.I1'
qi_55_i1.ps_id = 'QI.7.I1'
qi_57_i1.ps_id = 'QI.8.I1'
qi_59_i1.ps_id = 'QI.9.I1'
qi_60_i1.ps_id = 'QI.11.I1'
qi_61_i1.ps_id = 'QI.12.I1'

#  

#  

#  
c_a1_1_1_i1.ps_id = 'C.A1.I1'
c_a1_1_2_i1.ps_id = 'C.A1.I1'
c_a1_1_3_i1.ps_id = 'C.A1.I1'
c_a1_1_4_i1.ps_id = 'C.A1.I1'
c_a1_1_5_i1.ps_id = 'C.A1.I1'
c_a1_1_6_i1.ps_id = 'C.A1.I1'
c_a1_1_7_i1.ps_id = 'C.A1.I1'
c_a1_1_8_i1.ps_id = 'C.A1.I1'
c3_ah1_1_1_i1.ps_id = 'C3.AH1.I1'
c3_ah1_1_2_i1.ps_id = 'C3.AH1.I1'
c3_ah1_1_3_i1.ps_id = 'C3.AH1.I1'
c3_ah1_1_4_i1.ps_id = 'C3.AH1.I1'
c3_ah1_1_5_i1.ps_id = 'C3.AH1.I1'
c3_ah1_1_6_i1.ps_id = 'C3.AH1.I1'
c3_ah1_1_7_i1.ps_id = 'C3.AH1.I1'
c3_ah1_1_8_i1.ps_id = 'C3.AH1.I1'

#  
bl_48i_i1.ps_id = 'BL.1.I1'
bl_48ii_i1.ps_id = 'BL.1.I1'
bl_50i_i1.ps_id = 'BL.3.I1'
bl_50ii_i1.ps_id = 'BL.4.I1'
