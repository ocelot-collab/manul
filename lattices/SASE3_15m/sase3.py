from ocelot import * 
tws = Twiss()
tws.beta_x  = 22.42894928394991
tws.beta_y  = 9.632646879807218
tws.alpha_x = 1.5001188227461622
tws.alpha_y = -0.6639763667383163
tws.E = 14
# drifts 
d_1 = Drift(l=5.7595, eid='D_1')
d_2 = Drift(l=0.18665, eid='D_2')
d_3 = Drift(l=5.79965, eid='D_3')
d_5 = Drift(l=0.35787, eid='D_5')
d_6 = Drift(l=0.07278, eid='D_6')
d_7 = Drift(l=0.0717, eid='D_7')
d_8 = Drift(l=0.2973, eid='D_8')
d_110 = Drift(l=0.04015, eid='D_110')

# quadrupoles 
qa_2806_sa3 = Quadrupole(l=0.1137, k1=-1.1974301231310467, tilt=0.0, eid='QA.2806.SA3')
qa_2812_sa3 = Quadrupole(l=0.1137, k1=1.1974301231310467, tilt=0.0, eid='QA.2812.SA3')
qa_2818_sa3 = Quadrupole(l=0.1137, k1=-1.1974301231310467, tilt=0.0, eid='QA.2818.SA3')
qa_2824_sa3 = Quadrupole(l=0.1137, k1=1.1974301231310467, tilt=0.0, eid='QA.2824.SA3')
qa_2831_sa3 = Quadrupole(l=0.1137, k1=-1.1974301231310467, tilt=0.0, eid='QA.2831.SA3')
qa_2837_sa3 = Quadrupole(l=0.1137, k1=1.1974301231310467, tilt=0.0, eid='QA.2837.SA3')
qa_2843_sa3 = Quadrupole(l=0.1137, k1=-1.1974301231310467, tilt=0.0, eid='QA.2843.SA3')
qa_2849_sa3 = Quadrupole(l=0.1137, k1=1.1974301231310467, tilt=0.0, eid='QA.2849.SA3')
qa_2855_sa3 = Quadrupole(l=0.1137, k1=-1.1974301231310467, tilt=0.0, eid='QA.2855.SA3')
qa_2861_sa3 = Quadrupole(l=0.1137, k1=1.1974301231310467, tilt=0.0, eid='QA.2861.SA3')
qa_2867_sa3 = Quadrupole(l=0.1137, k1=-1.1974301231310467, tilt=0.0, eid='QA.2867.SA3')
qa_2873_sa3 = Quadrupole(l=0.1137, k1=1.1974301231310467, tilt=0.0, eid='QA.2873.SA3')
qa_2879_sa3 = Quadrupole(l=0.1137, k1=-1.1974301231310467, tilt=0.0, eid='QA.2879.SA3')
qa_2885_sa3 = Quadrupole(l=0.1137, k1=1.1974301231310467, tilt=0.0, eid='QA.2885.SA3')
qa_2892_sa3 = Quadrupole(l=0.1137, k1=-1.1974301231310467, tilt=0.0, eid='QA.2892.SA3')
qa_2898_sa3 = Quadrupole(l=0.1137, k1=1.1974301231310467, tilt=0.0, eid='QA.2898.SA3')
qa_2904_sa3 = Quadrupole(l=0.1137, k1=-1.1974301231310467, tilt=0.0, eid='QA.2904.SA3')
qa_2910_sa3 = Quadrupole(l=0.1137, k1=1.1974301231310467, tilt=0.0, eid='QA.2910.SA3')
qa_2916_sa3 = Quadrupole(l=0.1137, k1=-1.1974301231310467, tilt=0.0, eid='QA.2916.SA3')
qa_2922_sa3 = Quadrupole(l=0.1137, k1=1.1974301231310467, tilt=0.0, eid='QA.2922.SA3')
qa_2928_sa3 = Quadrupole(l=0.1137, k1=-1.1974301231310467, tilt=0.0, eid='QA.2928.SA3')
qa_2934_sa3 = Quadrupole(l=0.1137, k1=1.1974301231310467, tilt=0.0, eid='QA.2934.SA3')
qa_2940_sa3 = Quadrupole(l=0.1137, k1=-1.1974301231310467, tilt=0.0, eid='QA.2940.SA3')

# bending magnets 

# correctors 
cax_2813_sa3 = Hcor(l=0.0, angle=0.0, eid='CAX.2813.SA3')
cay_2813_sa3 = Vcor(l=0.0, angle=0.0, eid='CAY.2813.SA3')
cbx_2818_sa3 = Hcor(l=0.0, angle=0.0, eid='CBX.2818.SA3')
cby_2818_sa3 = Vcor(l=0.0, angle=0.0, eid='CBY.2818.SA3')
cax_2819_sa3 = Hcor(l=0.0, angle=0.0, eid='CAX.2819.SA3')
cay_2819_sa3 = Vcor(l=0.0, angle=0.0, eid='CAY.2819.SA3')
cbx_2824_sa3 = Hcor(l=0.0, angle=0.0, eid='CBX.2824.SA3')
cby_2824_sa3 = Vcor(l=0.0, angle=0.0, eid='CBY.2824.SA3')
cax_2825_sa3 = Hcor(l=0.0, angle=0.0, eid='CAX.2825.SA3')
cay_2825_sa3 = Vcor(l=0.0, angle=0.0, eid='CAY.2825.SA3')
cbx_2830_sa3 = Hcor(l=0.0, angle=0.0, eid='CBX.2830.SA3')
cby_2830_sa3 = Vcor(l=0.0, angle=0.0, eid='CBY.2830.SA3')
cax_2831_sa3 = Hcor(l=0.0, angle=0.0, eid='CAX.2831.SA3')
cay_2831_sa3 = Vcor(l=0.0, angle=0.0, eid='CAY.2831.SA3')
cbx_2836_sa3 = Hcor(l=0.0, angle=0.0, eid='CBX.2836.SA3')
cby_2836_sa3 = Vcor(l=0.0, angle=0.0, eid='CBY.2836.SA3')
cax_2838_sa3 = Hcor(l=0.0, angle=0.0, eid='CAX.2838.SA3')
cay_2838_sa3 = Vcor(l=0.0, angle=0.0, eid='CAY.2838.SA3')
cbx_2842_sa3 = Hcor(l=0.0, angle=0.0, eid='CBX.2842.SA3')
cby_2842_sa3 = Vcor(l=0.0, angle=0.0, eid='CBY.2842.SA3')
cax_2844_sa3 = Hcor(l=0.0, angle=0.0, eid='CAX.2844.SA3')
cay_2844_sa3 = Vcor(l=0.0, angle=0.0, eid='CAY.2844.SA3')
cbx_2848_sa3 = Hcor(l=0.0, angle=0.0, eid='CBX.2848.SA3')
cby_2848_sa3 = Vcor(l=0.0, angle=0.0, eid='CBY.2848.SA3')
cax_2850_sa3 = Hcor(l=0.0, angle=0.0, eid='CAX.2850.SA3')
cay_2850_sa3 = Vcor(l=0.0, angle=0.0, eid='CAY.2850.SA3')
cbx_2854_sa3 = Hcor(l=0.0, angle=0.0, eid='CBX.2854.SA3')
cby_2854_sa3 = Vcor(l=0.0, angle=0.0, eid='CBY.2854.SA3')
cax_2856_sa3 = Hcor(l=0.0, angle=0.0, eid='CAX.2856.SA3')
cay_2856_sa3 = Vcor(l=0.0, angle=0.0, eid='CAY.2856.SA3')
cbx_2860_sa3 = Hcor(l=0.0, angle=0.0, eid='CBX.2860.SA3')
cby_2860_sa3 = Vcor(l=0.0, angle=0.0, eid='CBY.2860.SA3')
cax_2862_sa3 = Hcor(l=0.0, angle=0.0, eid='CAX.2862.SA3')
cay_2862_sa3 = Vcor(l=0.0, angle=0.0, eid='CAY.2862.SA3')
cbx_2867_sa3 = Hcor(l=0.0, angle=0.0, eid='CBX.2867.SA3')
cby_2867_sa3 = Vcor(l=0.0, angle=0.0, eid='CBY.2867.SA3')
cax_2868_sa3 = Hcor(l=0.0, angle=0.0, eid='CAX.2868.SA3')
cay_2868_sa3 = Vcor(l=0.0, angle=0.0, eid='CAY.2868.SA3')
cbx_2873_sa3 = Hcor(l=0.0, angle=0.0, eid='CBX.2873.SA3')
cby_2873_sa3 = Vcor(l=0.0, angle=0.0, eid='CBY.2873.SA3')
cax_2874_sa3 = Hcor(l=0.0, angle=0.0, eid='CAX.2874.SA3')
cay_2874_sa3 = Vcor(l=0.0, angle=0.0, eid='CAY.2874.SA3')
cbx_2879_sa3 = Hcor(l=0.0, angle=0.0, eid='CBX.2879.SA3')
cby_2879_sa3 = Vcor(l=0.0, angle=0.0, eid='CBY.2879.SA3')
cax_2880_sa3 = Hcor(l=0.0, angle=0.0, eid='CAX.2880.SA3')
cay_2880_sa3 = Vcor(l=0.0, angle=0.0, eid='CAY.2880.SA3')
cbx_2885_sa3 = Hcor(l=0.0, angle=0.0, eid='CBX.2885.SA3')
cby_2885_sa3 = Vcor(l=0.0, angle=0.0, eid='CBY.2885.SA3')
cax_2886_sa3 = Hcor(l=0.0, angle=0.0, eid='CAX.2886.SA3')
cay_2886_sa3 = Vcor(l=0.0, angle=0.0, eid='CAY.2886.SA3')
cbx_2891_sa3 = Hcor(l=0.0, angle=0.0, eid='CBX.2891.SA3')
cby_2891_sa3 = Vcor(l=0.0, angle=0.0, eid='CBY.2891.SA3')
cax_2892_sa3 = Hcor(l=0.0, angle=0.0, eid='CAX.2892.SA3')
cay_2892_sa3 = Vcor(l=0.0, angle=0.0, eid='CAY.2892.SA3')
cbx_2897_sa3 = Hcor(l=0.0, angle=0.0, eid='CBX.2897.SA3')
cby_2897_sa3 = Vcor(l=0.0, angle=0.0, eid='CBY.2897.SA3')
cax_2899_sa3 = Hcor(l=0.0, angle=0.0, eid='CAX.2899.SA3')
cay_2899_sa3 = Vcor(l=0.0, angle=0.0, eid='CAY.2899.SA3')
cbx_2903_sa3 = Hcor(l=0.0, angle=0.0, eid='CBX.2903.SA3')
cby_2903_sa3 = Vcor(l=0.0, angle=0.0, eid='CBY.2903.SA3')
cax_2905_sa3 = Hcor(l=0.0, angle=0.0, eid='CAX.2905.SA3')
cay_2905_sa3 = Vcor(l=0.0, angle=0.0, eid='CAY.2905.SA3')
cbx_2909_sa3 = Hcor(l=0.0, angle=0.0, eid='CBX.2909.SA3')
cby_2909_sa3 = Vcor(l=0.0, angle=0.0, eid='CBY.2909.SA3')
cax_2911_sa3 = Hcor(l=0.0, angle=0.0, eid='CAX.2911.SA3')
cay_2911_sa3 = Vcor(l=0.0, angle=0.0, eid='CAY.2911.SA3')
cbx_2915_sa3 = Hcor(l=0.0, angle=0.0, eid='CBX.2915.SA3')
cby_2915_sa3 = Vcor(l=0.0, angle=0.0, eid='CBY.2915.SA3')
cax_2917_sa3 = Hcor(l=0.0, angle=0.0, eid='CAX.2917.SA3')
cay_2917_sa3 = Vcor(l=0.0, angle=0.0, eid='CAY.2917.SA3')
cbx_2921_sa3 = Hcor(l=0.0, angle=0.0, eid='CBX.2921.SA3')
cby_2921_sa3 = Vcor(l=0.0, angle=0.0, eid='CBY.2921.SA3')
cax_2923_sa3 = Hcor(l=0.0, angle=0.0, eid='CAX.2923.SA3')
cay_2923_sa3 = Vcor(l=0.0, angle=0.0, eid='CAY.2923.SA3')
cbx_2928_sa3 = Hcor(l=0.0, angle=0.0, eid='CBX.2928.SA3')
cby_2928_sa3 = Vcor(l=0.0, angle=0.0, eid='CBY.2928.SA3')
cax_2929_sa3 = Hcor(l=0.0, angle=0.0, eid='CAX.2929.SA3')
cay_2929_sa3 = Vcor(l=0.0, angle=0.0, eid='CAY.2929.SA3')
cbx_2934_sa3 = Hcor(l=0.0, angle=0.0, eid='CBX.2934.SA3')
cby_2934_sa3 = Vcor(l=0.0, angle=0.0, eid='CBY.2934.SA3')
cax_2935_sa3 = Hcor(l=0.0, angle=0.0, eid='CAX.2935.SA3')
cay_2935_sa3 = Vcor(l=0.0, angle=0.0, eid='CAY.2935.SA3')
cbx_2940_sa3 = Hcor(l=0.0, angle=0.0, eid='CBX.2940.SA3')
cby_2940_sa3 = Vcor(l=0.0, angle=0.0, eid='CBY.2940.SA3')

# markers 
ensec_2800_t4 = Marker(eid='ENSEC.2800.T4')
ensec_2940_sa3 = Marker(eid='ENSEC.2940.SA3')

# monitor 
bpme_2806_sa3 = Monitor(eid='BPME.2806.SA3')
bpme_2812_sa3 = Monitor(eid='BPME.2812.SA3')
bpme_2818_sa3 = Monitor(eid='BPME.2818.SA3')
bpme_2824_sa3 = Monitor(eid='BPME.2824.SA3')
bpme_2830_sa3 = Monitor(eid='BPME.2830.SA3')
bpme_2836_sa3 = Monitor(eid='BPME.2836.SA3')
bpme_2842_sa3 = Monitor(eid='BPME.2842.SA3')
bpme_2849_sa3 = Monitor(eid='BPME.2849.SA3')
bpme_2855_sa3 = Monitor(eid='BPME.2855.SA3')
bpme_2861_sa3 = Monitor(eid='BPME.2861.SA3')
bpme_2867_sa3 = Monitor(eid='BPME.2867.SA3')
bpme_2873_sa3 = Monitor(eid='BPME.2873.SA3')
bpme_2879_sa3 = Monitor(eid='BPME.2879.SA3')
bpme_2885_sa3 = Monitor(eid='BPME.2885.SA3')
bpme_2891_sa3 = Monitor(eid='BPME.2891.SA3')
bpme_2897_sa3 = Monitor(eid='BPME.2897.SA3')
bpme_2903_sa3 = Monitor(eid='BPME.2903.SA3')
bpme_2910_sa3 = Monitor(eid='BPME.2910.SA3')
bpme_2916_sa3 = Monitor(eid='BPME.2916.SA3')
bpme_2922_sa3 = Monitor(eid='BPME.2922.SA3')
bpme_2928_sa3 = Monitor(eid='BPME.2928.SA3')
bpme_2934_sa3 = Monitor(eid='BPME.2934.SA3')
bpme_2940_sa3 = Monitor(eid='BPME.2940.SA3')

# sextupoles 

# octupole 

# undulator 
u68_2815_sa3 = Undulator(lperiod=0.068, nperiods=73.53, Kx=0.0, Ky=0.0, eid='U68.2815.SA3')
u68_2821_sa3 = Undulator(lperiod=0.068, nperiods=73.53, Kx=0.0, Ky=0.0, eid='U68.2821.SA3')
u68_2827_sa3 = Undulator(lperiod=0.068, nperiods=73.53, Kx=0.0, Ky=0.0, eid='U68.2827.SA3')
u68_2834_sa3 = Undulator(lperiod=0.068, nperiods=73.53, Kx=0.0, Ky=0.0, eid='U68.2834.SA3')
u68_2840_sa3 = Undulator(lperiod=0.068, nperiods=73.53, Kx=0.0, Ky=0.0, eid='U68.2840.SA3')
u68_2846_sa3 = Undulator(lperiod=0.068, nperiods=73.53, Kx=0.0, Ky=0.0, eid='U68.2846.SA3')
u68_2852_sa3 = Undulator(lperiod=0.068, nperiods=73.53, Kx=0.0, Ky=0.0, eid='U68.2852.SA3')
u68_2858_sa3 = Undulator(lperiod=0.068, nperiods=73.53, Kx=0.0, Ky=0.0, eid='U68.2858.SA3')
u68_2864_sa3 = Undulator(lperiod=0.068, nperiods=73.53, Kx=0.0, Ky=0.0, eid='U68.2864.SA3')
u68_2870_sa3 = Undulator(lperiod=0.068, nperiods=73.53, Kx=0.0, Ky=0.0, eid='U68.2870.SA3')
u68_2876_sa3 = Undulator(lperiod=0.068, nperiods=73.53, Kx=0.0, Ky=0.0, eid='U68.2876.SA3')
u68_2882_sa3 = Undulator(lperiod=0.068, nperiods=73.53, Kx=0.0, Ky=0.0, eid='U68.2882.SA3')
u68_2888_sa3 = Undulator(lperiod=0.068, nperiods=73.53, Kx=0.0, Ky=0.0, eid='U68.2888.SA3')
u68_2894_sa3 = Undulator(lperiod=0.068, nperiods=73.53, Kx=0.0, Ky=0.0, eid='U68.2894.SA3')
u68_2901_sa3 = Undulator(lperiod=0.068, nperiods=73.53, Kx=0.0, Ky=0.0, eid='U68.2901.SA3')
u68_2907_sa3 = Undulator(lperiod=0.068, nperiods=73.53, Kx=0.0, Ky=0.0, eid='U68.2907.SA3')
u68_2913_sa3 = Undulator(lperiod=0.068, nperiods=73.53, Kx=0.0, Ky=0.0, eid='U68.2913.SA3')
u68_2919_sa3 = Undulator(lperiod=0.068, nperiods=73.53, Kx=0.0, Ky=0.0, eid='U68.2919.SA3')
u68_2925_sa3 = Undulator(lperiod=0.068, nperiods=73.53, Kx=0.0, Ky=0.0, eid='U68.2925.SA3')
u68_2931_sa3 = Undulator(lperiod=0.068, nperiods=73.53, Kx=0.0, Ky=0.0, eid='U68.2931.SA3')
u68_2937_sa3 = Undulator(lperiod=0.068, nperiods=73.53, Kx=0.0, Ky=0.0, eid='U68.2937.SA3')

# cavity 

# tdcavity 

# UnknowElement 

# Matrices 

# Solenoids 

# lattice 
cell = (ensec_2800_t4, d_1, bpme_2806_sa3, d_2, qa_2806_sa3, d_3, bpme_2812_sa3, 
d_2, qa_2812_sa3, d_5, cax_2813_sa3, cay_2813_sa3, d_6, u68_2815_sa3, d_7, 
cbx_2818_sa3, cby_2818_sa3, d_8, bpme_2818_sa3, d_2, qa_2818_sa3, d_5, cax_2819_sa3, 
cay_2819_sa3, d_6, u68_2821_sa3, d_7, cbx_2824_sa3, cby_2824_sa3, d_8, bpme_2824_sa3, 
d_2, qa_2824_sa3, d_5, cax_2825_sa3, cay_2825_sa3, d_6, u68_2827_sa3, d_7, 
cbx_2830_sa3, cby_2830_sa3, d_8, bpme_2830_sa3, d_2, qa_2831_sa3, d_5, cax_2831_sa3, 
cay_2831_sa3, d_6, u68_2834_sa3, d_7, cbx_2836_sa3, cby_2836_sa3, d_8, bpme_2836_sa3, 
d_2, qa_2837_sa3, d_5, cax_2838_sa3, cay_2838_sa3, d_6, u68_2840_sa3, d_7, 
cbx_2842_sa3, cby_2842_sa3, d_8, bpme_2842_sa3, d_2, qa_2843_sa3, d_5, cax_2844_sa3, 
cay_2844_sa3, d_6, u68_2846_sa3, d_7, cbx_2848_sa3, cby_2848_sa3, d_8, bpme_2849_sa3, 
d_2, qa_2849_sa3, d_5, cax_2850_sa3, cay_2850_sa3, d_6, u68_2852_sa3, d_7, 
cbx_2854_sa3, cby_2854_sa3, d_8, bpme_2855_sa3, d_2, qa_2855_sa3, d_5, cax_2856_sa3, 
cay_2856_sa3, d_6, u68_2858_sa3, d_7, cbx_2860_sa3, cby_2860_sa3, d_8, bpme_2861_sa3, 
d_2, qa_2861_sa3, d_5, cax_2862_sa3, cay_2862_sa3, d_6, u68_2864_sa3, d_7, 
cbx_2867_sa3, cby_2867_sa3, d_8, bpme_2867_sa3, d_2, qa_2867_sa3, d_5, cax_2868_sa3, 
cay_2868_sa3, d_6, u68_2870_sa3, d_7, cbx_2873_sa3, cby_2873_sa3, d_8, bpme_2873_sa3, 
d_2, qa_2873_sa3, d_5, cax_2874_sa3, cay_2874_sa3, d_6, u68_2876_sa3, d_7, 
cbx_2879_sa3, cby_2879_sa3, d_8, bpme_2879_sa3, d_2, qa_2879_sa3, d_5, cax_2880_sa3, 
cay_2880_sa3, d_6, u68_2882_sa3, d_7, cbx_2885_sa3, cby_2885_sa3, d_8, bpme_2885_sa3, 
d_2, qa_2885_sa3, d_5, cax_2886_sa3, cay_2886_sa3, d_6, u68_2888_sa3, d_7, 
cbx_2891_sa3, cby_2891_sa3, d_8, bpme_2891_sa3, d_2, qa_2892_sa3, d_5, cax_2892_sa3, 
cay_2892_sa3, d_6, u68_2894_sa3, d_7, cbx_2897_sa3, cby_2897_sa3, d_8, bpme_2897_sa3, 
d_2, qa_2898_sa3, d_5, cax_2899_sa3, cay_2899_sa3, d_6, u68_2901_sa3, d_7, 
cbx_2903_sa3, cby_2903_sa3, d_8, bpme_2903_sa3, d_2, qa_2904_sa3, d_5, cax_2905_sa3, 
cay_2905_sa3, d_6, u68_2907_sa3, d_7, cbx_2909_sa3, cby_2909_sa3, d_8, bpme_2910_sa3, 
d_2, qa_2910_sa3, d_5, cax_2911_sa3, cay_2911_sa3, d_6, u68_2913_sa3, d_7, 
cbx_2915_sa3, cby_2915_sa3, d_8, bpme_2916_sa3, d_2, qa_2916_sa3, d_5, cax_2917_sa3, 
cay_2917_sa3, d_6, u68_2919_sa3, d_7, cbx_2921_sa3, cby_2921_sa3, d_8, bpme_2922_sa3, 
d_2, qa_2922_sa3, d_5, cax_2923_sa3, cay_2923_sa3, d_6, u68_2925_sa3, d_7, 
cbx_2928_sa3, cby_2928_sa3, d_8, bpme_2928_sa3, d_2, qa_2928_sa3, d_5, cax_2929_sa3, 
cay_2929_sa3, d_6, u68_2931_sa3, d_7, cbx_2934_sa3, cby_2934_sa3, d_8, bpme_2934_sa3, 
d_2, qa_2934_sa3, d_5, cax_2935_sa3, cay_2935_sa3, d_6, u68_2937_sa3, d_7, 
cbx_2940_sa3, cby_2940_sa3, d_8, bpme_2940_sa3, d_2, qa_2940_sa3, d_110, ensec_2940_sa3)
# power supplies 

#  
qa_2806_sa3.ps_id = 'QA.1.SA3'
qa_2812_sa3.ps_id = 'QA.2.SA3'
qa_2818_sa3.ps_id = 'QA.1.SA3'
qa_2824_sa3.ps_id = 'QA.2.SA3'
qa_2831_sa3.ps_id = 'QA.1.SA3'
qa_2837_sa3.ps_id = 'QA.2.SA3'
qa_2843_sa3.ps_id = 'QA.1.SA3'
qa_2849_sa3.ps_id = 'QA.2.SA3'
qa_2855_sa3.ps_id = 'QA.1.SA3'
qa_2861_sa3.ps_id = 'QA.2.SA3'
qa_2867_sa3.ps_id = 'QA.1.SA3'
qa_2873_sa3.ps_id = 'QA.2.SA3'
qa_2879_sa3.ps_id = 'QA.1.SA3'
qa_2885_sa3.ps_id = 'QA.2.SA3'
qa_2892_sa3.ps_id = 'QA.1.SA3'
qa_2898_sa3.ps_id = 'QA.2.SA3'
qa_2904_sa3.ps_id = 'QA.1.SA3'
qa_2910_sa3.ps_id = 'QA.2.SA3'
qa_2916_sa3.ps_id = 'QA.1.SA3'
qa_2922_sa3.ps_id = 'QA.2.SA3'
qa_2928_sa3.ps_id = 'QA.1.SA3'
qa_2934_sa3.ps_id = 'QA.2.SA3'
qa_2940_sa3.ps_id = 'QA.1.SA3'

#  

#  

#  

#  
