from ocelot import * 
tws = Twiss()
tws.beta_x  = 7.47960745573
tws.beta_y  = 8.62195025642
tws.alpha_x = -0.726528847426
tws.alpha_y = -1.27890295717
tws.E       = 0.6999999892
# drifts 
d_1 = Drift(l=2.702746, eid='D_1')
d_2 = Drift(l=0.03165, eid='D_2')
d_3 = Drift(l=0.11165, eid='D_3')
d_4 = Drift(l=0.15, eid='D_4')
d_5 = Drift(l=0.15165, eid='D_5')
d_6 = Drift(l=0.12165, eid='D_6')
d_8 = Drift(l=0.14165, eid='D_8')
d_9 = Drift(l=0.13165, eid='D_9')
d_10 = Drift(l=1.415, eid='D_10')
d_11 = Drift(l=3.35, eid='D_11')
d_12 = Drift(l=0.2216, eid='D_12')
d_13 = Drift(l=0.3459, eid='D_13')
d_20 = Drift(l=0.2475, eid='D_20')
d_21 = Drift(l=0.0432, eid='D_21')
d_22 = Drift(l=0.085, eid='D_22')
d_23 = Drift(l=0.4579, eid='D_23')
d_156 = Drift(l=3.25, eid='D_156')
d_158 = Drift(l=0.13088, eid='D_158')
d_159 = Drift(l=0.248, eid='D_159')
d_160 = Drift(l=0.15277, eid='D_160')
d_162 = Drift(l=0.30008, eid='D_162')
d_163 = Drift(l=0.32755, eid='D_163')
d_164 = Drift(l=0.13567, eid='D_164')
d_165 = Drift(l=1.05, eid='D_165')
d_166 = Drift(l=0.1, eid='D_166')
d_167 = Drift(l=0.28888, eid='D_167')
d_168 = Drift(l=0.34, eid='D_168')
d_170 = Drift(l=0.10065, eid='D_170')
d_171 = Drift(l=0.29188, eid='D_171')
d_172 = Drift(l=0.27077, eid='D_172')
d_173 = Drift(l=0.08163, eid='D_173')
d_174 = Drift(l=0.3439, eid='D_174')
d_175 = Drift(l=0.194, eid='D_175')
d_176 = Drift(l=0.1565, eid='D_176')
d_177 = Drift(l=0.096, eid='D_177')
d_178 = Drift(l=0.15962, eid='D_178')
d_179 = Drift(l=0.3, eid='D_179')
d_180 = Drift(l=0.100073, eid='D_180')
d_181 = Drift(l=8.507518, eid='D_181')
d_182 = Drift(l=7.2e-05, eid='D_182')
d_183 = Drift(l=0.865, eid='D_183')
d_184 = Drift(l=0.31, eid='D_184')
d_185 = Drift(l=0.325073, eid='D_185')
d_187 = Drift(l=1.053189, eid='D_187')
d_188 = Drift(l=7.454257, eid='D_188')
d_191 = Drift(l=0.17, eid='D_191')
d_192 = Drift(l=0.15198, eid='D_192')
d_195 = Drift(l=0.3068, eid='D_195')
d_196 = Drift(l=0.15735, eid='D_196')
d_197 = Drift(l=0.14465, eid='D_197')
d_198 = Drift(l=0.15002, eid='D_198')
d_199 = Drift(l=0.34888, eid='D_199')
d_200 = Drift(l=0.58277, eid='D_200')
d_201 = Drift(l=0.78165, eid='D_201')
d_203 = Drift(l=0.17888, eid='D_203')
d_206 = Drift(l=4.0, eid='D_206')
d_207 = Drift(l=2.39998, eid='D_207')
d_208 = Drift(l=0.17165, eid='D_208')
d_209 = Drift(l=0.19165, eid='D_209')
d_210 = Drift(l=0.3899, eid='D_210')
d_211 = Drift(l=0.247, eid='D_211')
d_212 = Drift(l=0.43477, eid='D_212')
d_213 = Drift(l=0.09165, eid='D_213')
d_214 = Drift(l=0.2, eid='D_214')
d_215 = Drift(l=0.09428, eid='D_215')
d_216 = Drift(l=0.4, eid='D_216')
d_217 = Drift(l=0.1467, eid='D_217')
d_219 = Drift(l=0.09065, eid='D_219')
d_220 = Drift(l=0.3223, eid='D_220')
d_221 = Drift(l=0.17772, eid='D_221')
d_223 = Drift(l=1.53165, eid='D_223')
d_225 = Drift(l=2.23165, eid='D_225')
d_228 = Drift(l=1.44988, eid='D_228')
d_229 = Drift(l=1.629, eid='D_229')
d_232 = Drift(l=0.9, eid='D_232')
d_234 = Drift(l=2.07888, eid='D_234')
d_236 = Drift(l=1.78153, eid='D_236')
d_237 = Drift(l=0.35012, eid='D_237')
d_239 = Drift(l=0.35, eid='D_239')
d_240 = Drift(l=0.62888, eid='D_240')
d_243 = Drift(l=1.54988, eid='D_243')
d_244 = Drift(l=1.35012, eid='D_244')
d_246 = Drift(l=0.10488, eid='D_246')
d_247 = Drift(l=0.15285, eid='D_247')
d_248 = Drift(l=1.75545, eid='D_248')
d_249 = Drift(l=0.3501, eid='D_249')
d_250 = Drift(l=1.1789, eid='D_250')
d_255 = Drift(l=1.24988, eid='D_255')
d_259 = Drift(l=1.1, eid='D_259')
d_261 = Drift(l=0.24988, eid='D_261')
d_262 = Drift(l=1.079, eid='D_262')
d_263 = Drift(l=0.15275, eid='D_263')
d_264 = Drift(l=0.37055, eid='D_264')
d_265 = Drift(l=0.46112, eid='D_265')
d_266 = Drift(l=0.33165, eid='D_266')

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
qd_415_b2 = Quadrupole(l=0.2367, k1=0.169388438, tilt=0.0, eid='QD.415.B2')
qd_417_b2 = Quadrupole(l=0.2367, k1=-0.765663913, tilt=0.0, eid='QD.417.B2')
qd_418_b2 = Quadrupole(l=0.2367, k1=0.6775492967, tilt=0.0, eid='QD.418.B2')
qd_425_b2 = Quadrupole(l=0.2367, k1=-1.303340781, tilt=0.0, eid='QD.425.B2')
qd_427_b2 = Quadrupole(l=0.2367, k1=0.9388347029, tilt=0.0, eid='QD.427.B2')
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
bb_393_b2 = SBend(l = 0.5, angle=0.0455530935, e1=0.0, e2=0.0455530935, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BB.393.B2')
bb_402_b2 = SBend(l = 0.5, angle=-0.0455530935, e1=-0.0455530935, e2=0.0, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BB.402.B2')
bb_404_b2 = SBend(l = 0.5, angle=-0.0455530935, e1=0.0, e2=-0.0455530935, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BB.404.B2')
bb_413_b2 = SBend(l = 0.5, angle=0.0455530935, e1=0.0455530935, e2=0.0, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BB.413.B2')

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

cbb_403_b2 = Drift(eid='CBB.403.B2') # Vcor(l=0.0, angle=0.0, eid='CBB.403.B2')
cbb_405_b2 = Drift(eid='CBB.405.B2') # Vcor(l=0.0, angle=0.0, eid='CBB.405.B2')
cbb_414_b2 = Drift(eid='CBB.414.B2') # Vcor(l=0.0, angle=0.0, eid='CBB.414.B2')

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
stgrd_231_b1 = Marker(eid='STGRD.231.B1')
tora_232_b1 = Marker(eid='TORA.232.B1')
enblock_233_b1 = Marker(eid='ENBLOCK.233.B1')
engrd_233_b1 = Marker(eid='ENGRD.233.B1')
ensub_235_b1 = Marker(eid='ENSUB.235.B1')
ensec_235_b1 = Marker(eid='ENSEC.235.B1')
stsec_235_l2 = Marker(eid='STSEC.235.L2')
stac_238_l2 = Marker(eid='STAC.238.L2')
enac_250_l2 = Marker(eid='ENAC.250.L2')
stac_250_l2 = Marker(eid='STAC.250.L2')
enac_262_l2 = Marker(eid='ENAC.262.L2')
stac_262_l2 = Marker(eid='STAC.262.L2')
enac_274_l2 = Marker(eid='ENAC.274.L2')
stac_274_l2 = Marker(eid='STAC.274.L2')
enac_286_l2 = Marker(eid='ENAC.286.L2')
stac_286_l2 = Marker(eid='STAC.286.L2')
enac_298_l2 = Marker(eid='ENAC.298.L2')
stac_298_l2 = Marker(eid='STAC.298.L2')
enac_310_l2 = Marker(eid='ENAC.310.L2')
mid_310_l2 = Marker(eid='MID.310.L2')
stac_310_l2 = Marker(eid='STAC.310.L2')
enac_322_l2 = Marker(eid='ENAC.322.L2')
stac_322_l2 = Marker(eid='STAC.322.L2')
enac_334_l2 = Marker(eid='ENAC.334.L2')
stac_334_l2 = Marker(eid='STAC.334.L2')
enac_346_l2 = Marker(eid='ENAC.346.L2')
stac_346_l2 = Marker(eid='STAC.346.L2')
enac_358_l2 = Marker(eid='ENAC.358.L2')
stac_358_l2 = Marker(eid='STAC.358.L2')
enac_370_l2 = Marker(eid='ENAC.370.L2')
stac_370_l2 = Marker(eid='STAC.370.L2')
enac_382_l2 = Marker(eid='ENAC.382.L2')
ensec_385_l2 = Marker(eid='ENSEC.385.L2')
stsec_385_b2 = Marker(eid='STSEC.385.B2')
stsub_385_b2 = Marker(eid='STSUB.385.B2')
stgrd_386_b2 = Marker(eid='STGRD.386.B2')
tora_387_b2 = Marker(eid='TORA.387.B2')
dcm_388_b2 = Marker(eid='DCM.388.B2')
engrd_390_b2 = Marker(eid='ENGRD.390.B2')
stgrd_390_b2 = Marker(eid='STGRD.390.B2')
eod_390_b2 = Marker(eid='EOD.390.B2')
bcm_391_b2 = Marker(eid='BCM.391.B2')
otra_392_b2 = Marker(eid='OTRA.392.B2')
bam_392_b2 = Marker(eid='BAM.392.B2')
mpbpmf_393_b2 = Marker(eid='MPBPMF.393.B2')
engrd_393_b2 = Marker(eid='ENGRD.393.B2')
stlat_393_b2 = Marker(eid='STLAT.393.B2')
otrs_404_b2 = Marker(eid='OTRS.404.B2')
srm_406_b2 = Marker(eid='SRM.406.B2')
enlat_414_b2 = Marker(eid='ENLAT.414.B2')
match_414_b2 = Marker(eid='MATCH.414.B2')
stlat_414_b2 = Marker(eid='STLAT.414.B2')
stgrd_414_b2 = Marker(eid='STGRD.414.B2')
bam_414_b2 = Marker(eid='BAM.414.B2')
mpbpmf_414_b2 = Marker(eid='MPBPMF.414.B2')
tora_415_b2 = Marker(eid='TORA.415.B2')
bcm_416_b2 = Marker(eid='BCM.416.B2')
engrd_419_b2 = Marker(eid='ENGRD.419.B2')
stgrd_423_b2 = Marker(eid='STGRD.423.B2')
otra_426_b2 = Marker(eid='OTRA.426.B2')
engrd_427_b2 = Marker(eid='ENGRD.427.B2')
stgrd_427_b2 = Marker(eid='STGRD.427.B2')
match_428_b2 = Marker(eid='MATCH.428.B2')
stblock_431_b2 = Marker(eid='STBLOCK.431.B2')
engrd_432_b2 = Marker(eid='ENGRD.432.B2')
stgrd_432_b2 = Marker(eid='STGRD.432.B2')
engrd_437_b2 = Marker(eid='ENGRD.437.B2')
stgrd_437_b2 = Marker(eid='STGRD.437.B2')
otra_438_b2 = Marker(eid='OTRA.438.B2')
engrd_442_b2 = Marker(eid='ENGRD.442.B2')
stgrd_442_b2 = Marker(eid='STGRD.442.B2')
match_446_b2 = Marker(eid='MATCH.446.B2')
otra_446_b2 = Marker(eid='OTRA.446.B2')
engrd_446_b2 = Marker(eid='ENGRD.446.B2')
stgrd_447_b2 = Marker(eid='STGRD.447.B2')
otrb_450_b2 = Marker(eid='OTRB.450.B2')
engrd_451_b2 = Marker(eid='ENGRD.451.B2')
stgrd_451_b2 = Marker(eid='STGRD.451.B2')
otrb_454_b2 = Marker(eid='OTRB.454.B2')
engrd_456_b2 = Marker(eid='ENGRD.456.B2')
stgrd_456_b2 = Marker(eid='STGRD.456.B2')
otrb_457_b2 = Marker(eid='OTRB.457.B2')
engrd_461_b2 = Marker(eid='ENGRD.461.B2')
stgrd_461_b2 = Marker(eid='STGRD.461.B2')
otrb_461_b2 = Marker(eid='OTRB.461.B2')
crd_463_b2 = Marker(eid='CRD.463.B2')
engrd_466_b2 = Marker(eid='ENGRD.466.B2')
enlat_466_b2 = Marker(eid='ENLAT.466.B2')
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
tdsb_428_b2 = TDCavity(l=1.5, v=0.45*0, freq=2997000.0, phi=0.0, eid='TDSB.428.B2')
tdsb_430_b2 = TDCavity(l=1.5, v=0.45*0, freq=2997000.0, phi=0.0, eid='TDSB.430.B2')

# UnknowElement 

# Matrices 

# Solenoids 

# lattice 
cell = (stsub_229_b1, d_1, stgrd_231_b1, d_2, qd_231_b1, d_3, ccx_232_b1,
d_4, tora_232_b1, d_5, qd_232_b1, d_6, ccy_232_b1, d_4, bpma_233_b1, 
d_8, qd_233_b1, d_9, enblock_233_b1, engrd_233_b1, d_10, ensub_235_b1, ensec_235_b1, 
stsec_235_l2, d_11, stac_238_l2, d_12, c_a3_1_1_l2, d_13, c_a3_1_2_l2, d_13, 
c_a3_1_3_l2, d_13, c_a3_1_4_l2, d_13, c_a3_1_5_l2, d_13, c_a3_1_6_l2, d_13, 
c_a3_1_7_l2, d_13, c_a3_1_8_l2, d_20, q_249_l2, d_21, cx_249_l2, d_22, 
bpmc_249_l2, d_23, enac_250_l2, stac_250_l2, d_12, c_a3_2_1_l2, d_13, c_a3_2_2_l2, 
d_13, c_a3_2_3_l2, d_13, c_a3_2_4_l2, d_13, c_a3_2_5_l2, d_13, c_a3_2_6_l2, 
d_13, c_a3_2_7_l2, d_13, c_a3_2_8_l2, d_20, q_261_l2, d_21, cy_261_l2, 
d_22, bpmc_261_l2, d_23, enac_262_l2, stac_262_l2, d_12, c_a3_3_1_l2, d_13, 
c_a3_3_2_l2, d_13, c_a3_3_3_l2, d_13, c_a3_3_4_l2, d_13, c_a3_3_5_l2, d_13, 
c_a3_3_6_l2, d_13, c_a3_3_7_l2, d_13, c_a3_3_8_l2, d_20, q_273_l2, d_21, 
cx_273_l2, d_22, bpmr_273_l2, d_23, enac_274_l2, stac_274_l2, d_12, c_a3_4_1_l2, 
d_13, c_a3_4_2_l2, d_13, c_a3_4_3_l2, d_13, c_a3_4_4_l2, d_13, c_a3_4_5_l2, 
d_13, c_a3_4_6_l2, d_13, c_a3_4_7_l2, d_13, c_a3_4_8_l2, d_20, q_285_l2, 
d_21, cy_285_l2, d_22, bpmr_285_l2, d_23, enac_286_l2, stac_286_l2, d_12, 
c_a4_1_1_l2, d_13, c_a4_1_2_l2, d_13, c_a4_1_3_l2, d_13, c_a4_1_4_l2, d_13, 
c_a4_1_5_l2, d_13, c_a4_1_6_l2, d_13, c_a4_1_7_l2, d_13, c_a4_1_8_l2, d_20, 
q_297_l2, d_21, cx_297_l2, d_22, bpmc_297_l2, d_23, enac_298_l2, stac_298_l2, 
d_12, c_a4_2_1_l2, d_13, c_a4_2_2_l2, d_13, c_a4_2_3_l2, d_13, c_a4_2_4_l2, 
d_13, c_a4_2_5_l2, d_13, c_a4_2_6_l2, d_13, c_a4_2_7_l2, d_13, c_a4_2_8_l2, 
d_20, q_309_l2, d_21, cy_309_l2, d_22, bpmr_309_l2, d_23, enac_310_l2, 
mid_310_l2, stac_310_l2, d_12, c_a4_3_1_l2, d_13, c_a4_3_2_l2, d_13, c_a4_3_3_l2, 
d_13, c_a4_3_4_l2, d_13, c_a4_3_5_l2, d_13, c_a4_3_6_l2, d_13, c_a4_3_7_l2, 
d_13, c_a4_3_8_l2, d_20, q_321_l2, d_21, cx_321_l2, d_22, bpmc_321_l2, 
d_23, enac_322_l2, stac_322_l2, d_12, c_a4_4_1_l2, d_13, c_a4_4_2_l2, d_13, 
c_a4_4_3_l2, d_13, c_a4_4_4_l2, d_13, c_a4_4_5_l2, d_13, c_a4_4_6_l2, d_13, 
c_a4_4_7_l2, d_13, c_a4_4_8_l2, d_20, q_333_l2, d_21, cy_333_l2, d_22, 
bpmr_333_l2, d_23, enac_334_l2, stac_334_l2, d_12, c_a5_1_1_l2, d_13, c_a5_1_2_l2, 
d_13, c_a5_1_3_l2, d_13, c_a5_1_4_l2, d_13, c_a5_1_5_l2, d_13, c_a5_1_6_l2, 
d_13, c_a5_1_7_l2, d_13, c_a5_1_8_l2, d_20, q_345_l2, d_21, cx_345_l2, 
d_22, bpmc_345_l2, d_23, enac_346_l2, stac_346_l2, d_12, c_a5_2_1_l2, d_13, 
c_a5_2_2_l2, d_13, c_a5_2_3_l2, d_13, c_a5_2_4_l2, d_13, c_a5_2_5_l2, d_13, 
c_a5_2_6_l2, d_13, c_a5_2_7_l2, d_13, c_a5_2_8_l2, d_20, q_357_l2, d_21, 
cy_357_l2, d_22, bpmc_357_l2, d_23, enac_358_l2, stac_358_l2, d_12, c_a5_3_1_l2, 
d_13, c_a5_3_2_l2, d_13, c_a5_3_3_l2, d_13, c_a5_3_4_l2, d_13, c_a5_3_5_l2, 
d_13, c_a5_3_6_l2, d_13, c_a5_3_7_l2, d_13, c_a5_3_8_l2, d_20, q_369_l2, 
d_21, cx_369_l2, d_22, bpmr_369_l2, d_23, enac_370_l2, stac_370_l2, d_12, 
c_a5_4_1_l2, d_13, c_a5_4_2_l2, d_13, c_a5_4_3_l2, d_13, c_a5_4_4_l2, d_13, 
c_a5_4_5_l2, d_13, c_a5_4_6_l2, d_13, c_a5_4_7_l2, d_13, c_a5_4_8_l2, d_20, 
q_381_l2, d_21, cy_381_l2, d_22, bpmr_381_l2, d_23, enac_382_l2, d_156, 
ensec_385_l2, stsec_385_b2, stsub_385_b2, d_10, stgrd_386_b2, d_158, tora_387_b2, d_159, 
bpma_387_b2, d_160, qd_387_b2, d_9, ccy_387_b2, d_162, dcm_388_b2, d_163, 
qd_388_b2, d_164, ccx_388_b2, d_165, engrd_390_b2, d_166, stgrd_390_b2, d_167, 
eod_390_b2, d_168, bpma_390_b2, d_160, qd_391_b2, d_170, ccy_391_b2, d_171, 
bcm_391_b2, d_172, qd_392_b2, d_173, ccx_392_b2, d_174, otra_392_b2, d_175, 
bam_392_b2, d_176, mpbpmf_393_b2, d_177, bpmf_393_b2, d_178, engrd_393_b2, d_179, 
stlat_393_b2, d_180, bb_393_b2, d_181, bb_402_b2, d_182, cbb_403_b2, d_183, 
bpms_404_b2, d_184, otrs_404_b2, d_185, bb_404_b2, d_182, cbb_405_b2, d_187, 
srm_406_b2, d_188, bb_413_b2, d_182, cbb_414_b2, d_166, enlat_414_b2, match_414_b2, 
stlat_414_b2, d_191, stgrd_414_b2, d_192, bam_414_b2, d_176, mpbpmf_414_b2, d_177, 
bpmf_414_b2, d_195, tora_415_b2, d_196, qd_415_b2, d_197, ccx_415_b2, d_198, 
ccy_416_b2, d_199, bcm_416_b2, d_200, qd_417_b2, d_201, ccx_418_b2, d_4, 
ccy_418_b2, d_203, bpma_418_b2, d_160, qd_418_b2, d_9, engrd_419_b2, d_206, 
stgrd_423_b2, d_207, ccx_425_b2, d_208, qd_425_b2, d_209, ccy_426_b2, d_210, 
otra_426_b2, d_211, bpma_426_b2, d_212, qd_427_b2, d_213, engrd_427_b2, d_214, 
stgrd_427_b2, d_215, match_428_b2, tdsb_428_b2, d_216, tdsb_430_b2, d_217, stblock_431_b2, 
d_2, qd_431_b2, d_219, ccx_431_b2, d_220, bpma_432_b2, d_221, engrd_432_b2, 
d_214, stgrd_432_b2, d_223, qd_434_b2, d_9, ccy_434_b2, d_225, qd_437_b2, 
d_9, engrd_437_b2, d_214, stgrd_437_b2, d_228, otra_438_b2, d_229, bpma_440_b2, 
d_160, qd_440_b2, d_9, ccx_441_b2, d_232, engrd_442_b2, d_214, stgrd_442_b2, 
d_234, bpma_444_b2, d_160, qd_444_b2, d_236, match_446_b2, otra_446_b2, d_237, 
engrd_446_b2, d_214, stgrd_447_b2, d_239, ccx_447_b2, d_240, bpma_448_b2, d_160, 
qd_448_b2, d_9, ccy_448_b2, d_243, otrb_450_b2, d_244, engrd_451_b2, d_214, 
stgrd_451_b2, d_246, bpma_452_b2, d_247, qd_452_b2, d_248, otrb_454_b2, d_249, 
ccx_454_b2, d_250, bpma_455_b2, d_160, qd_456_b2, d_9, ccx_456_b2, d_166, 
engrd_456_b2, d_214, stgrd_456_b2, d_255, otrb_457_b2, d_229, bpma_459_b2, d_160, 
qd_459_b2, d_9, ccy_460_b2, d_259, engrd_461_b2, d_214, stgrd_461_b2, d_261, 
otrb_461_b2, d_262, bpma_462_b2, d_263, qd_463_b2, d_264, crd_463_b2, d_265, 
ccx_464_b2, d_266, qd_464_b2, d_9, ccy_464_b2, d_239, ccx_465_b2, d_203, 
bpma_465_b2, d_160, qd_465_b2, d_9, engrd_466_b2, d_216, enlat_466_b2, ensub_466_b2)
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
tdsb_428_b2.ps_id = 'TDSB.B2'
tdsb_430_b2.ps_id = 'TDSB.B2'

#  
bb_393_b2.ps_id = 'BB.1.B2'
bb_402_b2.ps_id = 'BB.1.B2'
bb_404_b2.ps_id = 'BB.1.B2'
bb_413_b2.ps_id = 'BB.1.B2'
