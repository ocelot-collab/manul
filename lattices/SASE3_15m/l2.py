from ocelot import * 
tws = Twiss()
tws.beta_x  = 7.48319123649
tws.beta_y  = 8.79758475319
tws.alpha_x = -0.721071482665
tws.alpha_y = -1.31392272539
tws.E = 0.7
# drifts 
d_1 = Drift(l=2.734396, eid='D_1')
d_2 = Drift(l=0.11165, eid='D_2')
d_3 = Drift(l=0.15, eid='D_3')
d_4 = Drift(l=0.15165, eid='D_4')
d_5 = Drift(l=0.12165, eid='D_5')
d_7 = Drift(l=0.14165, eid='D_7')
d_8 = Drift(l=5.11825, eid='D_8')
d_9 = Drift(l=0.3459, eid='D_9')
d_16 = Drift(l=0.2475, eid='D_16')
d_17 = Drift(l=0.0432, eid='D_17')
d_18 = Drift(l=0.085, eid='D_18')
d_19 = Drift(l=0.6795, eid='D_19')
d_140 = Drift(l=5.25378, eid='D_140')
d_141 = Drift(l=0.248, eid='D_141')
d_142 = Drift(l=0.15277, eid='D_142')
d_143 = Drift(l=0.13165, eid='D_143')
d_144 = Drift(l=0.62763, eid='D_144')
d_145 = Drift(l=0.13567, eid='D_145')
d_146 = Drift(l=1.77888, eid='D_146')
d_148 = Drift(l=0.10065, eid='D_148')
d_149 = Drift(l=0.56265, eid='D_149')
d_150 = Drift(l=0.08163, eid='D_150')
d_151 = Drift(l=0.3439, eid='D_151')
d_152 = Drift(l=0.4465, eid='D_152')
d_153 = Drift(l=0.559693, eid='D_153')
d_154 = Drift(l=8.507518, eid='D_154')
d_155 = Drift(l=0.865072, eid='D_155')
d_156 = Drift(l=0.31, eid='D_156')
d_157 = Drift(l=0.325073, eid='D_157')
d_159 = Drift(l=0.674552, eid='D_159')
d_160 = Drift(l=0.3068, eid='D_160')
d_161 = Drift(l=0.15735, eid='D_161')
d_162 = Drift(l=0.14465, eid='D_162')
d_163 = Drift(l=0.15002, eid='D_163')
d_164 = Drift(l=0.93165, eid='D_164')
d_165 = Drift(l=0.78165, eid='D_165')
d_167 = Drift(l=0.17888, eid='D_167')
d_170 = Drift(l=6.39998, eid='D_170')
d_171 = Drift(l=0.17165, eid='D_171')
d_172 = Drift(l=0.19165, eid='D_172')
d_173 = Drift(l=0.3899, eid='D_173')
d_174 = Drift(l=0.247, eid='D_174')
d_175 = Drift(l=0.43477, eid='D_175')
d_176 = Drift(l=0.38593, eid='D_176')
d_177 = Drift(l=0.4, eid='D_177')
d_178 = Drift(l=0.17835, eid='D_178')
d_179 = Drift(l=0.09065, eid='D_179')
d_180 = Drift(l=0.3223, eid='D_180')
d_181 = Drift(l=1.90937, eid='D_181')
d_183 = Drift(l=2.23165, eid='D_183')
d_184 = Drift(l=1.78153, eid='D_184')
d_185 = Drift(l=1.629, eid='D_185')
d_188 = Drift(l=3.17888, eid='D_188')
d_191 = Drift(l=0.90012, eid='D_191')
d_192 = Drift(l=0.62888, eid='D_192')
d_195 = Drift(l=1.54988, eid='D_195')
d_196 = Drift(l=1.655, eid='D_196')
d_197 = Drift(l=0.15285, eid='D_197')
d_198 = Drift(l=1.75545, eid='D_198')
d_199 = Drift(l=0.3501, eid='D_199')
d_200 = Drift(l=1.1789, eid='D_200')
d_208 = Drift(l=1.079, eid='D_208')
d_209 = Drift(l=0.15275, eid='D_209')
d_210 = Drift(l=0.83167, eid='D_210')
d_211 = Drift(l=0.33165, eid='D_211')
d_213 = Drift(l=0.35, eid='D_213')
d_216 = Drift(l=0.53165, eid='D_216')

# quadrupoles 
qd_231_b1 = Quadrupole(l=0.2367, k1=1.655730773, tilt=0.0, eid='QD.231.B1')
qd_232_b1 = Quadrupole(l=0.2367, k1=-1.250171811, tilt=0.0, eid='QD.232.B1')
qd_233_b1 = Quadrupole(l=0.2367, k1=-0.4397248283, tilt=0.0, eid='QD.233.B1')
q_249_l2 = Quadrupole(l=0.2136, k1=0.4249129069, tilt=0.0, eid='Q.249.L2')
q_261_l2 = Quadrupole(l=0.2136, k1=-0.3938485271, tilt=0.0, eid='Q.261.L2')
q_273_l2 = Quadrupole(l=0.2136, k1=0.3877757319, tilt=0.0, eid='Q.273.L2')
q_285_l2 = Quadrupole(l=0.2136, k1=-0.424753737, tilt=0.0, eid='Q.285.L2')
q_297_l2 = Quadrupole(l=0.2136, k1=0.4881898114, tilt=0.0, eid='Q.297.L2')
q_309_l2 = Quadrupole(l=0.2136, k1=-0.605809757, tilt=0.0, eid='Q.309.L2')
q_321_l2 = Quadrupole(l=0.2136, k1=0.4881898114, tilt=0.0, eid='Q.321.L2')
q_333_l2 = Quadrupole(l=0.2136, k1=-0.605809757, tilt=0.0, eid='Q.333.L2')
q_345_l2 = Quadrupole(l=0.2136, k1=0.6525829807, tilt=0.0, eid='Q.345.L2')
q_357_l2 = Quadrupole(l=0.2136, k1=-0.3890854168, tilt=0.0, eid='Q.357.L2')
q_369_l2 = Quadrupole(l=0.2136, k1=0.431283982, tilt=0.0, eid='Q.369.L2')
q_381_l2 = Quadrupole(l=0.2136, k1=-0.3839148875, tilt=0.0, eid='Q.381.L2')
qd_387_b2 = Quadrupole(l=0.2367, k1=0.3351733848, tilt=0.0, eid='QD.387.B2')
qd_388_b2 = Quadrupole(l=0.2367, k1=0.3559964322, tilt=0.0, eid='QD.388.B2')
qd_391_b2 = Quadrupole(l=0.2367, k1=-0.7255245526, tilt=0.0, eid='QD.391.B2')
qd_392_b2 = Quadrupole(l=0.2367, k1=0.1969960906, tilt=0.0, eid='QD.392.B2')
qd_415_b2 = Quadrupole(l=0.2367, k1=0.1717108241, tilt=0.0, eid='QD.415.B2')
qd_417_b2 = Quadrupole(l=0.2367, k1=-0.7224091405, tilt=0.0, eid='QD.417.B2')
qd_418_b2 = Quadrupole(l=0.2367, k1=0.6215463712, tilt=0.0, eid='QD.418.B2')
qd_425_b2 = Quadrupole(l=0.2367, k1=-1.29933836, tilt=0.0, eid='QD.425.B2')
qd_427_b2 = Quadrupole(l=0.2367, k1=0.9419328867, tilt=0.0, eid='QD.427.B2')
qd_431_b2 = Quadrupole(l=0.2367, k1=0.4351830275, tilt=0.0, eid='QD.431.B2')
qd_434_b2 = Quadrupole(l=0.2367, k1=-0.527858191, tilt=0.0, eid='QD.434.B2')
qd_437_b2 = Quadrupole(l=0.2367, k1=0.4055492835, tilt=0.0, eid='QD.437.B2')
qd_440_b2 = Quadrupole(l=0.2367, k1=-0.668524672, tilt=0.0, eid='QD.440.B2')
qd_444_b2 = Quadrupole(l=0.2367, k1=-0.4582186615, tilt=0.0, eid='QD.444.B2')
qd_448_b2 = Quadrupole(l=0.2367, k1=0.896095549, tilt=0.0, eid='QD.448.B2')
qd_452_b2 = Quadrupole(l=0.2367, k1=-1.263284384, tilt=0.0, eid='QD.452.B2')
qd_456_b2 = Quadrupole(l=0.2367, k1=0.896095549, tilt=0.0, eid='QD.456.B2')
qd_459_b2 = Quadrupole(l=0.2367, k1=-1.263284384, tilt=0.0, eid='QD.459.B2')
qd_463_b2 = Quadrupole(l=0.2367, k1=-0.5696070976, tilt=0.0, eid='QD.463.B2')
qd_464_b2 = Quadrupole(l=0.2367, k1=1.29826785, tilt=0.0, eid='QD.464.B2')
qd_465_b2 = Quadrupole(l=0.2367, k1=-0.2468610055, tilt=0.0, eid='QD.465.B2')

# bending magnets 
bb_393_b2 = SBend(l=0.5, angle=0.0336848546, e1=0.0, e2=0.0336848546, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BB.393.B2')
bb_402_b2 = SBend(l=0.5, angle=-0.0336848546, e1=-0.0336848546, e2=0.0, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BB.402.B2')
bb_404_b2 = SBend(l=0.5, angle=-0.0336848546, e1=0.0, e2=-0.0336848546, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BB.404.B2')
bb_413_b2 = SBend(l=0.5, angle=0.0336848546, e1=0.0336848546, e2=0.0, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BB.413.B2')

# correctors 
ccx_232_b1 = Hcor(l=0.1, angle=0.0, eid='CCX.232.B1')
ccy_232_b1 = Vcor(l=0.1, angle=0.0, eid='CCY.232.B1')
cx_249_l2 = Hcor(l=0.0, angle=0.0, eid='CX.249.L2')
cy_261_l2 = Vcor(l=0.0, angle=0.0, eid='CY.261.L2')
cx_273_l2 = Hcor(l=0.0, angle=0.0, eid='CX.273.L2')
cy_285_l2 = Vcor(l=0.0, angle=0.0, eid='CY.285.L2')
cx_297_l2 = Hcor(l=0.0, angle=0.0, eid='CX.297.L2')
cy_309_l2 = Vcor(l=0.0, angle=0.0, eid='CY.309.L2')
cx_321_l2 = Hcor(l=0.0, angle=0.0, eid='CX.321.L2')
cy_333_l2 = Vcor(l=0.0, angle=0.0, eid='CY.333.L2')
cx_345_l2 = Hcor(l=0.0, angle=0.0, eid='CX.345.L2')
cy_357_l2 = Vcor(l=0.0, angle=0.0, eid='CY.357.L2')
cx_369_l2 = Hcor(l=0.0, angle=0.0, eid='CX.369.L2')
cy_381_l2 = Vcor(l=0.0, angle=0.0, eid='CY.381.L2')
ccy_387_b2 = Vcor(l=0.1, angle=0.0, eid='CCY.387.B2')
ccx_388_b2 = Hcor(l=0.1, angle=0.0, eid='CCX.388.B2')
ccy_391_b2 = Vcor(l=0.1, angle=0.0, eid='CCY.391.B2')
ccx_392_b2 = Hcor(l=0.1, angle=0.0, eid='CCX.392.B2')
ccx_415_b2 = Hcor(l=0.1, angle=0.0, eid='CCX.415.B2')
ccy_416_b2 = Vcor(l=0.1, angle=0.0, eid='CCY.416.B2')
ccx_418_b2 = Hcor(l=0.1, angle=0.0, eid='CCX.418.B2')
ccy_418_b2 = Vcor(l=0.1, angle=0.0, eid='CCY.418.B2')
ccx_425_b2 = Hcor(l=0.1, angle=0.0, eid='CCX.425.B2')
ccy_426_b2 = Vcor(l=0.1, angle=0.0, eid='CCY.426.B2')
ccx_431_b2 = Hcor(l=0.1, angle=0.0, eid='CCX.431.B2')
ccy_434_b2 = Vcor(l=0.1, angle=0.0, eid='CCY.434.B2')
ccx_441_b2 = Hcor(l=0.1, angle=0.0, eid='CCX.441.B2')
ccx_447_b2 = Hcor(l=0.1, angle=0.0, eid='CCX.447.B2')
ccy_448_b2 = Vcor(l=0.1, angle=0.0, eid='CCY.448.B2')
ccx_454_b2 = Hcor(l=0.1, angle=0.0, eid='CCX.454.B2')
ccx_456_b2 = Hcor(l=0.1, angle=0.0, eid='CCX.456.B2')
ccy_460_b2 = Vcor(l=0.1, angle=0.0, eid='CCY.460.B2')
ccx_464_b2 = Hcor(l=0.1, angle=0.0, eid='CCX.464.B2')
ccy_464_b2 = Vcor(l=0.1, angle=0.0, eid='CCY.464.B2')
ccx_465_b2 = Hcor(l=0.1, angle=0.0, eid='CCX.465.B2')

# markers 
stsub_229_b1 = Marker(eid='STSUB.229.B1')
tora_232_b1 = Marker(eid='TORA.232.B1')
tora_387_b2 = Marker(eid='TORA.387.B2')
otra_392_b2 = Marker(eid='OTRA.392.B2')
otrs_404_b2 = Marker(eid='OTRS.404.B2')
tora_415_b2 = Marker(eid='TORA.415.B2')
engrd_419_b2 = Marker(eid='ENGRD.419.B2')
otra_426_b2 = Marker(eid='OTRA.426.B2')
otra_438_b2 = Marker(eid='OTRA.438.B2')
otra_446_b2 = Marker(eid='OTRA.446.B2')
otrb_450_b2 = Marker(eid='OTRB.450.B2')
otrb_454_b2 = Marker(eid='OTRB.454.B2')
otrb_457_b2 = Marker(eid='OTRB.457.B2')
otrb_461_b2 = Marker(eid='OTRB.461.B2')
ensub_466_b2 = Marker(eid='ENSUB.466.B2')

# monitor 
bpma_233_b1 = Monitor(eid='BPMA.233.B1')
bpmc_249_l2 = Monitor(eid='BPMC.249.L2')
bpmc_261_l2 = Monitor(eid='BPMC.261.L2')
bpmr_273_l2 = Monitor(eid='BPMR.273.L2')
bpmr_285_l2 = Monitor(eid='BPMR.285.L2')
bpmc_297_l2 = Monitor(eid='BPMC.297.L2')
bpmr_309_l2 = Monitor(eid='BPMR.309.L2')
bpmc_321_l2 = Monitor(eid='BPMC.321.L2')
bpmr_333_l2 = Monitor(eid='BPMR.333.L2')
bpmc_345_l2 = Monitor(eid='BPMC.345.L2')
bpmc_357_l2 = Monitor(eid='BPMC.357.L2')
bpmr_369_l2 = Monitor(eid='BPMR.369.L2')
bpmr_381_l2 = Monitor(eid='BPMR.381.L2')
bpma_387_b2 = Monitor(eid='BPMA.387.B2')
bpma_390_b2 = Monitor(eid='BPMA.390.B2')
bpmf_393_b2 = Monitor(eid='BPMF.393.B2')
bpms_404_b2 = Monitor(eid='BPMS.404.B2')
bpmf_414_b2 = Monitor(eid='BPMF.414.B2')
bpma_418_b2 = Monitor(eid='BPMA.418.B2')
bpma_426_b2 = Monitor(eid='BPMA.426.B2')
bpma_432_b2 = Monitor(eid='BPMA.432.B2')
bpma_440_b2 = Monitor(eid='BPMA.440.B2')
bpma_444_b2 = Monitor(eid='BPMA.444.B2')
bpma_448_b2 = Monitor(eid='BPMA.448.B2')
bpma_452_b2 = Monitor(eid='BPMA.452.B2')
bpma_455_b2 = Monitor(eid='BPMA.455.B2')
bpma_459_b2 = Monitor(eid='BPMA.459.B2')
bpma_462_b2 = Monitor(eid='BPMA.462.B2')
bpma_465_b2 = Monitor(eid='BPMA.465.B2')

# sextupoles 

# octupole 

# undulator 

# cavity 
c_a3_1_1_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.1.1.L2')
c_a3_1_2_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.1.2.L2')
c_a3_1_3_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.1.3.L2')
c_a3_1_4_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.1.4.L2')
c_a3_1_5_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.1.5.L2')
c_a3_1_6_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.1.6.L2')
c_a3_1_7_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.1.7.L2')
c_a3_1_8_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.1.8.L2')
c_a3_2_1_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.2.1.L2')
c_a3_2_2_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.2.2.L2')
c_a3_2_3_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.2.3.L2')
c_a3_2_4_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.2.4.L2')
c_a3_2_5_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.2.5.L2')
c_a3_2_6_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.2.6.L2')
c_a3_2_7_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.2.7.L2')
c_a3_2_8_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.2.8.L2')
c_a3_3_1_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.3.1.L2')
c_a3_3_2_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.3.2.L2')
c_a3_3_3_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.3.3.L2')
c_a3_3_4_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.3.4.L2')
c_a3_3_5_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.3.5.L2')
c_a3_3_6_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.3.6.L2')
c_a3_3_7_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.3.7.L2')
c_a3_3_8_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.3.8.L2')
c_a3_4_1_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.4.1.L2')
c_a3_4_2_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.4.2.L2')
c_a3_4_3_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.4.3.L2')
c_a3_4_4_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.4.4.L2')
c_a3_4_5_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.4.5.L2')
c_a3_4_6_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.4.6.L2')
c_a3_4_7_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.4.7.L2')
c_a3_4_8_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A3.4.8.L2')
c_a4_1_1_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.1.1.L2')
c_a4_1_2_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.1.2.L2')
c_a4_1_3_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.1.3.L2')
c_a4_1_4_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.1.4.L2')
c_a4_1_5_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.1.5.L2')
c_a4_1_6_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.1.6.L2')
c_a4_1_7_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.1.7.L2')
c_a4_1_8_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.1.8.L2')
c_a4_2_1_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.2.1.L2')
c_a4_2_2_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.2.2.L2')
c_a4_2_3_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.2.3.L2')
c_a4_2_4_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.2.4.L2')
c_a4_2_5_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.2.5.L2')
c_a4_2_6_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.2.6.L2')
c_a4_2_7_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.2.7.L2')
c_a4_2_8_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.2.8.L2')
c_a4_3_1_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.3.1.L2')
c_a4_3_2_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.3.2.L2')
c_a4_3_3_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.3.3.L2')
c_a4_3_4_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.3.4.L2')
c_a4_3_5_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.3.5.L2')
c_a4_3_6_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.3.6.L2')
c_a4_3_7_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.3.7.L2')
c_a4_3_8_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.3.8.L2')
c_a4_4_1_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.4.1.L2')
c_a4_4_2_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.4.2.L2')
c_a4_4_3_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.4.3.L2')
c_a4_4_4_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.4.4.L2')
c_a4_4_5_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.4.5.L2')
c_a4_4_6_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.4.6.L2')
c_a4_4_7_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.4.7.L2')
c_a4_4_8_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A4.4.8.L2')
c_a5_1_1_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.1.1.L2')
c_a5_1_2_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.1.2.L2')
c_a5_1_3_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.1.3.L2')
c_a5_1_4_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.1.4.L2')
c_a5_1_5_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.1.5.L2')
c_a5_1_6_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.1.6.L2')
c_a5_1_7_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.1.7.L2')
c_a5_1_8_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.1.8.L2')
c_a5_2_1_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.2.1.L2')
c_a5_2_2_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.2.2.L2')
c_a5_2_3_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.2.3.L2')
c_a5_2_4_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.2.4.L2')
c_a5_2_5_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.2.5.L2')
c_a5_2_6_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.2.6.L2')
c_a5_2_7_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.2.7.L2')
c_a5_2_8_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.2.8.L2')
c_a5_3_1_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.3.1.L2')
c_a5_3_2_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.3.2.L2')
c_a5_3_3_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.3.3.L2')
c_a5_3_4_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.3.4.L2')
c_a5_3_5_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.3.5.L2')
c_a5_3_6_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.3.6.L2')
c_a5_3_7_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.3.7.L2')
c_a5_3_8_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.3.8.L2')
c_a5_4_1_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.4.1.L2')
c_a5_4_2_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.4.2.L2')
c_a5_4_3_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.4.3.L2')
c_a5_4_4_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.4.4.L2')
c_a5_4_5_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.4.5.L2')
c_a5_4_6_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.4.6.L2')
c_a5_4_7_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.4.7.L2')
c_a5_4_8_l2 = Cavity(l=1.0377, v=0.0177083334375, freq=1300000000.0, phi=0.0, eid='C.A5.4.8.L2')
tdsb_428_b2 = Cavity(l=1.5, v=0.0, freq=2997000.0, phi=0.0, eid='TDSB.428.B2')
tdsb_430_b2 = Cavity(l=1.5, v=0.0, freq=2997000.0, phi=0.0, eid='TDSB.430.B2')

# tdcavity 

# UnknowElement 

# Matrices 

# Solenoids 

# lattice 
cell = (stsub_229_b1, d_1, qd_231_b1, d_2, ccx_232_b1, d_3, tora_232_b1, 
d_4, qd_232_b1, d_5, ccy_232_b1, d_3, bpma_233_b1, d_7, qd_233_b1, 
d_8, c_a3_1_1_l2, d_9, c_a3_1_2_l2, d_9, c_a3_1_3_l2, d_9, c_a3_1_4_l2, 
d_9, c_a3_1_5_l2, d_9, c_a3_1_6_l2, d_9, c_a3_1_7_l2, d_9, c_a3_1_8_l2, 
d_16, q_249_l2, d_17, cx_249_l2, d_18, bpmc_249_l2, d_19, c_a3_2_1_l2, 
d_9, c_a3_2_2_l2, d_9, c_a3_2_3_l2, d_9, c_a3_2_4_l2, d_9, c_a3_2_5_l2, 
d_9, c_a3_2_6_l2, d_9, c_a3_2_7_l2, d_9, c_a3_2_8_l2, d_16, q_261_l2, 
d_17, cy_261_l2, d_18, bpmc_261_l2, d_19, c_a3_3_1_l2, d_9, c_a3_3_2_l2, 
d_9, c_a3_3_3_l2, d_9, c_a3_3_4_l2, d_9, c_a3_3_5_l2, d_9, c_a3_3_6_l2, 
d_9, c_a3_3_7_l2, d_9, c_a3_3_8_l2, d_16, q_273_l2, d_17, cx_273_l2, 
d_18, bpmr_273_l2, d_19, c_a3_4_1_l2, d_9, c_a3_4_2_l2, d_9, c_a3_4_3_l2, 
d_9, c_a3_4_4_l2, d_9, c_a3_4_5_l2, d_9, c_a3_4_6_l2, d_9, c_a3_4_7_l2, 
d_9, c_a3_4_8_l2, d_16, q_285_l2, d_17, cy_285_l2, d_18, bpmr_285_l2, 
d_19, c_a4_1_1_l2, d_9, c_a4_1_2_l2, d_9, c_a4_1_3_l2, d_9, c_a4_1_4_l2, 
d_9, c_a4_1_5_l2, d_9, c_a4_1_6_l2, d_9, c_a4_1_7_l2, d_9, c_a4_1_8_l2, 
d_16, q_297_l2, d_17, cx_297_l2, d_18, bpmc_297_l2, d_19, c_a4_2_1_l2, 
d_9, c_a4_2_2_l2, d_9, c_a4_2_3_l2, d_9, c_a4_2_4_l2, d_9, c_a4_2_5_l2, 
d_9, c_a4_2_6_l2, d_9, c_a4_2_7_l2, d_9, c_a4_2_8_l2, d_16, q_309_l2, 
d_17, cy_309_l2, d_18, bpmr_309_l2, d_19, c_a4_3_1_l2, d_9, c_a4_3_2_l2, 
d_9, c_a4_3_3_l2, d_9, c_a4_3_4_l2, d_9, c_a4_3_5_l2, d_9, c_a4_3_6_l2, 
d_9, c_a4_3_7_l2, d_9, c_a4_3_8_l2, d_16, q_321_l2, d_17, cx_321_l2, 
d_18, bpmc_321_l2, d_19, c_a4_4_1_l2, d_9, c_a4_4_2_l2, d_9, c_a4_4_3_l2, 
d_9, c_a4_4_4_l2, d_9, c_a4_4_5_l2, d_9, c_a4_4_6_l2, d_9, c_a4_4_7_l2, 
d_9, c_a4_4_8_l2, d_16, q_333_l2, d_17, cy_333_l2, d_18, bpmr_333_l2, 
d_19, c_a5_1_1_l2, d_9, c_a5_1_2_l2, d_9, c_a5_1_3_l2, d_9, c_a5_1_4_l2, 
d_9, c_a5_1_5_l2, d_9, c_a5_1_6_l2, d_9, c_a5_1_7_l2, d_9, c_a5_1_8_l2, 
d_16, q_345_l2, d_17, cx_345_l2, d_18, bpmc_345_l2, d_19, c_a5_2_1_l2, 
d_9, c_a5_2_2_l2, d_9, c_a5_2_3_l2, d_9, c_a5_2_4_l2, d_9, c_a5_2_5_l2, 
d_9, c_a5_2_6_l2, d_9, c_a5_2_7_l2, d_9, c_a5_2_8_l2, d_16, q_357_l2, 
d_17, cy_357_l2, d_18, bpmc_357_l2, d_19, c_a5_3_1_l2, d_9, c_a5_3_2_l2, 
d_9, c_a5_3_3_l2, d_9, c_a5_3_4_l2, d_9, c_a5_3_5_l2, d_9, c_a5_3_6_l2, 
d_9, c_a5_3_7_l2, d_9, c_a5_3_8_l2, d_16, q_369_l2, d_17, cx_369_l2, 
d_18, bpmr_369_l2, d_19, c_a5_4_1_l2, d_9, c_a5_4_2_l2, d_9, c_a5_4_3_l2, 
d_9, c_a5_4_4_l2, d_9, c_a5_4_5_l2, d_9, c_a5_4_6_l2, d_9, c_a5_4_7_l2, 
d_9, c_a5_4_8_l2, d_16, q_381_l2, d_17, cy_381_l2, d_18, bpmr_381_l2, 
d_140, tora_387_b2, d_141, bpma_387_b2, d_142, qd_387_b2, d_143, ccy_387_b2, 
d_144, qd_388_b2, d_145, ccx_388_b2, d_146, bpma_390_b2, d_142, qd_391_b2, 
d_148, ccy_391_b2, d_149, qd_392_b2, d_150, ccx_392_b2, d_151, otra_392_b2, 
d_152, bpmf_393_b2, d_153, bb_393_b2, d_154, bb_402_b2, d_155, bpms_404_b2, 
d_156, otrs_404_b2, d_157, bb_404_b2, d_154, bb_413_b2, d_159, bpmf_414_b2, 
d_160, tora_415_b2, d_161, qd_415_b2, d_162, ccx_415_b2, d_163, ccy_416_b2, 
d_164, qd_417_b2, d_165, ccx_418_b2, d_3, ccy_418_b2, d_167, bpma_418_b2, 
d_142, qd_418_b2, d_143, engrd_419_b2, d_170, ccx_425_b2, d_171, qd_425_b2, 
d_172, ccy_426_b2, d_173, otra_426_b2, d_174, bpma_426_b2, d_175, qd_427_b2, 
d_176, tdsb_428_b2, d_177, tdsb_430_b2, d_178, qd_431_b2, d_179, ccx_431_b2, 
d_180, bpma_432_b2, d_181, qd_434_b2, d_143, ccy_434_b2, d_183, qd_437_b2, 
d_184, otra_438_b2, d_185, bpma_440_b2, d_142, qd_440_b2, d_143, ccx_441_b2, 
d_188, bpma_444_b2, d_142, qd_444_b2, d_184, otra_446_b2, d_191, ccx_447_b2, 
d_192, bpma_448_b2, d_142, qd_448_b2, d_143, ccy_448_b2, d_195, otrb_450_b2, 
d_196, bpma_452_b2, d_197, qd_452_b2, d_198, otrb_454_b2, d_199, ccx_454_b2, 
d_200, bpma_455_b2, d_142, qd_456_b2, d_143, ccx_456_b2, d_195, otrb_457_b2, 
d_185, bpma_459_b2, d_142, qd_459_b2, d_143, ccy_460_b2, d_195, otrb_461_b2, 
d_208, bpma_462_b2, d_209, qd_463_b2, d_210, ccx_464_b2, d_211, qd_464_b2, 
d_143, ccy_464_b2, d_213, ccx_465_b2, d_167, bpma_465_b2, d_142, qd_465_b2, 
d_216, ensub_466_b2)
# power supplies 

#  
qd_231_b1.ps_id = 'QD.20.B1'
qd_232_b1.ps_id = 'QD.21.B1'
qd_233_b1.ps_id = 'QD.22.B1'
q_249_l2.ps_id = 'Q.A3.1.L2'
q_261_l2.ps_id = 'Q.A3.2.L2'
q_273_l2.ps_id = 'Q.A3.3.L2'
q_285_l2.ps_id = 'Q.A3.4.L2'
q_297_l2.ps_id = 'Q.A4.1.L2'
q_309_l2.ps_id = 'Q.A4.2.L2'
q_321_l2.ps_id = 'Q.A4.3.L2'
q_333_l2.ps_id = 'Q.A4.4.L2'
q_345_l2.ps_id = 'Q.A5.1.L2'
q_357_l2.ps_id = 'Q.A5.2.L2'
q_369_l2.ps_id = 'Q.A5.3.L2'
q_381_l2.ps_id = 'Q.A5.4.L2'
qd_387_b2.ps_id = 'QD.1.B2'
qd_388_b2.ps_id = 'QD.2.B2'
qd_391_b2.ps_id = 'QD.3.B2'
qd_392_b2.ps_id = 'QD.4.B2'
qd_415_b2.ps_id = 'QD.6.B2'
qd_417_b2.ps_id = 'QD.7.B2'
qd_418_b2.ps_id = 'QD.8.B2'
qd_425_b2.ps_id = 'QD.9.B2'
qd_427_b2.ps_id = 'QD.10.B2'
qd_431_b2.ps_id = 'QD.11.B2'
qd_434_b2.ps_id = 'QD.12.B2'
qd_437_b2.ps_id = 'QD.13.B2'
qd_440_b2.ps_id = 'QD.14.B2'
qd_444_b2.ps_id = 'QD.15.B2'
qd_448_b2.ps_id = 'QD.16.B2'
qd_452_b2.ps_id = 'QD.17.B2'
qd_456_b2.ps_id = 'QD.18.B2'
qd_459_b2.ps_id = 'QD.19.B2'
qd_463_b2.ps_id = 'QD.21.B2'
qd_464_b2.ps_id = 'QD.22.B2'
qd_465_b2.ps_id = 'QD.23.B2'

#  

#  

#  
c_a3_1_1_l2.ps_id = 'C.A3.L2'
c_a3_1_2_l2.ps_id = 'C.A3.L2'
c_a3_1_3_l2.ps_id = 'C.A3.L2'
c_a3_1_4_l2.ps_id = 'C.A3.L2'
c_a3_1_5_l2.ps_id = 'C.A3.L2'
c_a3_1_6_l2.ps_id = 'C.A3.L2'
c_a3_1_7_l2.ps_id = 'C.A3.L2'
c_a3_1_8_l2.ps_id = 'C.A3.L2'
c_a3_2_1_l2.ps_id = 'C.A3.L2'
c_a3_2_2_l2.ps_id = 'C.A3.L2'
c_a3_2_3_l2.ps_id = 'C.A3.L2'
c_a3_2_4_l2.ps_id = 'C.A3.L2'
c_a3_2_5_l2.ps_id = 'C.A3.L2'
c_a3_2_6_l2.ps_id = 'C.A3.L2'
c_a3_2_7_l2.ps_id = 'C.A3.L2'
c_a3_2_8_l2.ps_id = 'C.A3.L2'
c_a3_3_1_l2.ps_id = 'C.A3.L2'
c_a3_3_2_l2.ps_id = 'C.A3.L2'
c_a3_3_3_l2.ps_id = 'C.A3.L2'
c_a3_3_4_l2.ps_id = 'C.A3.L2'
c_a3_3_5_l2.ps_id = 'C.A3.L2'
c_a3_3_6_l2.ps_id = 'C.A3.L2'
c_a3_3_7_l2.ps_id = 'C.A3.L2'
c_a3_3_8_l2.ps_id = 'C.A3.L2'
c_a3_4_1_l2.ps_id = 'C.A3.L2'
c_a3_4_2_l2.ps_id = 'C.A3.L2'
c_a3_4_3_l2.ps_id = 'C.A3.L2'
c_a3_4_4_l2.ps_id = 'C.A3.L2'
c_a3_4_5_l2.ps_id = 'C.A3.L2'
c_a3_4_6_l2.ps_id = 'C.A3.L2'
c_a3_4_7_l2.ps_id = 'C.A3.L2'
c_a3_4_8_l2.ps_id = 'C.A3.L2'
c_a4_1_1_l2.ps_id = 'C.A4.L2'
c_a4_1_2_l2.ps_id = 'C.A4.L2'
c_a4_1_3_l2.ps_id = 'C.A4.L2'
c_a4_1_4_l2.ps_id = 'C.A4.L2'
c_a4_1_5_l2.ps_id = 'C.A4.L2'
c_a4_1_6_l2.ps_id = 'C.A4.L2'
c_a4_1_7_l2.ps_id = 'C.A4.L2'
c_a4_1_8_l2.ps_id = 'C.A4.L2'
c_a4_2_1_l2.ps_id = 'C.A4.L2'
c_a4_2_2_l2.ps_id = 'C.A4.L2'
c_a4_2_3_l2.ps_id = 'C.A4.L2'
c_a4_2_4_l2.ps_id = 'C.A4.L2'
c_a4_2_5_l2.ps_id = 'C.A4.L2'
c_a4_2_6_l2.ps_id = 'C.A4.L2'
c_a4_2_7_l2.ps_id = 'C.A4.L2'
c_a4_2_8_l2.ps_id = 'C.A4.L2'
c_a4_3_1_l2.ps_id = 'C.A4.L2'
c_a4_3_2_l2.ps_id = 'C.A4.L2'
c_a4_3_3_l2.ps_id = 'C.A4.L2'
c_a4_3_4_l2.ps_id = 'C.A4.L2'
c_a4_3_5_l2.ps_id = 'C.A4.L2'
c_a4_3_6_l2.ps_id = 'C.A4.L2'
c_a4_3_7_l2.ps_id = 'C.A4.L2'
c_a4_3_8_l2.ps_id = 'C.A4.L2'
c_a4_4_1_l2.ps_id = 'C.A4.L2'
c_a4_4_2_l2.ps_id = 'C.A4.L2'
c_a4_4_3_l2.ps_id = 'C.A4.L2'
c_a4_4_4_l2.ps_id = 'C.A4.L2'
c_a4_4_5_l2.ps_id = 'C.A4.L2'
c_a4_4_6_l2.ps_id = 'C.A4.L2'
c_a4_4_7_l2.ps_id = 'C.A4.L2'
c_a4_4_8_l2.ps_id = 'C.A4.L2'
c_a5_1_1_l2.ps_id = 'C.A5.L2'
c_a5_1_2_l2.ps_id = 'C.A5.L2'
c_a5_1_3_l2.ps_id = 'C.A5.L2'
c_a5_1_4_l2.ps_id = 'C.A5.L2'
c_a5_1_5_l2.ps_id = 'C.A5.L2'
c_a5_1_6_l2.ps_id = 'C.A5.L2'
c_a5_1_7_l2.ps_id = 'C.A5.L2'
c_a5_1_8_l2.ps_id = 'C.A5.L2'
c_a5_2_1_l2.ps_id = 'C.A5.L2'
c_a5_2_2_l2.ps_id = 'C.A5.L2'
c_a5_2_3_l2.ps_id = 'C.A5.L2'
c_a5_2_4_l2.ps_id = 'C.A5.L2'
c_a5_2_5_l2.ps_id = 'C.A5.L2'
c_a5_2_6_l2.ps_id = 'C.A5.L2'
c_a5_2_7_l2.ps_id = 'C.A5.L2'
c_a5_2_8_l2.ps_id = 'C.A5.L2'
c_a5_3_1_l2.ps_id = 'C.A5.L2'
c_a5_3_2_l2.ps_id = 'C.A5.L2'
c_a5_3_3_l2.ps_id = 'C.A5.L2'
c_a5_3_4_l2.ps_id = 'C.A5.L2'
c_a5_3_5_l2.ps_id = 'C.A5.L2'
c_a5_3_6_l2.ps_id = 'C.A5.L2'
c_a5_3_7_l2.ps_id = 'C.A5.L2'
c_a5_3_8_l2.ps_id = 'C.A5.L2'
c_a5_4_1_l2.ps_id = 'C.A5.L2'
c_a5_4_2_l2.ps_id = 'C.A5.L2'
c_a5_4_3_l2.ps_id = 'C.A5.L2'
c_a5_4_4_l2.ps_id = 'C.A5.L2'
c_a5_4_5_l2.ps_id = 'C.A5.L2'
c_a5_4_6_l2.ps_id = 'C.A5.L2'
c_a5_4_7_l2.ps_id = 'C.A5.L2'
c_a5_4_8_l2.ps_id = 'C.A5.L2'

#  
bb_393_b2.ps_id = 'BB.1.B2'
bb_402_b2.ps_id = 'BB.1.B2'
bb_404_b2.ps_id = 'BB.1.B2'
bb_413_b2.ps_id = 'BB.1.B2'
