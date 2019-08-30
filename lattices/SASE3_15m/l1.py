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
d_85 = Drift(l=0.3, eid='D_85')
d_87 = Drift(l=0.481747, eid='D_87')
d_88 = Drift(l=1.008384, eid='D_88')
d_89 = Drift(l=0.865597, eid='D_89')
d_90 = Drift(l=0.31, eid='D_90')
d_91 = Drift(l=0.325597, eid='D_91')
d_92 = Drift(l=1.008385, eid='D_92')
d_93 = Drift(l=0.491746, eid='D_93')
d_95 = Drift(l=0.25, eid='D_95')
d_96 = Drift(l=0.24, eid='D_96')
d_99 = Drift(l=0.56, eid='D_99')
d_102 = Drift(l=1.89, eid='D_102')
d_111 = Drift(l=2.04, eid='D_111')
d_114 = Drift(l=1.1242, eid='D_114')
d_115 = Drift(l=0.1408, eid='D_115')
d_117 = Drift(l=0.13965, eid='D_117')
d_118 = Drift(l=1.09132, eid='D_118')
d_119 = Drift(l=0.44018, eid='D_119')
d_121 = Drift(l=0.14395, eid='D_121')
d_122 = Drift(l=3.923801, eid='D_122')
d_123 = Drift(l=0.345899, eid='D_123')
d_124 = Drift(l=0.3459, eid='D_124')
d_125 = Drift(l=0.345901, eid='D_125')
d_130 = Drift(l=0.2475, eid='D_130')
d_131 = Drift(l=0.0432, eid='D_131')
d_132 = Drift(l=0.085, eid='D_132')
d_133 = Drift(l=0.6795, eid='D_133')
d_141 = Drift(l=0.247499, eid='D_141')
d_142 = Drift(l=0.043201, eid='D_142')
d_153 = Drift(l=0.043199, eid='D_153')
d_154 = Drift(l=0.085001, eid='D_154')
d_166 = Drift(l=5.253899, eid='D_166')
d_167 = Drift(l=0.248001, eid='D_167')
d_168 = Drift(l=0.15215, eid='D_168')
d_169 = Drift(l=0.082149, eid='D_169')
d_170 = Drift(l=1.215001, eid='D_170')
d_171 = Drift(l=1.613, eid='D_171')
d_172 = Drift(l=0.15265, eid='D_172')
d_173 = Drift(l=0.131649, eid='D_173')
d_174 = Drift(l=0.650001, eid='D_174')
d_175 = Drift(l=0.231649, eid='D_175')
d_176 = Drift(l=0.10165, eid='D_176')
d_177 = Drift(l=0.3555, eid='D_177')
d_178 = Drift(l=0.524605, eid='D_178')
d_179 = Drift(l=8.510829, eid='D_179')
d_180 = Drift(l=0.865104, eid='D_180')
d_182 = Drift(l=0.325104, eid='D_182')
d_184 = Drift(l=0.775104, eid='D_184')
d_185 = Drift(l=0.3548, eid='D_185')
d_186 = Drift(l=0.1542, eid='D_186')
d_187 = Drift(l=0.09715, eid='D_187')
d_188 = Drift(l=0.66515, eid='D_188')
d_190 = Drift(l=0.62315, eid='D_190')
d_191 = Drift(l=0.536, eid='D_191')
d_192 = Drift(l=0.15315, eid='D_192')
d_195 = Drift(l=0.53115, eid='D_195')
d_196 = Drift(l=0.379, eid='D_196')
d_198 = Drift(l=0.13165, eid='D_198')
d_199 = Drift(l=1.03115, eid='D_199')
d_200 = Drift(l=1.23015, eid='D_200')
d_201 = Drift(l=0.18, eid='D_201')
d_204 = Drift(l=1.329, eid='D_204')
d_207 = Drift(l=1.066, eid='D_207')
d_208 = Drift(l=0.147, eid='D_208')
d_210 = Drift(l=0.83115, eid='D_210')
d_211 = Drift(l=0.699, eid='D_211')
d_212 = Drift(l=0.13265, eid='D_212')
d_213 = Drift(l=0.83165, eid='D_213')
d_214 = Drift(l=0.679, eid='D_214')
d_216 = Drift(l=0.10765, eid='D_216')
d_217 = Drift(l=0.624, eid='D_217')
d_220 = Drift(l=0.18165, eid='D_220')
d_221 = Drift(l=0.55, eid='D_221')
d_222 = Drift(l=0.34615, eid='D_222')
d_223 = Drift(l=1.22815, eid='D_223')
d_224 = Drift(l=0.152151, eid='D_224')
d_225 = Drift(l=0.081151, eid='D_225')
d_226 = Drift(l=0.15, eid='D_226')
d_229 = Drift(l=1.494401, eid='D_229')

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
tora_94_i1 = Marker(eid='TORA.94.I1')
otrs_99_i1 = Marker(eid='OTRS.99.I1')
tora_116_i1 = Marker(eid='TORA.116.I1')
otra_118_i1 = Marker(eid='OTRA.118.I1')
tora_175_b1 = Marker(eid='TORA.175.B1')
otra_180_b1 = Marker(eid='OTRA.180.B1')
otrs_192_b1 = Marker(eid='OTRS.192.B1')
tora_203_b1 = Marker(eid='TORA.203.B1')
otra_206_b1 = Marker(eid='OTRA.206.B1')
otrb_218_b1 = Marker(eid='OTRB.218.B1')
otrb_220_b1 = Marker(eid='OTRB.220.B1')
otrb_222_b1 = Marker(eid='OTRB.222.B1')
otrb_224_b1 = Marker(eid='OTRB.224.B1')
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
cell = (ensub_62_i1, d_1, ciy_63_i1, d_2, qi_63_i1, d_3, bpma_63_i1, 
d_4, cix_65_i1, d_5, qi_66_i1, d_6, qi_69_i1, d_7, qi_71_i1, 
d_8, bpma_72_i1, d_9, qi_72_i1, d_9, ciy_72_i1, d_11, cix_73i_i1, 
d_2, qi_73_i1, d_13, bl_73_i1, d_14, cix_73ii_i1, d_15, sc_74i_i1, 
d_16, qi_74_i1, d_16, sc_74ii_i1, d_18, bl_75_i1, d_19, bpma_75_i1, 
d_20, ciy_75_i1, d_21, qi_75_i1, d_22, cix_76_i1, d_23, bl_76_i1, 
d_18, sc_76_i1, d_16, qi_77_i1, d_16, sc_77_i1, d_27, bpma_77_i1, 
d_28, bl_77_i1, d_13, qi_78_i1, d_30, bl_78_i1, d_14, cix_78_i1, 
d_15, sc_79i_i1, d_16, qi_79_i1, d_16, sc_79ii_i1, d_35, bl_80_i1, 
d_19, bpma_80_i1, d_20, ciy_80_i1, d_21, qi_80_i1, d_22, cix_81_i1, 
d_40, bl_81_i1, d_18, sc_81_i1, d_16, qi_82_i1, d_16, sc_82_i1, 
d_44, bpma_82_i1, d_45, bl_82_i1, d_13, qi_83_i1, d_13, bl_83_i1, 
d_48, cix_83_i1, d_49, sc_84i_i1, d_16, qi_84_i1, d_16, sc_84ii_i1, 
d_18, bl_85_i1, d_19, bpma_85_i1, d_20, ciy_85_i1, d_21, qi_85_i1, 
d_22, cix_86_i1, d_40, bl_86_i1, d_35, sc_86_i1, d_16, qi_86_i1, 
d_16, sc_87_i1, d_27, bpma_87_i1, d_45, bl_87_i1, d_13, qi_88_i1, 
d_13, bl_88_i1, d_14, cix_88_i1, d_15, sc_89i_i1, d_16, qi_89_i1, 
d_16, sc_89ii_i1, d_35, bl_90_i1, d_19, bpma_90_i1, d_20, cix_90_i1, 
d_21, qi_90_i1, d_73, bl_91_i1, d_18, sc_91_i1, d_16, qi_92_i1, 
d_16, sc_92_i1, d_77, ciy_92_i1, d_20, bpma_92_i1, d_28, bl_92_i1, 
d_13, qi_93_i1, d_81, tora_94_i1, d_11, ciy_94_i1, d_83, qi_94_i1, 
d_84, bpmf_95_i1, d_85, cix_95_i1, d_83, qi_95_i1, d_87, bb_96_i1, 
d_88, bb_98_i1, d_89, bpms_99_i1, d_90, otrs_99_i1, d_91, bb_100_i1, 
d_92, bb_101_i1, d_93, qi_102_i1, d_83, cix_102_i1, d_95, bpmf_103_i1, 
d_96, ciy_103_i1, d_83, qi_103_i1, d_9, bpma_103_i1, d_99, cix_104_i1, 
d_83, qi_104_i1, d_9, bpma_105_i1, d_102, ciy_107_i1, d_83, qi_107_i1, 
d_9, bpma_107_i1, d_102, cix_109_i1, d_83, qi_109_i1, d_9, bpma_110_i1, 
d_102, ciy_112_i1, d_83, qi_112_i1, d_9, bpma_112_i1, d_111, cix_114_i1, 
d_83, qi_114_i1, d_9, bpma_115_i1, d_114, tora_116_i1, d_115, ciy_116_i1, 
d_83, qi_116_i1, d_117, bpma_117_i1, d_118, otra_118_i1, d_119, cix_118_i1, 
d_83, qi_118_i1, d_121, bpma_119_i1, d_122, c_a2_1_1_l1, d_123, c_a2_1_2_l1, 
d_124, c_a2_1_3_l1, d_125, c_a2_1_4_l1, d_124, c_a2_1_5_l1, d_124, c_a2_1_6_l1, 
d_124, c_a2_1_7_l1, d_124, c_a2_1_8_l1, d_130, q_134_l1, d_131, cx_134_l1, 
cy_134_l1, d_132, bpmc_134_l1, d_133, c_a2_2_1_l1, d_124, c_a2_2_2_l1, d_124, 
c_a2_2_3_l1, d_124, c_a2_2_4_l1, d_124, c_a2_2_5_l1, d_123, c_a2_2_6_l1, d_124, 
c_a2_2_7_l1, d_125, c_a2_2_8_l1, d_141, q_146_l1, d_142, cx_146_l1, cy_146_l1, 
d_132, bpmr_146_l1, d_133, c_a2_3_1_l1, d_124, c_a2_3_2_l1, d_124, c_a2_3_3_l1, 
d_124, c_a2_3_4_l1, d_124, c_a2_3_5_l1, d_124, c_a2_3_6_l1, d_124, c_a2_3_7_l1, 
d_124, c_a2_3_8_l1, d_130, q_158_l1, d_153, cx_158_l1, cy_158_l1, d_154, 
bpmc_158_l1, d_133, c_a2_4_1_l1, d_124, c_a2_4_2_l1, d_124, c_a2_4_3_l1, d_124, 
c_a2_4_4_l1, d_124, c_a2_4_5_l1, d_124, c_a2_4_6_l1, d_124, c_a2_4_7_l1, d_124, 
c_a2_4_8_l1, d_141, q_170_l1, d_142, cx_170_l1, cy_170_l1, d_132, bpmr_170_l1, 
d_166, tora_175_b1, d_167, bpma_175_b1, d_168, qi_176_b1, d_169, ciy_176_b1, 
d_170, cix_177_b1, d_171, bpma_179_b1, d_172, qd_179_b1, d_173, ccx_179_b1, 
d_174, otra_180_b1, d_175, qd_181_b1, d_176, ccy_181_b1, d_177, bpmf_181_b1, 
d_178, bb_182_b1, d_179, bb_191_b1, d_180, bpms_192_b1, d_90, otrs_192_b1, 
d_182, bb_193_b1, d_179, bb_202_b1, d_184, bpmf_203_b1, d_185, tora_203_b1, 
d_186, ciy_204_b1, d_187, qi_204_b1, d_188, cix_205_b1, d_187, qi_205_b1, 
d_190, otra_206_b1, d_191, bpma_206_b1, d_192, qi_206_b1, d_9, tdsb_208_b1, 
d_9, qi_209_b1, d_195, cix_209_b1, d_196, bpma_210_b1, d_172, qd_210_b1, 
d_198, ccy_210_b1, d_199, qi_211_b1, d_200, cix_213_b1, d_201, bpma_213_b1, 
d_168, qi_213_b1, d_2, ciy_214_b1, d_204, bpma_215_b1, d_168, qi_215_b1, 
d_187, cix_216_b1, d_207, ccy_217_b1, d_208, bpma_217_b1, d_168, qi_217_b1, 
d_210, otrb_218_b1, d_211, bpma_219_b1, d_212, qd_219_b1, d_213, otrb_220_b1, 
d_214, bpma_221_b1, d_172, qd_221_b1, d_216, ccy_221_b1, d_217, otrb_222_b1, 
d_214, bpma_223_b1, d_172, qd_223_b1, d_220, cfx_223_b1, d_221, otrb_224_b1, 
d_222, qi_224_b1, d_223, bpma_226_b1, d_224, qi_226_b1, d_225, ciy_226_b1, 
d_226, cfx_226_b1, d_201, bpma_227_b1, d_224, qi_227_b1, d_229, ensub_229_b1)
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
