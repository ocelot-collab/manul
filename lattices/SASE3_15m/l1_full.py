from ocelot import * 
tws = Twiss()
tws.beta_x  = 3.20269749953
tws.beta_y  = 4.57912479282
tws.alpha_x = 0.310986994864
tws.alpha_y = -1.79696241883
tws.E = 0.13

# drifts 
d_1 = Drift(l=1.24, eid='D_1')
d_2 = Drift(l=0.08115, eid='D_2')
d_3 = Drift(l=0.13115, eid='D_3')
d_4 = Drift(l=1.45, eid='D_4')
d_5 = Drift(l=0.63115, eid='D_5')
d_6 = Drift(l=2.8623, eid='D_6')
d_7 = Drift(l=1.7623, eid='D_7')
d_8 = Drift(l=0.68115, eid='D_8')
d_9 = Drift(l=0.18115, eid='D_9')
d_11 = Drift(l=0.2, eid='D_11')
d_13 = Drift(l=0.182428, eid='D_13')
d_14 = Drift(l=0.135051, eid='D_14')
d_15 = Drift(l=0.239432, eid='D_15')
d_16 = Drift(l=0.0751, eid='D_16')
d_18 = Drift(l=0.13494, eid='D_18')
d_19 = Drift(l=0.158616, eid='D_19')
d_20 = Drift(l=0.1325, eid='D_20')
d_21 = Drift(l=0.09865, eid='D_21')
d_22 = Drift(l=0.11615, eid='D_22')
d_23 = Drift(l=0.273615, eid='D_23')
d_27 = Drift(l=0.324432, eid='D_27')
d_28 = Drift(l=0.150051, eid='D_28')
d_30 = Drift(l=0.182429, eid='D_30')
d_35 = Drift(l=0.134939, eid='D_35')
d_40 = Drift(l=0.273616, eid='D_40')
d_44 = Drift(l=0.324431, eid='D_44')
d_45 = Drift(l=0.150052, eid='D_45')
d_48 = Drift(l=0.135052, eid='D_48')
d_49 = Drift(l=0.239431, eid='D_49')
d_73 = Drift(l=0.489766, eid='D_73')
d_77 = Drift(l=0.091932, eid='D_77')
d_81 = Drift(l=0.88128, eid='D_81')
d_83 = Drift(l=0.09115, eid='D_83')
d_84 = Drift(l=0.28115, eid='D_84')
d_85 = Drift(l=0.096, eid='D_85')
d_86 = Drift(l=0.204, eid='D_86')
d_88 = Drift(l=0.38115, eid='D_88')
d_89 = Drift(l=0.100597, eid='D_89')
d_90 = Drift(l=1.008384, eid='D_90')
d_91 = Drift(l=0.865597, eid='D_91')
d_92 = Drift(l=0.31, eid='D_92')
d_93 = Drift(l=0.325597, eid='D_93')
d_94 = Drift(l=1.008385, eid='D_94')
d_95 = Drift(l=0.100596, eid='D_95')
d_96 = Drift(l=0.39115, eid='D_96')
d_98 = Drift(l=0.25, eid='D_98')
d_100 = Drift(l=0.144, eid='D_100')
d_103 = Drift(l=0.56, eid='D_103')
d_106 = Drift(l=1.89, eid='D_106')
d_115 = Drift(l=2.04, eid='D_115')
d_118 = Drift(l=1.1242, eid='D_118')
d_119 = Drift(l=0.1408, eid='D_119')
d_121 = Drift(l=0.13965, eid='D_121')
d_122 = Drift(l=1.09132, eid='D_122')
d_123 = Drift(l=0.34903, eid='D_123')
d_126 = Drift(l=0.14395, eid='D_126')
d_127 = Drift(l=0.3522, eid='D_127')
d_128 = Drift(l=3.35, eid='D_128')
d_129 = Drift(l=0.221601, eid='D_129')
d_130 = Drift(l=0.345899, eid='D_130')
d_131 = Drift(l=0.3459, eid='D_131')
d_132 = Drift(l=0.345901, eid='D_132')
d_137 = Drift(l=0.2475, eid='D_137')
d_138 = Drift(l=0.0432, eid='D_138')
d_139 = Drift(l=0.085, eid='D_139')
d_140 = Drift(l=0.4579, eid='D_140')
d_141 = Drift(l=0.2216, eid='D_141')
d_149 = Drift(l=0.247499, eid='D_149')
d_150 = Drift(l=0.043201, eid='D_150')
d_162 = Drift(l=0.043199, eid='D_162')
d_163 = Drift(l=0.085001, eid='D_163')
d_164 = Drift(l=0.457899, eid='D_164')
d_177 = Drift(l=3.25, eid='D_177')
d_178 = Drift(l=1.414999, eid='D_178')
d_179 = Drift(l=0.131, eid='D_179')
d_180 = Drift(l=0.248001, eid='D_180')
d_181 = Drift(l=0.15215, eid='D_181')
d_182 = Drift(l=0.082149, eid='D_182')
d_183 = Drift(l=0.369, eid='D_183')
d_184 = Drift(l=0.846001, eid='D_184')
d_185 = Drift(l=0.884, eid='D_185')
d_186 = Drift(l=0.05, eid='D_186')
d_187 = Drift(l=0.33, eid='D_187')
d_188 = Drift(l=0.349, eid='D_188')
d_189 = Drift(l=0.15265, eid='D_189')
d_190 = Drift(l=0.131649, eid='D_190')
d_191 = Drift(l=0.150001, eid='D_191')
d_192 = Drift(l=0.5, eid='D_192')
d_193 = Drift(l=0.231649, eid='D_193')
d_194 = Drift(l=0.10165, eid='D_194')
d_195 = Drift(l=0.103001, eid='D_195')
d_196 = Drift(l=0.156499, eid='D_196')
d_198 = Drift(l=0.1745, eid='D_198')
d_200 = Drift(l=0.100105, eid='D_200')
d_201 = Drift(l=8.510829, eid='D_201')
d_202 = Drift(l=0.865104, eid='D_202')
d_204 = Drift(l=0.325104, eid='D_204')
d_205 = Drift(l=1.05488, eid='D_205')
d_206 = Drift(l=7.455949, eid='D_206')
d_207 = Drift(l=0.100104, eid='D_207')
d_208 = Drift(l=0.3, eid='D_208')
d_209 = Drift(l=0.1225, eid='D_209')
d_210 = Drift(l=0.1565, eid='D_210')
d_212 = Drift(l=0.3548, eid='D_212')
d_213 = Drift(l=0.1542, eid='D_213')
d_214 = Drift(l=0.09715, eid='D_214')
d_215 = Drift(l=0.44215, eid='D_215')
d_216 = Drift(l=0.223, eid='D_216')
d_218 = Drift(l=0.15015, eid='D_218')
d_219 = Drift(l=0.473, eid='D_219')
d_220 = Drift(l=0.108, eid='D_220')
d_222 = Drift(l=0.378, eid='D_222')
d_223 = Drift(l=0.15315, eid='D_223')
d_225 = Drift(l=0.1, eid='D_225')
d_228 = Drift(l=0.15, eid='D_228')
d_230 = Drift(l=0.379, eid='D_230')
d_232 = Drift(l=0.13165, eid='D_232')
d_233 = Drift(l=1.03115, eid='D_233')
d_234 = Drift(l=1.23015, eid='D_234')
d_235 = Drift(l=0.18, eid='D_235')
d_240 = Drift(l=1.079, eid='D_240')
d_243 = Drift(l=1.066, eid='D_243')
d_244 = Drift(l=0.147, eid='D_244')
d_246 = Drift(l=0.83115, eid='D_246')
d_247 = Drift(l=0.4, eid='D_247')
d_249 = Drift(l=0.099, eid='D_249')
d_250 = Drift(l=0.13265, eid='D_250')
d_251 = Drift(l=0.83165, eid='D_251')
d_252 = Drift(l=0.679, eid='D_252')
d_254 = Drift(l=0.10765, eid='D_254')
d_255 = Drift(l=0.15418, eid='D_255')
d_256 = Drift(l=0.46982, eid='D_256')
d_259 = Drift(l=0.18165, eid='D_259')
d_263 = Drift(l=0.34615, eid='D_263')
d_264 = Drift(l=1.22815, eid='D_264')
d_265 = Drift(l=0.152151, eid='D_265')
d_266 = Drift(l=0.081151, eid='D_266')
d_270 = Drift(l=1.097151, eid='D_270')
d_271 = Drift(l=0.39725, eid='D_271')

# quadrupoles 
qi_63_i1 = Quadrupole(l=0.2377, k1=-2.025428786, tilt=0.0, eid='QI.63.I1')
qi_66_i1 = Quadrupole(l=0.2377, k1=2.160052729, tilt=0.0, eid='QI.66.I1')
qi_69_i1 = Quadrupole(l=0.2377, k1=-2.224853904, tilt=0.0, eid='QI.69.I1')
qi_71_i1 = Quadrupole(l=0.2377, k1=3.403378798, tilt=0.0, eid='QI.71.I1')
qi_72_i1 = Quadrupole(l=0.2377, k1=-4.43452895, tilt=0.0, eid='QI.72.I1')
qi_73_i1 = Quadrupole(l=0.2377, k1=4.632555992, tilt=0.0, eid='QI.73.I1')
qi_74_i1 = Quadrupole(l=0.2377, k1=-4.99137522, tilt=0.0, eid='QI.74.I1')
qi_75_i1 = Quadrupole(l=0.2377, k1=5.027338701, tilt=0.0, eid='QI.75.I1')
qi_77_i1 = Quadrupole(l=0.2377, k1=-4.99137522, tilt=0.0, eid='QI.77.I1')
qi_78_i1 = Quadrupole(l=0.2377, k1=4.632555992, tilt=0.0, eid='QI.78.I1')
qi_79_i1 = Quadrupole(l=0.2377, k1=-4.99137522, tilt=0.0, eid='QI.79.I1')
qi_80_i1 = Quadrupole(l=0.2377, k1=5.027338701, tilt=0.0, eid='QI.80.I1')
qi_82_i1 = Quadrupole(l=0.2377, k1=-4.99137522, tilt=0.0, eid='QI.82.I1')
qi_83_i1 = Quadrupole(l=0.2377, k1=4.632555992, tilt=0.0, eid='QI.83.I1')
qi_84_i1 = Quadrupole(l=0.2377, k1=-4.99137522, tilt=0.0, eid='QI.84.I1')
qi_85_i1 = Quadrupole(l=0.2377, k1=5.027338701, tilt=0.0, eid='QI.85.I1')
qi_86_i1 = Quadrupole(l=0.2377, k1=-4.99137522, tilt=0.0, eid='QI.86.I1')
qi_88_i1 = Quadrupole(l=0.2377, k1=4.632555992, tilt=0.0, eid='QI.88.I1')
qi_89_i1 = Quadrupole(l=0.2377, k1=-4.99137522, tilt=0.0, eid='QI.89.I1')
qi_90_i1 = Quadrupole(l=0.2377, k1=5.027338701, tilt=0.0, eid='QI.90.I1')
qi_92_i1 = Quadrupole(l=0.2377, k1=-4.99137522, tilt=0.0, eid='QI.92.I1')
qi_93_i1 = Quadrupole(l=0.2377, k1=-0.7125210101, tilt=0.0, eid='QI.93.I1')
qi_94_i1 = Quadrupole(l=0.2377, k1=3.329565017, tilt=0.0, eid='QI.94.I1')
qi_95_i1 = Quadrupole(l=0.2377, k1=-2.997330916, tilt=0.0, eid='QI.95.I1')
qi_102_i1 = Quadrupole(l=0.2377, k1=0.2397081548, tilt=0.0, eid='QI.102.I1')
qi_103_i1 = Quadrupole(l=0.2377, k1=-0.9101419679, tilt=0.0, eid='QI.103.I1')
qi_104_i1 = Quadrupole(l=0.2377, k1=1.443246717, tilt=0.0, eid='QI.104.I1')
qi_107_i1 = Quadrupole(l=0.2377, k1=-1.522641254, tilt=0.0, eid='QI.107.I1')
qi_109_i1 = Quadrupole(l=0.2377, k1=1.522641068, tilt=0.0, eid='QI.109.I1')
qi_112_i1 = Quadrupole(l=0.2377, k1=-1.522641254, tilt=0.0, eid='QI.112.I1')
qi_114_i1 = Quadrupole(l=0.2377, k1=0.9967996614, tilt=0.0, eid='QI.114.I1')
qi_116_i1 = Quadrupole(l=0.2377, k1=0.5375414029, tilt=0.0, eid='QI.116.I1')
qi_118_i1 = Quadrupole(l=0.2377, k1=-0.94121992, tilt=0.0, eid='QI.118.I1')
q_134_l1 = Quadrupole(l=0.2136, k1=0.2815559415, tilt=0.0, eid='Q.134.L1')
q_146_l1 = Quadrupole(l=0.2136, k1=-0.2990648887, tilt=0.0, eid='Q.146.L1')
q_158_l1 = Quadrupole(l=0.2136, k1=0.2134774877, tilt=0.0, eid='Q.158.L1')
q_170_l1 = Quadrupole(l=0.2136, k1=-0.2202627275, tilt=0.0, eid='Q.170.L1')
qi_176_b1 = Quadrupole(l=0.2377, k1=0.0, tilt=0.0, eid='QI.176.B1')
qd_179_b1 = Quadrupole(l=0.2367, k1=0.7959712907, tilt=0.0, eid='QD.179.B1')
qd_181_b1 = Quadrupole(l=0.2367, k1=-0.7306067065, tilt=0.0, eid='QD.181.B1')
qi_204_b1 = Quadrupole(l=0.2377, k1=-0.9122656301, tilt=0.0, eid='QI.204.B1')
qi_205_b1 = Quadrupole(l=0.2377, k1=0.0161280277, tilt=0.0, eid='QI.205.B1')
qi_206_b1 = Quadrupole(l=0.2377, k1=0.6876709288, tilt=0.0, eid='QI.206.B1')
qi_209_b1 = Quadrupole(l=0.2377, k1=1.044386249, tilt=0.0, eid='QI.209.B1')
qd_210_b1 = Quadrupole(l=0.2367, k1=-2.183150525, tilt=0.0, eid='QD.210.B1')
qi_211_b1 = Quadrupole(l=0.2377, k1=0.6386118848, tilt=0.0, eid='QI.211.B1')
qi_213_b1 = Quadrupole(l=0.2377, k1=1.186969649, tilt=0.0, eid='QI.213.B1')
qi_215_b1 = Quadrupole(l=0.2377, k1=-1.123733875, tilt=0.0, eid='QI.215.B1')
qi_217_b1 = Quadrupole(l=0.2377, k1=-1.43507582, tilt=0.0, eid='QI.217.B1')
qd_219_b1 = Quadrupole(l=0.2367, k1=2.859590704, tilt=0.0, eid='QD.219.B1')
qd_221_b1 = Quadrupole(l=0.2367, k1=-2.859590929, tilt=0.0, eid='QD.221.B1')
qd_223_b1 = Quadrupole(l=0.2367, k1=2.859590704, tilt=0.0, eid='QD.223.B1')
qi_224_b1 = Quadrupole(l=0.2377, k1=-0.8565833408, tilt=0.0, eid='QI.224.B1')
qi_226_b1 = Quadrupole(l=0.2377, k1=-1.561856764, tilt=0.0, eid='QI.226.B1')
qi_227_b1 = Quadrupole(l=0.2377, k1=1.523532903, tilt=0.0, eid='QI.227.B1')

# bending magnets 
bl_73_i1 = SBend(l=0.2, angle=-0.1109740393, e1=-0.05548702, e2=-0.05548702, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.73.I1')
bl_75_i1 = SBend(l=0.2, angle=0.0426524581, e1=0.021326229, e2=0.021326229, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.75.I1')
bl_76_i1 = SBend(l=0.2, angle=0.0426524581, e1=0.021326229, e2=0.021326229, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.76.I1')
bl_77_i1 = SBend(l=0.2, angle=-0.1109740393, e1=-0.05548702, e2=-0.05548702, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.77.I1')
bl_78_i1 = SBend(l=0.2, angle=-0.1109740393, e1=-0.05548702, e2=-0.05548702, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.78.I1')
bl_80_i1 = SBend(l=0.2, angle=0.0426524581, e1=0.021326229, e2=0.021326229, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.80.I1')
bl_81_i1 = SBend(l=0.2, angle=0.0426524581, e1=0.021326229, e2=0.021326229, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.81.I1')
bl_82_i1 = SBend(l=0.2, angle=-0.1109740393, e1=-0.05548702, e2=-0.05548702, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.82.I1')
bl_83_i1 = SBend(l=0.2, angle=0.1109740393, e1=0.05548702, e2=0.05548702, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.83.I1')
bl_85_i1 = SBend(l=0.2, angle=-0.0426524581, e1=-0.021326229, e2=-0.021326229, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.85.I1')
bl_86_i1 = SBend(l=0.2, angle=-0.0426524581, e1=-0.021326229, e2=-0.021326229, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.86.I1')
bl_87_i1 = SBend(l=0.2, angle=0.1109740393, e1=0.05548702, e2=0.05548702, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.87.I1')
bl_88_i1 = SBend(l=0.2, angle=0.1109740393, e1=0.05548702, e2=0.05548702, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.88.I1')
bl_90_i1 = SBend(l=0.2, angle=-0.0426524581, e1=-0.021326229, e2=-0.021326229, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.90.I1')
bl_91_i1 = SBend(l=0.2, angle=-0.0426524581, e1=-0.021326229, e2=-0.021326229, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.91.I1')
bl_92_i1 = SBend(l=0.2, angle=0.1109740393, e1=0.05548702, e2=0.05548702, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.92.I1')
bb_96_i1 = SBend(l=0.5, angle=0.1429424657, e1=0.0, e2=0.1429424657, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BB.96.I1')
bb_98_i1 = SBend(l=0.5, angle=-0.1429424657, e1=-0.1429424657, e2=0.0, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BB.98.I1')
bb_100_i1 = SBend(l=0.5, angle=-0.1429424657, e1=0.0, e2=-0.1429424657, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BB.100.I1')
bb_101_i1 = SBend(l=0.5, angle=0.1429424657, e1=0.1429424657, e2=0.0, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BB.101.I1')
bb_182_b1 = SBend(l=0.5, angle=0.0504400154, e1=0.0, e2=0.0504400154, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BB.182.B1')
bb_191_b1 = SBend(l=0.5, angle=-0.0504400154, e1=-0.0504400154, e2=0.0, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BB.191.B1')
bb_193_b1 = SBend(l=0.5, angle=-0.0504400154, e1=0.0, e2=-0.0504400154, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BB.193.B1')
bb_202_b1 = SBend(l=0.5, angle=0.0504400154, e1=0.0504400154, e2=0.0, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BB.202.B1')

# correctors 
ciy_63_i1 = Vcor(l=0.1, angle=0.0, eid='CIY.63.I1')
cix_65_i1 = Hcor(l=0.1, angle=0.0, eid='CIX.65.I1')
ciy_72_i1 = Vcor(l=0.1, angle=0.0, eid='CIY.72.I1')
cix_73i_i1 = Hcor(l=0.1, angle=0.0, eid='CIX.73I.I1')
cix_73ii_i1 = Hcor(l=0.1, angle=0.0, eid='CIX.73II.I1')
ciy_75_i1 = Vcor(l=0.1, angle=0.0, eid='CIY.75.I1')
cix_76_i1 = Hcor(l=0.1, angle=0.0, eid='CIX.76.I1')
cix_78_i1 = Hcor(l=0.1, angle=0.0, eid='CIX.78.I1')
ciy_80_i1 = Vcor(l=0.1, angle=0.0, eid='CIY.80.I1')
cix_81_i1 = Hcor(l=0.1, angle=0.0, eid='CIX.81.I1')
cix_83_i1 = Hcor(l=0.1, angle=0.0, eid='CIX.83.I1')
ciy_85_i1 = Vcor(l=0.1, angle=0.0, eid='CIY.85.I1')
cix_86_i1 = Hcor(l=0.1, angle=0.0, eid='CIX.86.I1')
cix_88_i1 = Hcor(l=0.1, angle=0.0, eid='CIX.88.I1')
cix_90_i1 = Hcor(l=0.1, angle=0.0, eid='CIX.90.I1')
ciy_92_i1 = Vcor(l=0.1, angle=0.0, eid='CIY.92.I1')
ciy_94_i1 = Vcor(l=0.1, angle=0.0, eid='CIY.94.I1')
cix_95_i1 = Hcor(l=0.1, angle=0.0, eid='CIX.95.I1')
cix_102_i1 = Hcor(l=0.1, angle=0.0, eid='CIX.102.I1')
ciy_103_i1 = Vcor(l=0.1, angle=0.0, eid='CIY.103.I1')
cix_104_i1 = Hcor(l=0.1, angle=0.0, eid='CIX.104.I1')
ciy_107_i1 = Vcor(l=0.1, angle=0.0, eid='CIY.107.I1')
cix_109_i1 = Hcor(l=0.1, angle=0.0, eid='CIX.109.I1')
ciy_112_i1 = Vcor(l=0.1, angle=0.0, eid='CIY.112.I1')
cix_114_i1 = Hcor(l=0.1, angle=0.0, eid='CIX.114.I1')
ciy_116_i1 = Vcor(l=0.1, angle=0.0, eid='CIY.116.I1')
cix_118_i1 = Hcor(l=0.1, angle=0.0, eid='CIX.118.I1')
cx_134_l1 = Hcor(l=0.0, angle=0.0, eid='CX.134.L1')
cy_134_l1 = Vcor(l=0.0, angle=0.0, eid='CY.134.L1')
cx_146_l1 = Hcor(l=0.0, angle=0.0, eid='CX.146.L1')
cy_146_l1 = Vcor(l=0.0, angle=0.0, eid='CY.146.L1')
cx_158_l1 = Hcor(l=0.0, angle=0.0, eid='CX.158.L1')
cy_158_l1 = Vcor(l=0.0, angle=0.0, eid='CY.158.L1')
cx_170_l1 = Hcor(l=0.0, angle=0.0, eid='CX.170.L1')
cy_170_l1 = Vcor(l=0.0, angle=0.0, eid='CY.170.L1')
ciy_176_b1 = Vcor(l=0.1, angle=0.0, eid='CIY.176.B1')
cix_177_b1 = Hcor(l=0.1, angle=0.0, eid='CIX.177.B1')
ccx_179_b1 = Hcor(l=0.1, angle=0.0, eid='CCX.179.B1')
ccy_181_b1 = Vcor(l=0.1, angle=0.0, eid='CCY.181.B1')
ciy_204_b1 = Vcor(l=0.1, angle=0.0, eid='CIY.204.B1')
cix_205_b1 = Hcor(l=0.1, angle=0.0, eid='CIX.205.B1')
cix_209_b1 = Hcor(l=0.1, angle=0.0, eid='CIX.209.B1')
ccy_210_b1 = Vcor(l=0.1, angle=0.0, eid='CCY.210.B1')
cix_213_b1 = Hcor(l=0.1, angle=0.0, eid='CIX.213.B1')
ciy_214_b1 = Vcor(l=0.1, angle=0.0, eid='CIY.214.B1')
cix_216_b1 = Hcor(l=0.1, angle=0.0, eid='CIX.216.B1')
ccy_217_b1 = Vcor(l=0.1, angle=0.0, eid='CCY.217.B1')
ccy_221_b1 = Vcor(l=0.1, angle=0.0, eid='CCY.221.B1')
cfx_223_b1 = Hcor(l=0.1, angle=0.0, eid='CFX.223.B1')
ciy_226_b1 = Vcor(l=0.1, angle=0.0, eid='CIY.226.B1')
cfx_226_b1 = Hcor(l=0.1, angle=0.0, eid='CFX.226.B1')

# markers 
ensub_62_i1 = Marker(eid='ENSUB.62.I1')
stsub_62_i1 = Marker(eid='STSUB.62.I1')
stlat_73_i1 = Marker(eid='STLAT.73.I1')
match_73_i1 = Marker(eid='MATCH.73.I1')
id_90904668_ = Marker(eid='ID_90904668_')
enlat_93_i1 = Marker(eid='ENLAT.93.I1')
ensub_93_i1 = Marker(eid='ENSUB.93.I1')
stsub_93_i1 = Marker(eid='STSUB.93.I1')
tora_94_i1 = Marker(eid='TORA.94.I1')
mpbpmf_95_i1 = Marker(eid='MPBPMF.95.I1')
stlat_96_i1 = Marker(eid='STLAT.96.I1')
otrs_99_i1 = Marker(eid='OTRS.99.I1')
enlat_101_i1 = Marker(eid='ENLAT.101.I1')
mpbpmf_103_i1 = Marker(eid='MPBPMF.103.I1')
stlat_104_i1 = Marker(eid='STLAT.104.I1')
match_104_i1 = Marker(eid='MATCH.104.I1')
enlat_114_i1 = Marker(eid='ENLAT.114.I1')
tora_116_i1 = Marker(eid='TORA.116.I1')
otra_118_i1 = Marker(eid='OTRA.118.I1')
dcm_118_i1 = Marker(eid='DCM.118.I1')
ensub_119_i1 = Marker(eid='ENSUB.119.I1')
ensec_119_i1 = Marker(eid='ENSEC.119.I1')
stsec_119_l1 = Marker(eid='STSEC.119.L1')
stac_122_l1 = Marker(eid='STAC.122.L1')
enac_134_l1 = Marker(eid='ENAC.134.L1')
stac_134_l1 = Marker(eid='STAC.134.L1')
enac_146_l1 = Marker(eid='ENAC.146.L1')
stac_146_l1 = Marker(eid='STAC.146.L1')
enac_158_l1 = Marker(eid='ENAC.158.L1')
stac_158_l1 = Marker(eid='STAC.158.L1')
enac_170_l1 = Marker(eid='ENAC.170.L1')
ensec_174_l1 = Marker(eid='ENSEC.174.L1')
match_174_l1 = Marker(eid='MATCH.174.L1')
stsec_174_b1 = Marker(eid='STSEC.174.B1')
stsub_174_b1 = Marker(eid='STSUB.174.B1')
stgrd_175_b1 = Marker(eid='STGRD.175.B1')
tora_175_b1 = Marker(eid='TORA.175.B1')
dcm_176_b1 = Marker(eid='DCM.176.B1')
engrd_178_b1 = Marker(eid='ENGRD.178.B1')
stgrd_178_b1 = Marker(eid='STGRD.178.B1')
eod_179_b1 = Marker(eid='EOD.179.B1')
bcm_180_b1 = Marker(eid='BCM.180.B1')
otra_180_b1 = Marker(eid='OTRA.180.B1')
bam_181_b1 = Marker(eid='BAM.181.B1')
mpbpmf_181_b1 = Marker(eid='MPBPMF.181.B1')
engrd_181_b1 = Marker(eid='ENGRD.181.B1')
stlat_182_b1 = Marker(eid='STLAT.182.B1')
otrs_192_b1 = Marker(eid='OTRS.192.B1')
srm_194_b1 = Marker(eid='SRM.194.B1')
enlat_202_b1 = Marker(eid='ENLAT.202.B1')
match_202_b1 = Marker(eid='MATCH.202.B1')
stlat_202_b1 = Marker(eid='STLAT.202.B1')
stgrd_203_b1 = Marker(eid='STGRD.203.B1')
bam_203_b1 = Marker(eid='BAM.203.B1')
mpbpmf_203_b1 = Marker(eid='MPBPMF.203.B1')
tora_203_b1 = Marker(eid='TORA.203.B1')
eod_204_b1 = Marker(eid='EOD.204.B1')
bcm_205_b1 = Marker(eid='BCM.205.B1')
otra_206_b1 = Marker(eid='OTRA.206.B1')
engrd_206_b1 = Marker(eid='ENGRD.206.B1')
stgrd_206_b1 = Marker(eid='STGRD.206.B1')
match_207_b1 = Marker(eid='MATCH.207.B1')
stblock_207_b1 = Marker(eid='STBLOCK.207.B1')
engrd_209_b1 = Marker(eid='ENGRD.209.B1')
stgrd_209_b1 = Marker(eid='STGRD.209.B1')
engrd_214_b1 = Marker(eid='ENGRD.214.B1')
stgrd_214_b1 = Marker(eid='STGRD.214.B1')
match_218_b1 = Marker(eid='MATCH.218.B1')
otrb_218_b1 = Marker(eid='OTRB.218.B1')
engrd_219_b1 = Marker(eid='ENGRD.219.B1')
stgrd_219_b1 = Marker(eid='STGRD.219.B1')
otrb_220_b1 = Marker(eid='OTRB.220.B1')
dcm_221_b1 = Marker(eid='DCM.221.B1')
otrb_222_b1 = Marker(eid='OTRB.222.B1')
engrd_223_b1 = Marker(eid='ENGRD.223.B1')
stgrd_224_b1 = Marker(eid='STGRD.224.B1')
otrb_224_b1 = Marker(eid='OTRB.224.B1')
engrd_228_b1 = Marker(eid='ENGRD.228.B1')
enlat_229_b1 = Marker(eid='ENLAT.229.B1')
ensub_229_b1 = Marker(eid='ENSUB.229.B1')

# monitor 
bpma_63_i1 = Monitor(eid='BPMA.63.I1')
bpma_72_i1 = Monitor(eid='BPMA.72.I1')
bpma_75_i1 = Monitor(eid='BPMA.75.I1')
bpma_77_i1 = Monitor(eid='BPMA.77.I1')
bpma_80_i1 = Monitor(eid='BPMA.80.I1')
bpma_82_i1 = Monitor(eid='BPMA.82.I1')
bpma_85_i1 = Monitor(eid='BPMA.85.I1')
bpma_87_i1 = Monitor(eid='BPMA.87.I1')
bpma_90_i1 = Monitor(eid='BPMA.90.I1')
bpma_92_i1 = Monitor(eid='BPMA.92.I1')
bpmf_95_i1 = Monitor(eid='BPMF.95.I1')
bpms_99_i1 = Monitor(eid='BPMS.99.I1')
bpmf_103_i1 = Monitor(eid='BPMF.103.I1')
bpma_103_i1 = Monitor(eid='BPMA.103.I1')
bpma_105_i1 = Monitor(eid='BPMA.105.I1')
bpma_107_i1 = Monitor(eid='BPMA.107.I1')
bpma_110_i1 = Monitor(eid='BPMA.110.I1')
bpma_112_i1 = Monitor(eid='BPMA.112.I1')
bpma_115_i1 = Monitor(eid='BPMA.115.I1')
bpma_117_i1 = Monitor(eid='BPMA.117.I1')
bpma_119_i1 = Monitor(eid='BPMA.119.I1')
bpmc_134_l1 = Monitor(eid='BPMC.134.L1')
bpmr_146_l1 = Monitor(eid='BPMR.146.L1')
bpmc_158_l1 = Monitor(eid='BPMC.158.L1')
bpmr_170_l1 = Monitor(eid='BPMR.170.L1')
bpma_175_b1 = Monitor(eid='BPMA.175.B1')
bpma_179_b1 = Monitor(eid='BPMA.179.B1')
bpmf_181_b1 = Monitor(eid='BPMF.181.B1')
bpms_192_b1 = Monitor(eid='BPMS.192.B1')
bpmf_203_b1 = Monitor(eid='BPMF.203.B1')
bpma_206_b1 = Monitor(eid='BPMA.206.B1')
bpma_210_b1 = Monitor(eid='BPMA.210.B1')
bpma_213_b1 = Monitor(eid='BPMA.213.B1')
bpma_215_b1 = Monitor(eid='BPMA.215.B1')
bpma_217_b1 = Monitor(eid='BPMA.217.B1')
bpma_219_b1 = Monitor(eid='BPMA.219.B1')
bpma_221_b1 = Monitor(eid='BPMA.221.B1')
bpma_223_b1 = Monitor(eid='BPMA.223.B1')
bpma_226_b1 = Monitor(eid='BPMA.226.B1')
bpma_227_b1 = Monitor(eid='BPMA.227.B1')

# sextupoles 
sc_74i_i1 = Sextupole(l=0.1121, k2=-9.817522762156, tilt=1.570796327, eid='SC.74I.I1')
sc_74ii_i1 = Sextupole(l=0.1121, k2=-5.948211333809, tilt=1.570796327, eid='SC.74II.I1')
sc_76_i1 = Sextupole(l=0.1121, k2=-5.948211333809, tilt=1.570796327, eid='SC.76.I1')
sc_77_i1 = Sextupole(l=0.1121, k2=-9.817522762156, tilt=1.570796327, eid='SC.77.I1')
sc_79i_i1 = Sextupole(l=0.1121, k2=-9.817522762156, tilt=1.570796327, eid='SC.79I.I1')
sc_79ii_i1 = Sextupole(l=0.1121, k2=-5.948211333809, tilt=1.570796327, eid='SC.79II.I1')
sc_81_i1 = Sextupole(l=0.1121, k2=-5.948211333809, tilt=1.570796327, eid='SC.81.I1')
sc_82_i1 = Sextupole(l=0.1121, k2=-9.817522762156, tilt=1.570796327, eid='SC.82.I1')
sc_84i_i1 = Sextupole(l=0.1121, k2=9.817522762156, tilt=1.570796327, eid='SC.84I.I1')
sc_84ii_i1 = Sextupole(l=0.1121, k2=5.948211333809, tilt=1.570796327, eid='SC.84II.I1')
sc_86_i1 = Sextupole(l=0.1121, k2=5.948211333809, tilt=1.570796327, eid='SC.86.I1')
sc_87_i1 = Sextupole(l=0.1121, k2=9.817522762156, tilt=1.570796327, eid='SC.87.I1')
sc_89i_i1 = Sextupole(l=0.1121, k2=9.817522762156, tilt=1.570796327, eid='SC.89I.I1')
sc_89ii_i1 = Sextupole(l=0.1121, k2=5.948211333809, tilt=1.570796327, eid='SC.89II.I1')
sc_91_i1 = Sextupole(l=0.1121, k2=5.948211333809, tilt=1.570796327, eid='SC.91.I1')
sc_92_i1 = Sextupole(l=0.1121, k2=9.817522762156, tilt=1.570796327, eid='SC.92.I1')

# octupole 

# undulator 

# cavity 
c_a2_1_1_l1 = Cavity(l=1.0377, v=0.0214344953, freq=1300000000.0, phi=25, eid='C.A2.1.1.L1')
c_a2_1_2_l1 = Cavity(l=1.0377, v=0.0214344953, freq=1300000000.0, phi=25, eid='C.A2.1.2.L1')
c_a2_1_3_l1 = Cavity(l=1.0377, v=0.0214344953, freq=1300000000.0, phi=25, eid='C.A2.1.3.L1')
c_a2_1_4_l1 = Cavity(l=1.0377, v=0.0214344953, freq=1300000000.0, phi=25, eid='C.A2.1.4.L1')
c_a2_1_5_l1 = Cavity(l=1.0377, v=0.0214344953, freq=1300000000.0, phi=25, eid='C.A2.1.5.L1')
c_a2_1_6_l1 = Cavity(l=1.0377, v=0.0214344953, freq=1300000000.0, phi=25, eid='C.A2.1.6.L1')
c_a2_1_7_l1 = Cavity(l=1.0377, v=0.0214344953, freq=1300000000.0, phi=25, eid='C.A2.1.7.L1')
c_a2_1_8_l1 = Cavity(l=1.0377, v=0.0214344953, freq=1300000000.0, phi=25, eid='C.A2.1.8.L1')
c_a2_2_1_l1 = Cavity(l=1.0377, v=0.020463522730000003, freq=1300000000.0, phi=25, eid='C.A2.2.1.L1')
c_a2_2_2_l1 = Cavity(l=1.0377, v=0.020463522730000003, freq=1300000000.0, phi=25, eid='C.A2.2.2.L1')
c_a2_2_3_l1 = Cavity(l=1.0377, v=0.020463522730000003, freq=1300000000.0, phi=25, eid='C.A2.2.3.L1')
c_a2_2_4_l1 = Cavity(l=1.0377, v=0.020463522730000003, freq=1300000000.0, phi=25, eid='C.A2.2.4.L1')
c_a2_2_5_l1 = Cavity(l=1.0377, v=0.020463522730000003, freq=1300000000.0, phi=25, eid='C.A2.2.5.L1')
c_a2_2_6_l1 = Cavity(l=1.0377, v=0.020463522730000003, freq=1300000000.0, phi=25, eid='C.A2.2.6.L1')
c_a2_2_7_l1 = Cavity(l=1.0377, v=0.020463522730000003, freq=1300000000.0, phi=25, eid='C.A2.2.7.L1')
c_a2_2_8_l1 = Cavity(l=1.0377, v=0.020463522730000003, freq=1300000000.0, phi=25, eid='C.A2.2.8.L1')
c_a2_3_1_l1 = Cavity(l=1.0377, v=0.01914636534, freq=1300000000.0, phi=25, eid='C.A2.3.1.L1')
c_a2_3_2_l1 = Cavity(l=1.0377, v=0.01914636534, freq=1300000000.0, phi=25, eid='C.A2.3.2.L1')
c_a2_3_3_l1 = Cavity(l=1.0377, v=0.01914636534, freq=1300000000.0, phi=25, eid='C.A2.3.3.L1')
c_a2_3_4_l1 = Cavity(l=1.0377, v=0.01914636534, freq=1300000000.0, phi=25, eid='C.A2.3.4.L1')
c_a2_3_5_l1 = Cavity(l=1.0377, v=0.01914636534, freq=1300000000.0, phi=25, eid='C.A2.3.5.L1')
c_a2_3_6_l1 = Cavity(l=1.0377, v=0.01914636534, freq=1300000000.0, phi=25, eid='C.A2.3.6.L1')
c_a2_3_7_l1 = Cavity(l=1.0377, v=0.01914636534, freq=1300000000.0, phi=25, eid='C.A2.3.7.L1')
c_a2_3_8_l1 = Cavity(l=1.0377, v=0.01914636534, freq=1300000000.0, phi=25, eid='C.A2.3.8.L1')
c_a2_4_1_l1 = Cavity(l=1.0377, v=0.017571293340000002, freq=1300000000.0, phi=25, eid='C.A2.4.1.L1')
c_a2_4_2_l1 = Cavity(l=1.0377, v=0.017571293340000002, freq=1300000000.0, phi=25, eid='C.A2.4.2.L1')
c_a2_4_3_l1 = Cavity(l=1.0377, v=0.017571293340000002, freq=1300000000.0, phi=25, eid='C.A2.4.3.L1')
c_a2_4_4_l1 = Cavity(l=1.0377, v=0.017571293340000002, freq=1300000000.0, phi=25, eid='C.A2.4.4.L1')
c_a2_4_5_l1 = Cavity(l=1.0377, v=0.017571293340000002, freq=1300000000.0, phi=25, eid='C.A2.4.5.L1')
c_a2_4_6_l1 = Cavity(l=1.0377, v=0.017571293340000002, freq=1300000000.0, phi=25, eid='C.A2.4.6.L1')
c_a2_4_7_l1 = Cavity(l=1.0377, v=0.017571293340000002, freq=1300000000.0, phi=25, eid='C.A2.4.7.L1')
c_a2_4_8_l1 = Cavity(l=1.0377, v=0.017571293340000002, freq=1300000000.0, phi=25, eid='C.A2.4.8.L1')

# tdcavity 
tdsb_208_b1 = Cavity(l=1.5, v=0.0, freq=2997000.0, phi=0.0, eid='TDSB.208.B1')

# UnknowElement 

# Matrices 

# Solenoids 

# lattice 
cell = (ensub_62_i1, stsub_62_i1, d_1, ciy_63_i1, d_2, qi_63_i1, d_3, 
bpma_63_i1, d_4, cix_65_i1, d_5, qi_66_i1, d_6, qi_69_i1, d_7, 
qi_71_i1, d_8, bpma_72_i1, d_9, qi_72_i1, d_9, ciy_72_i1, d_11, 
cix_73i_i1, d_2, stlat_73_i1, match_73_i1, qi_73_i1, id_90904668_, d_13, bl_73_i1, 
d_14, cix_73ii_i1, d_15, sc_74i_i1, d_16, qi_74_i1, d_16, sc_74ii_i1, 
d_18, bl_75_i1, d_19, bpma_75_i1, d_20, ciy_75_i1, d_21, qi_75_i1, 
d_22, cix_76_i1, d_23, bl_76_i1, d_18, sc_76_i1, d_16, qi_77_i1, 
d_16, sc_77_i1, d_27, bpma_77_i1, d_28, bl_77_i1, d_13, qi_78_i1, 
d_30, bl_78_i1, d_14, cix_78_i1, d_15, sc_79i_i1, d_16, qi_79_i1, 
d_16, sc_79ii_i1, d_35, bl_80_i1, d_19, bpma_80_i1, d_20, ciy_80_i1, 
d_21, qi_80_i1, d_22, cix_81_i1, d_40, bl_81_i1, d_18, sc_81_i1, 
d_16, qi_82_i1, d_16, sc_82_i1, d_44, bpma_82_i1, d_45, bl_82_i1, 
d_13, qi_83_i1, d_13, bl_83_i1, d_48, cix_83_i1, d_49, sc_84i_i1, 
d_16, qi_84_i1, d_16, sc_84ii_i1, d_18, bl_85_i1, d_19, bpma_85_i1, 
d_20, ciy_85_i1, d_21, qi_85_i1, d_22, cix_86_i1, d_40, bl_86_i1, 
d_35, sc_86_i1, d_16, qi_86_i1, d_16, sc_87_i1, d_27, bpma_87_i1, 
d_45, bl_87_i1, d_13, qi_88_i1, d_13, bl_88_i1, d_14, cix_88_i1, 
d_15, sc_89i_i1, d_16, qi_89_i1, d_16, sc_89ii_i1, d_35, bl_90_i1, 
d_19, bpma_90_i1, d_20, cix_90_i1, d_21, qi_90_i1, d_73, bl_91_i1, 
d_18, sc_91_i1, d_16, qi_92_i1, d_16, sc_92_i1, d_77, ciy_92_i1, 
d_20, bpma_92_i1, d_28, bl_92_i1, d_13, qi_93_i1, enlat_93_i1, ensub_93_i1, 
stsub_93_i1, d_81, tora_94_i1, d_11, ciy_94_i1, d_83, qi_94_i1, d_84, 
bpmf_95_i1, d_85, mpbpmf_95_i1, d_86, cix_95_i1, d_83, qi_95_i1, d_88, 
stlat_96_i1, d_89, bb_96_i1, d_90, bb_98_i1, d_91, bpms_99_i1, d_92, 
otrs_99_i1, d_93, bb_100_i1, d_94, bb_101_i1, d_95, enlat_101_i1, d_96, 
qi_102_i1, d_83, cix_102_i1, d_98, bpmf_103_i1, d_85, mpbpmf_103_i1, d_100, 
ciy_103_i1, d_83, qi_103_i1, d_9, bpma_103_i1, d_103, cix_104_i1, d_83, 
qi_104_i1, stlat_104_i1, match_104_i1, d_9, bpma_105_i1, d_106, ciy_107_i1, d_83, 
qi_107_i1, d_9, bpma_107_i1, d_106, cix_109_i1, d_83, qi_109_i1, d_9, 
bpma_110_i1, d_106, ciy_112_i1, d_83, qi_112_i1, d_9, bpma_112_i1, d_115, 
enlat_114_i1, cix_114_i1, d_83, qi_114_i1, d_9, bpma_115_i1, d_118, tora_116_i1, 
d_119, ciy_116_i1, d_83, qi_116_i1, d_121, bpma_117_i1, d_122, otra_118_i1, 
d_123, dcm_118_i1, d_83, cix_118_i1, d_83, qi_118_i1, d_126, bpma_119_i1, 
d_127, ensub_119_i1, ensec_119_i1, stsec_119_l1, d_128, stac_122_l1, d_129, c_a2_1_1_l1, 
d_130, c_a2_1_2_l1, d_131, c_a2_1_3_l1, d_132, c_a2_1_4_l1, d_131, c_a2_1_5_l1, 
d_131, c_a2_1_6_l1, d_131, c_a2_1_7_l1, d_131, c_a2_1_8_l1, d_137, q_134_l1, 
d_138, cx_134_l1, cy_134_l1, d_139, bpmc_134_l1, d_140, enac_134_l1, stac_134_l1, 
d_141, c_a2_2_1_l1, d_131, c_a2_2_2_l1, d_131, c_a2_2_3_l1, d_131, c_a2_2_4_l1, 
d_131, c_a2_2_5_l1, d_130, c_a2_2_6_l1, d_131, c_a2_2_7_l1, d_132, c_a2_2_8_l1, 
d_149, q_146_l1, d_150, cx_146_l1, cy_146_l1, d_139, bpmr_146_l1, d_140, 
enac_146_l1, stac_146_l1, d_141, c_a2_3_1_l1, d_131, c_a2_3_2_l1, d_131, c_a2_3_3_l1, 
d_131, c_a2_3_4_l1, d_131, c_a2_3_5_l1, d_131, c_a2_3_6_l1, d_131, c_a2_3_7_l1, 
d_131, c_a2_3_8_l1, d_137, q_158_l1, d_162, cx_158_l1, cy_158_l1, d_163, 
bpmc_158_l1, d_164, enac_158_l1, stac_158_l1, d_129, c_a2_4_1_l1, d_131, c_a2_4_2_l1, 
d_131, c_a2_4_3_l1, d_131, c_a2_4_4_l1, d_131, c_a2_4_5_l1, d_131, c_a2_4_6_l1, 
d_131, c_a2_4_7_l1, d_131, c_a2_4_8_l1, d_149, q_170_l1, d_150, cx_170_l1, 
cy_170_l1, d_139, bpmr_170_l1, d_140, enac_170_l1, d_177, ensec_174_l1, match_174_l1, 
stsec_174_b1, stsub_174_b1, d_178, stgrd_175_b1, d_179, tora_175_b1, d_180, bpma_175_b1, 
d_181, qi_176_b1, d_182, ciy_176_b1, d_183, dcm_176_b1, d_184, cix_177_b1, 
d_185, engrd_178_b1, d_186, stgrd_178_b1, d_187, eod_179_b1, d_188, bpma_179_b1, 
d_189, qd_179_b1, d_190, ccx_179_b1, d_191, bcm_180_b1, d_192, otra_180_b1, 
d_193, qd_181_b1, d_194, ccy_181_b1, d_195, bam_181_b1, d_196, mpbpmf_181_b1, 
d_85, bpmf_181_b1, d_198, engrd_181_b1, d_98, stlat_182_b1, d_200, bb_182_b1, 
d_201, bb_191_b1, d_202, bpms_192_b1, d_92, otrs_192_b1, d_204, bb_193_b1, 
d_205, srm_194_b1, d_206, bb_202_b1, d_207, enlat_202_b1, match_202_b1, stlat_202_b1, 
d_208, stgrd_203_b1, d_209, bam_203_b1, d_210, mpbpmf_203_b1, d_85, bpmf_203_b1, 
d_212, tora_203_b1, d_213, ciy_204_b1, d_214, qi_204_b1, d_215, eod_204_b1, 
d_216, cix_205_b1, d_214, qi_205_b1, d_218, bcm_205_b1, d_219, otra_206_b1, 
d_220, engrd_206_b1, d_186, stgrd_206_b1, d_222, bpma_206_b1, d_223, qi_206_b1, 
d_2, match_207_b1, stblock_207_b1, d_225, tdsb_208_b1, d_9, qi_209_b1, d_84, 
engrd_209_b1, d_228, stgrd_209_b1, d_225, cix_209_b1, d_230, bpma_210_b1, d_189, 
qd_210_b1, d_232, ccy_210_b1, d_233, qi_211_b1, d_234, cix_213_b1, d_235, 
bpma_213_b1, d_181, qi_213_b1, d_2, ciy_214_b1, d_186, engrd_214_b1, d_11, 
stgrd_214_b1, d_240, bpma_215_b1, d_181, qi_215_b1, d_214, cix_216_b1, d_243, 
ccy_217_b1, d_244, bpma_217_b1, d_181, qi_217_b1, d_246, match_218_b1, otrb_218_b1, 
d_247, engrd_219_b1, d_11, stgrd_219_b1, d_249, bpma_219_b1, d_250, qd_219_b1, 
d_251, otrb_220_b1, d_252, bpma_221_b1, d_189, qd_221_b1, d_254, ccy_221_b1, 
d_255, dcm_221_b1, d_256, otrb_222_b1, d_252, bpma_223_b1, d_189, qd_223_b1, 
d_259, cfx_223_b1, d_186, engrd_223_b1, d_11, stgrd_224_b1, d_208, otrb_224_b1, 
d_263, qi_224_b1, d_264, bpma_226_b1, d_265, qi_226_b1, d_266, ciy_226_b1, 
d_228, cfx_226_b1, d_235, bpma_227_b1, d_265, qi_227_b1, d_270, engrd_228_b1, 
d_271, enlat_229_b1, ensub_229_b1)
# power supplies 

#  
qi_63_i1.ps_id = 'QI.13.I1'
qi_66_i1.ps_id = 'QI.14.I1'
qi_69_i1.ps_id = 'QI.15.I1'
qi_71_i1.ps_id = 'QI.16.I1'
qi_72_i1.ps_id = 'QI.17.I1'
qi_73_i1.ps_id = 'QI.18.I1'
qi_74_i1.ps_id = 'QI.19.I1'
qi_75_i1.ps_id = 'QI.20.I1'
qi_77_i1.ps_id = 'QI.19.I1'
qi_78_i1.ps_id = 'QI.18.I1'
qi_79_i1.ps_id = 'QI.19.I1'
qi_80_i1.ps_id = 'QI.20.I1'
qi_82_i1.ps_id = 'QI.21.I1'
qi_83_i1.ps_id = 'QI.22.I1'
qi_84_i1.ps_id = 'QI.21.I1'
qi_85_i1.ps_id = 'QI.24.I1'
qi_86_i1.ps_id = 'QI.23.I1'
qi_88_i1.ps_id = 'QI.22.I1'
qi_89_i1.ps_id = 'QI.23.I1'
qi_90_i1.ps_id = 'QI.24.I1'
qi_92_i1.ps_id = 'QI.23.I1'
qi_93_i1.ps_id = 'QI.25.I1'
qi_94_i1.ps_id = 'QI.26.I1'
qi_95_i1.ps_id = 'QI.27.I1'
qi_102_i1.ps_id = 'QI.28.I1'
qi_103_i1.ps_id = 'QI.29.I1'
qi_104_i1.ps_id = 'QI.30.I1'
qi_107_i1.ps_id = 'QI.31.I1'
qi_109_i1.ps_id = 'QI.32.I1'
qi_112_i1.ps_id = 'QI.31.I1'
qi_114_i1.ps_id = 'QI.33.I1'
qi_116_i1.ps_id = 'QI.34.I1'
qi_118_i1.ps_id = 'QI.35.I1'
q_134_l1.ps_id = 'Q.A2.1.L1'
q_146_l1.ps_id = 'Q.A2.2.L1'
q_158_l1.ps_id = 'Q.A2.3.L1'
q_170_l1.ps_id = 'Q.A2.4.L1'
qi_176_b1.ps_id = 'QI.1.B1'
qd_179_b1.ps_id = 'QD.3.B1'
qd_181_b1.ps_id = 'QD.4.B1'
qi_204_b1.ps_id = 'QI.5.B1'
qi_205_b1.ps_id = 'QI.6.B1'
qi_206_b1.ps_id = 'QI.7.B1'
qi_209_b1.ps_id = 'QI.8.B1'
qd_210_b1.ps_id = 'QD.9.B1'
qi_211_b1.ps_id = 'QI.10.B1'
qi_213_b1.ps_id = 'QI.11.B1'
qi_215_b1.ps_id = 'QI.12.B1'
qi_217_b1.ps_id = 'QI.13.B1'
qd_219_b1.ps_id = 'QD.14.B1'
qd_221_b1.ps_id = 'QD.15.B1'
qd_223_b1.ps_id = 'QD.16.B1'
qi_224_b1.ps_id = 'QI.17.B1'
qi_226_b1.ps_id = 'QI.18.B1'
qi_227_b1.ps_id = 'QI.19.B1'

#  
sc_74i_i1.ps_id = 'SC.1.I1'
sc_74ii_i1.ps_id = 'SC.2.I1'
sc_76_i1.ps_id = 'SC.2.I1'
sc_77_i1.ps_id = 'SC.1.I1'
sc_79i_i1.ps_id = 'SC.1.I1'
sc_79ii_i1.ps_id = 'SC.2.I1'
sc_81_i1.ps_id = 'SC.2.I1'
sc_82_i1.ps_id = 'SC.1.I1'
sc_84i_i1.ps_id = 'SC.1.I1'
sc_84ii_i1.ps_id = 'SC.2.I1'
sc_86_i1.ps_id = 'SC.2.I1'
sc_87_i1.ps_id = 'SC.1.I1'
sc_89i_i1.ps_id = 'SC.1.I1'
sc_89ii_i1.ps_id = 'SC.2.I1'
sc_91_i1.ps_id = 'SC.2.I1'
sc_92_i1.ps_id = 'SC.1.I1'

#  

#  
c_a2_1_1_l1.ps_id = 'C.A2.L1'
c_a2_1_2_l1.ps_id = 'C.A2.L1'
c_a2_1_3_l1.ps_id = 'C.A2.L1'
c_a2_1_4_l1.ps_id = 'C.A2.L1'
c_a2_1_5_l1.ps_id = 'C.A2.L1'
c_a2_1_6_l1.ps_id = 'C.A2.L1'
c_a2_1_7_l1.ps_id = 'C.A2.L1'
c_a2_1_8_l1.ps_id = 'C.A2.L1'
c_a2_2_1_l1.ps_id = 'C.A2.L1'
c_a2_2_2_l1.ps_id = 'C.A2.L1'
c_a2_2_3_l1.ps_id = 'C.A2.L1'
c_a2_2_4_l1.ps_id = 'C.A2.L1'
c_a2_2_5_l1.ps_id = 'C.A2.L1'
c_a2_2_6_l1.ps_id = 'C.A2.L1'
c_a2_2_7_l1.ps_id = 'C.A2.L1'
c_a2_2_8_l1.ps_id = 'C.A2.L1'
c_a2_3_1_l1.ps_id = 'C.A2.L1'
c_a2_3_2_l1.ps_id = 'C.A2.L1'
c_a2_3_3_l1.ps_id = 'C.A2.L1'
c_a2_3_4_l1.ps_id = 'C.A2.L1'
c_a2_3_5_l1.ps_id = 'C.A2.L1'
c_a2_3_6_l1.ps_id = 'C.A2.L1'
c_a2_3_7_l1.ps_id = 'C.A2.L1'
c_a2_3_8_l1.ps_id = 'C.A2.L1'
c_a2_4_1_l1.ps_id = 'C.A2.L1'
c_a2_4_2_l1.ps_id = 'C.A2.L1'
c_a2_4_3_l1.ps_id = 'C.A2.L1'
c_a2_4_4_l1.ps_id = 'C.A2.L1'
c_a2_4_5_l1.ps_id = 'C.A2.L1'
c_a2_4_6_l1.ps_id = 'C.A2.L1'
c_a2_4_7_l1.ps_id = 'C.A2.L1'
c_a2_4_8_l1.ps_id = 'C.A2.L1'

#  
bl_73_i1.ps_id = 'BL.6.I1'
bl_75_i1.ps_id = 'BL.7.I1'
bl_76_i1.ps_id = 'BL.7.I1'
bl_77_i1.ps_id = 'BL.6.I1'
bl_78_i1.ps_id = 'BL.6.I1'
bl_80_i1.ps_id = 'BL.7.I1'
bl_81_i1.ps_id = 'BL.7.I1'
bl_82_i1.ps_id = 'BL.6.I1'
bl_83_i1.ps_id = 'BL.8.I1'
bl_85_i1.ps_id = 'BL.7.I1'
bl_86_i1.ps_id = 'BL.7.I1'
bl_87_i1.ps_id = 'BL.8.I1'
bl_88_i1.ps_id = 'BL.8.I1'
bl_90_i1.ps_id = 'BL.7.I1'
bl_91_i1.ps_id = 'BL.7.I1'
bl_92_i1.ps_id = 'BL.8.I1'
bb_96_i1.ps_id = 'BB.1.I1'
bb_98_i1.ps_id = 'BB.1.I1'
bb_100_i1.ps_id = 'BB.1.I1'
bb_101_i1.ps_id = 'BB.1.I1'
bb_182_b1.ps_id = 'BB.1.B1'
bb_191_b1.ps_id = 'BB.1.B1'
bb_193_b1.ps_id = 'BB.1.B1'
bb_202_b1.ps_id = 'BB.1.B1'
