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
d_5 = Drift(l=0.15, eid='D_5')
d_6 = Drift(l=0.198782, eid='D_6')
d_7 = Drift(l=0.439218, eid='D_7')
d_8 = Drift(l=0.225, eid='D_8')
d_9 = Drift(l=0.088, eid='D_9')
d_10 = Drift(l=0.111, eid='D_10')
d_11 = Drift(l=0.31, eid='D_11')
d_12 = Drift(l=0.5776, eid='D_12')
d_13 = Drift(l=0.1, eid='D_13')
d_14 = Drift(l=0.2216, eid='D_14')
d_15 = Drift(l=0.3459, eid='D_15')
d_22 = Drift(l=0.2043, eid='D_22')
d_23 = Drift(l=0.0432, eid='D_23')
d_25 = Drift(l=0.085, eid='D_25')
d_26 = Drift(l=0.4579, eid='D_26')
d_27 = Drift(l=0.2211, eid='D_27')
d_28 = Drift(l=0.1282, eid='D_28')
d_30 = Drift(l=0.202, eid='D_30')
d_31 = Drift(l=0.262, eid='D_31')
d_38 = Drift(l=0.155, eid='D_38')
d_39 = Drift(l=2.3364, eid='D_39')
d_40 = Drift(l=0.33305, eid='D_40')
d_41 = Drift(l=0.08615, eid='D_41')
d_42 = Drift(l=0.2175, eid='D_42')
d_43 = Drift(l=0.096, eid='D_43')
d_44 = Drift(l=0.1177, eid='D_44')
d_45 = Drift(l=0.12345, eid='D_45')
d_46 = Drift(l=0.08115, eid='D_46')
d_47 = Drift(l=0.051165, eid='D_47')
d_48 = Drift(l=0.100827, eid='D_48')
d_49 = Drift(l=0.092415, eid='D_49')
d_51 = Drift(l=0.27175, eid='D_51')
d_52 = Drift(l=0.164, eid='D_52')
d_54 = Drift(l=0.120165, eid='D_54')
d_55 = Drift(l=0.100828, eid='D_55')
d_58 = Drift(l=0.18964, eid='D_58')
d_59 = Drift(l=0.2, eid='D_59')
d_60 = Drift(l=0.303, eid='D_60')
d_61 = Drift(l=0.1975, eid='D_61')
d_63 = Drift(l=0.08765, eid='D_63')
d_64 = Drift(l=0.05115, eid='D_64')
d_66 = Drift(l=0.7143, eid='D_66')
d_67 = Drift(l=0.72115, eid='D_67')
d_68 = Drift(l=0.035, eid='D_68')
d_69 = Drift(l=0.175, eid='D_69')
d_71 = Drift(l=0.13115, eid='D_71')
d_72 = Drift(l=0.75615, eid='D_72')
d_77 = Drift(l=0.275, eid='D_77')
d_78 = Drift(l=0.18115, eid='D_78')
d_79 = Drift(l=0.20115, eid='D_79')
d_80 = Drift(l=0.38, eid='D_80')
d_81 = Drift(l=0.28115, eid='D_81')
d_82 = Drift(l=0.26285, eid='D_82')
d_83 = Drift(l=0.74945, eid='D_83')
d_84 = Drift(l=0.53115, eid='D_84')

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
stsub_23_i1 = Marker(eid='STSUB.23.I1')
gun_23_i1 = Marker(eid='GUN.23.I1')
scrn_24_i1 = Marker(eid='SCRN.24.I1')
fcup_24_i1 = Marker(eid='FCUP.24.I1')
ensub_24_i1 = Marker(eid='ENSUB.24.I1')
stsub_24i_i1 = Marker(eid='STSUB.24I.I1')
tora_25_i1 = Marker(eid='TORA.25.I1')
scrn_25i_i1 = Marker(eid='SCRN.25I.I1')
fcup_25i_i1 = Marker(eid='FCUP.25I.I1')
dcm_25_i1 = Marker(eid='DCM.25.I1')
id_22433449_ = Marker(eid='ID_22433449_')
stac_26_i1 = Marker(eid='STAC.26.I1')
id_75115473_ = Marker(eid='ID_75115473_')
id_68749308_ = Marker(eid='ID_68749308_')
match_37_i1 = Marker(eid='MATCH.37.I1')
enac_38_i1 = Marker(eid='ENAC.38.I1')
stac_38_i1 = Marker(eid='STAC.38.I1')
enac_44_i1 = Marker(eid='ENAC.44.I1')
tora_46_i1 = Marker(eid='TORA.46.I1')
bam_47_i1 = Marker(eid='BAM.47.I1')
mpbpmf_47_i1 = Marker(eid='MPBPMF.47.I1')
dcm_47_i1 = Marker(eid='DCM.47.I1')
stlat_47_i1 = Marker(eid='STLAT.47.I1')
mpbpmf_48_i1 = Marker(eid='MPBPMF.48.I1')
otrl_48_i1 = Marker(eid='OTRL.48.I1')
otrl_50_i1 = Marker(eid='OTRL.50.I1')
enlat_50_i1 = Marker(eid='ENLAT.50.I1')
eod_51_i1 = Marker(eid='EOD.51.I1')
mpbpmf_52_i1 = Marker(eid='MPBPMF.52.I1')
stlat_55_i1 = Marker(eid='STLAT.55.I1')
match_55_i1 = Marker(eid='MATCH.55.I1')
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
cell = (stsec_23_i1, stsub_23_i1, gun_23_i1, d_1, solb_23_i1, d_2, ckx_23_i1, 
cky_23_i1, d_3, ckx_24_i1, cky_24_i1, d_4, bpmg_24_i1, d_5, scrn_24_i1, 
fcup_24_i1, d_6, ensub_24_i1, stsub_24i_i1, d_7, tora_25_i1, d_8, scrn_25i_i1, 
fcup_25i_i1, d_9, bpmg_25i_i1, d_10, dcm_25_i1, d_11, ckx_25_i1, cky_25_i1, 
d_12, id_22433449_, d_13, stac_26_i1, d_14, c_a1_1_1_i1, id_75115473_, d_15, 
c_a1_1_2_i1, d_15, c_a1_1_3_i1, d_15, c_a1_1_4_i1, d_15, c_a1_1_5_i1, d_15, 
c_a1_1_6_i1, d_15, c_a1_1_7_i1, d_15, c_a1_1_8_i1, id_68749308_, d_22, match_37_i1, 
d_23, q_37_i1, d_23, cx_37_i1, cy_37_i1, d_25, bpmc_38i_i1, d_26, 
enac_38_i1, stac_38_i1, d_27, bpmr_38ii_i1, d_28, q_38_i1, d_23, cx_39_i1, 
cy_39_i1, d_30, c3_ah1_1_1_i1, d_31, c3_ah1_1_2_i1, d_31, c3_ah1_1_3_i1, d_31, 
c3_ah1_1_4_i1, d_31, c3_ah1_1_5_i1, d_31, c3_ah1_1_6_i1, d_31, c3_ah1_1_7_i1, d_31, 
c3_ah1_1_8_i1, d_38, enac_44_i1, d_39, tora_46_i1, d_40, qi_46_i1, d_41, 
bam_47_i1, d_42, bpmf_47_i1, d_43, mpbpmf_47_i1, d_44, dcm_47_i1, d_45, 
qi_47_i1, d_46, stlat_47_i1, d_47, bl_48i_i1, d_48, bl_48ii_i1, d_49, 
mpbpmf_48_i1, d_43, bpmf_48_i1, d_51, otrl_48_i1, d_52, undu_49_i1, d_52, 
otrl_50_i1, d_54, bl_50i_i1, d_55, bl_50ii_i1, d_47, enlat_50_i1, d_46, 
qi_50_i1, d_58, eod_51_i1, d_59, ciy_51_i1, d_60, cix_51_i1, d_61, 
bpmf_52_i1, d_43, mpbpmf_52_i1, d_63, qi_52_i1, d_64, tdsa_52_i1, d_64, 
qi_53_i1, d_66, qi_54_i1, d_67, stlat_55_i1, d_68, match_55_i1, otrc_55_i1, 
d_69, ciy_55_i1, d_5, bpma_55_i1, d_71, qi_55_i1, d_72, otrc_56_i1, 
d_69, cix_57_i1, d_5, bpma_57_i1, d_71, qi_57_i1, d_72, otrc_58_i1, 
d_77, ciy_58_i1, d_78, qi_59_i1, d_79, bpma_59_i1, d_80, otrc_59_i1, 
d_81, qi_60_i1, d_82, tora_60_i1, d_83, qi_61_i1, d_84, ensub_62_i1)
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
