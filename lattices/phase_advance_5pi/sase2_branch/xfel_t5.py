from ocelot import * 

# drifts 
d_2 = Drift(l=1.0, eid='D_2')
d_3 = Drift(l=11.39, eid='D_3')
d_4 = Drift(l=0.205, eid='D_4')
d_5 = Drift(l=0.14, eid='D_5')
d_6 = Drift(l=9.315, eid='D_6')
d_15 = Drift(l=17.095, eid='D_15')
d_16 = Drift(l=0.21045, eid='D_16')
d_17 = Drift(l=0.15545, eid='D_17')
d_18 = Drift(l=1.545, eid='D_18')
d_21 = Drift(l=9.06, eid='D_21')
d_22 = Drift(l=0.185, eid='D_22')
d_23 = Drift(l=0.182, eid='D_23')
d_24 = Drift(l=0.21845, eid='D_24')
d_25 = Drift(l=0.38545, eid='D_25')
d_26 = Drift(l=1.5e-05, eid='D_26')
d_27 = Drift(l=1.070165, eid='D_27')
d_28 = Drift(l=3.59515, eid='D_28')
d_29 = Drift(l=0.34515, eid='D_29')
d_30 = Drift(l=0.29015, eid='D_30')
d_31 = Drift(l=0.6718, eid='D_31')
d_32 = Drift(l=2.1168, eid='D_32')
d_35 = Drift(l=1.3218, eid='D_35')
d_36 = Drift(l=1.0768, eid='D_36')
d_37 = Drift(l=0.19, eid='D_37')
d_39 = Drift(l=0.370165, eid='D_39')
d_40 = Drift(l=0.875015, eid='D_40')
d_43 = Drift(l=9.835, eid='D_43')
d_49 = Drift(l=18.61, eid='D_49')
d_52 = Drift(l=21.065, eid='D_52')
d_64 = Drift(l=11.515, eid='D_64')
d_65 = Drift(l=0.73326, eid='D_65')
d_66 = Drift(l=7.139, eid='D_66')
d_75 = Drift(l=9.676, eid='D_75')

# quadrupoles 
qe_2756_t5 = Quadrupole(l=0.24, k1=-0.21551678190000004, tilt=0.0, eid='QE.2756.T5')
qe_2766_t5 = Quadrupole(l=0.24, k1=0.1255484698, tilt=0.0, eid='QE.2766.T5')
qe_2776_t5 = Quadrupole(l=0.24, k1=0.133219012, tilt=0.0, eid='QE.2776.T5')
qe_2786_t5 = Quadrupole(l=0.24, k1=-0.2117153227, tilt=0.0, eid='QE.2786.T5')
qh_2804_t5 = Quadrupole(l=1.0291, k1=0.19652570639976683, tilt=0.0, eid='QH.2804.T5')
qh_2807_t5 = Quadrupole(l=1.0291, k1=-0.1965228316995433, tilt=0.0, eid='QH.2807.T5')
qh_2819_t5 = Quadrupole(l=1.0291, k1=0.2948796721999806, tilt=0.0, eid='QH.2819.T5')
qm_2824_t5 = Quadrupole(l=1.0597, k1=-0.2866762791997735, tilt=0.0, eid='QM.2824.T5')
qm_2829_t5 = Quadrupole(l=1.0597, k1=0.2878854605001415, tilt=0.0, eid='QM.2829.T5')
qm_2834_t5 = Quadrupole(l=1.0597, k1=-0.2866762791997735, tilt=0.0, eid='QM.2834.T5')
qm_2839_t5 = Quadrupole(l=1.0597, k1=0.2878854605001415, tilt=0.0, eid='QM.2839.T5')
qh_2844_t5 = Quadrupole(l=1.0291, k1=-0.294760129400447, tilt=0.0, eid='QH.2844.T5')
qh_2855_t5 = Quadrupole(l=1.0291, k1=0.19652570639976683, tilt=0.0, eid='QH.2855.T5')
qh_2858_t5 = Quadrupole(l=1.0291, k1=-0.1965228316995433, tilt=0.0, eid='QH.2858.T5')
qe_2878_t5 = Quadrupole(l=0.24, k1=0.19227955160000001, tilt=0.0, eid='QE.2878.T5')
qe_2900_t5 = Quadrupole(l=0.24, k1=-0.19227955160000001, tilt=0.0, eid='QE.2900.T5')
qe_2922_t5 = Quadrupole(l=0.24, k1=0.19227955160000001, tilt=0.0, eid='QE.2922.T5')
qe_2943_t5 = Quadrupole(l=0.24, k1=-0.19227955160000001, tilt=0.0, eid='QE.2943.T5')
qe_2965_t5 = Quadrupole(l=0.24, k1=0.19227955160000001, tilt=0.0, eid='QE.2965.T5')
qe_2985_un2 = Quadrupole(l=0.24, k1=-0.19227955160000001, tilt=0.0, eid='QE.2985.UN2')
qe_3007_un2 = Quadrupole(l=0.24, k1=0.19227955160000001, tilt=0.0, eid='QE.3007.UN2')
qe_3029_un2 = Quadrupole(l=0.24, k1=-0.19227955160000001, tilt=0.0, eid='QE.3029.UN2')

# bending magnets 
be_2821_t5 = SBend(l = 2.5, angle=-0.0169497, e1=-0.00847485, e2=-0.00847485, gap=0, tilt=0.0, fint=0.0, fintx=0.0, eid='BE.2821.T5')
be_2841_t5 = SBend(l = 2.5, angle=-0.0169497, e1=-0.00847485, e2=-0.00847485, gap=0, tilt=0.0, fint=0.0, fintx=0.0, eid='BE.2841.T5')

# correctors 
cey_2756_t5 = Vcor(l=0.1, angle=0.0, eid='CEY.2756.T5')
cex_2766_t5 = Hcor(l=0.1, angle=0.0, eid='CEX.2766.T5')
cex_2776_t5 = Hcor(l=0.1, angle=0.0, eid='CEX.2776.T5')
cey_2786_t5 = Vcor(l=0.1, angle=0.0, eid='CEY.2786.T5')
chx_2805_t5 = Hcor(l=0.2, angle=0.0, eid='CHX.2805.T5')
chy_2808_t5 = Vcor(l=0.2, angle=0.0, eid='CHY.2808.T5')
chx_2817_t5 = Hcor(l=0.2, angle=0.0, eid='CHX.2817.T5')
chy_2818_t5 = Vcor(l=0.2, angle=0.0, eid='CHY.2818.T5')
chx_2830_t5 = Hcor(l=0.2, angle=0.0, eid='CHX.2830.T5')
chy_2835_t5 = Vcor(l=0.2, angle=0.0, eid='CHY.2835.T5')
chx_2838_t5 = Hcor(l=0.2, angle=0.0, eid='CHX.2838.T5')
chy_2845_t5 = Vcor(l=0.2, angle=0.0, eid='CHY.2845.T5')
chx_2856_t5 = Hcor(l=0.2, angle=0.0, eid='CHX.2856.T5')
chy_2859_t5 = Vcor(l=0.2, angle=0.0, eid='CHY.2859.T5')
cex_2879_t5 = Hcor(l=0.1, angle=0.0, eid='CEX.2879.T5')
cey_2900_t5 = Vcor(l=0.1, angle=0.0, eid='CEY.2900.T5')
cex_2922_t5 = Hcor(l=0.1, angle=0.0, eid='CEX.2922.T5')
cey_2944_t5 = Vcor(l=0.1, angle=0.0, eid='CEY.2944.T5')
cex_2966_t5 = Hcor(l=0.1, angle=0.0, eid='CEX.2966.T5')
cey_2986_un2 = Vcor(l=0.1, angle=0.0, eid='CEY.2986.UN2')
cex_3007_un2 = Hcor(l=0.1, angle=0.0, eid='CEX.3007.UN2')
cey_3029_un2 = Vcor(l=0.1, angle=0.0, eid='CEY.3029.UN2')

# markers 
stsec_2743_t5 = Marker(eid='STSEC.2743.T5')
stsub_2743_t5 = Marker(eid='STSUB.2743.T5')
tora_2744_t5 = Marker(eid='TORA.2744.T5')
ensub_2820_t5 = Marker(eid='ENSUB.2820.T5')
stsub_2820_t5 = Marker(eid='STSUB.2820.T5')
tora_2977_t5 = Marker(eid='TORA.2977.T5')
ensub_2978_t5 = Marker(eid='ENSUB.2978.T5')
ensec_2978_t5 = Marker(eid='ENSEC.2978.T5')
stsec_2978_un2 = Marker(eid='STSEC.2978.UN2')
ensec_3039_un2 = Marker(eid='ENSEC.3039.UN2')
stsec_3039_t5d = Marker(eid='STSEC.3039.T5D')

# monitor 
bpma_2756_t5 = Monitor(eid='BPMA.2756.T5')
bpma_2766_t5 = Monitor(eid='BPMA.2766.T5')
bpma_2776_t5 = Monitor(eid='BPMA.2776.T5')
bpma_2786_t5 = Monitor(eid='BPMA.2786.T5')
bpma_2804_t5 = Monitor(eid='BPMA.2804.T5')
bpma_2807_t5 = Monitor(eid='BPMA.2807.T5')
bpma_2818_t5 = Monitor(eid='BPMA.2818.T5')
bpma_2828_t5 = Monitor(eid='BPMA.2828.T5')
bpma_2833_t5 = Monitor(eid='BPMA.2833.T5')
bpma_2838_t5 = Monitor(eid='BPMA.2838.T5')
bpma_2843_t5 = Monitor(eid='BPMA.2843.T5')
bpma_2855_t5 = Monitor(eid='BPMA.2855.T5')
bpma_2858_t5 = Monitor(eid='BPMA.2858.T5')
bpma_2878_t5 = Monitor(eid='BPMA.2878.T5')
bpma_2900_t5 = Monitor(eid='BPMA.2900.T5')
bpma_2921_t5 = Monitor(eid='BPMA.2921.T5')
bpma_2943_t5 = Monitor(eid='BPMA.2943.T5')
bpma_2965_t5 = Monitor(eid='BPMA.2965.T5')
bpma_2985_un2 = Monitor(eid='BPMA.2985.UN2')
bpma_3007_un2 = Monitor(eid='BPMA.3007.UN2')
bpma_3028_un2 = Monitor(eid='BPMA.3028.UN2')

# sextupoles 
saox_2831_t5 = Sextupole(l=0.3164, k2=-16.23261694, tilt=0.0, eid='SAOX.2831.T5')
sao_2836_t5 = Sextupole(l=0.3164, k2=-5.755372945998736, tilt=0.0, eid='SAO.2836.T5')

# octupole 

# undulator 

# cavity 

# UnknowElement 

# Matrices 

# Solenoids 

# lattice 
cell = (stsec_2743_t5, stsub_2743_t5, d_2, tora_2744_t5, d_3, bpma_2756_t5,
d_4, qe_2756_t5, d_5, cey_2756_t5, d_6, bpma_2766_t5, d_4, qe_2766_t5, 
d_5, cex_2766_t5, d_6, bpma_2776_t5, d_4, qe_2776_t5, d_5, cex_2776_t5, 
d_6, bpma_2786_t5, d_4, qe_2786_t5, d_5, cey_2786_t5, d_15, bpma_2804_t5, 
d_16, qh_2804_t5, d_17, chx_2805_t5, d_18, bpma_2807_t5, d_16, qh_2807_t5, 
d_17, chy_2808_t5, d_21, chx_2817_t5, d_22, chy_2818_t5, d_23, bpma_2818_t5, 
d_24, qh_2819_t5, d_25, ensub_2820_t5, stsub_2820_t5, d_26, be_2821_t5, d_27, 
qm_2824_t5, d_28, bpma_2828_t5, d_29, qm_2829_t5, d_30, chx_2830_t5, d_31, 
saox_2831_t5, d_32, bpma_2833_t5, d_29, qm_2834_t5, d_30, chy_2835_t5, d_35, 
sao_2836_t5, d_36, chx_2838_t5, d_37, bpma_2838_t5, d_29, qm_2839_t5, d_39, 
be_2841_t5, d_40, bpma_2843_t5, d_16, qh_2844_t5, d_17, chy_2845_t5, d_43, 
bpma_2855_t5, d_16, qh_2855_t5, d_17, chx_2856_t5, d_18, bpma_2858_t5, d_16, 
qh_2858_t5, d_17, chy_2859_t5, d_49, bpma_2878_t5, d_4, qe_2878_t5, d_5, 
cex_2879_t5, d_52, bpma_2900_t5, d_4, qe_2900_t5, d_5, cey_2900_t5, d_52, 
bpma_2921_t5, d_4, qe_2922_t5, d_5, cex_2922_t5, d_52, bpma_2943_t5, d_4, 
qe_2943_t5, d_5, cey_2944_t5, d_52, bpma_2965_t5, d_4, qe_2965_t5, d_5, 
cex_2966_t5, d_64, tora_2977_t5, d_65, ensub_2978_t5, ensec_2978_t5, stsec_2978_un2, d_66, 
bpma_2985_un2, d_4, qe_2985_un2, d_5, cey_2986_un2, d_52, bpma_3007_un2, d_4, 
qe_3007_un2, d_5, cex_3007_un2, d_52, bpma_3028_un2, d_4, qe_3029_un2, d_5, 
cey_3029_un2, d_75, ensec_3039_un2, stsec_3039_t5d)
# power supplies 

#  
qe_2756_t5.ps_id = 'QE.3.T5'
qe_2766_t5.ps_id = 'QE.4.T5'
qe_2776_t5.ps_id = 'QE.5.T5'
qe_2786_t5.ps_id = 'QE.6.T5'
qh_2804_t5.ps_id = 'QH.3.T5'
qh_2807_t5.ps_id = 'QH.4.T5'
qh_2819_t5.ps_id = 'QH.1.T5'
qm_2824_t5.ps_id = 'QM.2.T5'
qm_2829_t5.ps_id = 'QM.1.T5'
qm_2834_t5.ps_id = 'QM.2.T5'
qm_2839_t5.ps_id = 'QM.1.T5'
qh_2844_t5.ps_id = 'QH.2.T5'
qh_2855_t5.ps_id = 'QH.3.T5'
qh_2858_t5.ps_id = 'QH.4.T5'
qe_2878_t5.ps_id = 'QE.1.T5'
qe_2900_t5.ps_id = 'QE.2.T5'
qe_2922_t5.ps_id = 'QE.1.T5'
qe_2943_t5.ps_id = 'QE.2.T5'
qe_2965_t5.ps_id = 'QE.1.T5'
qe_2985_un2.ps_id = 'QE.2.UN2'
qe_3007_un2.ps_id = 'QE.1.UN2'
qe_3029_un2.ps_id = 'QE.2.UN2'

#  
saox_2831_t5.ps_id = 'SAOX.1.T5'
sao_2836_t5.ps_id = 'SAO.2.T5'

#  

#  

#  
be_2821_t5.ps_id = 'BE.1.T5'
be_2841_t5.ps_id = 'BE.1.T5'
