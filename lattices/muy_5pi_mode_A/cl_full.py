from ocelot import * 
tws = Twiss()
tws.beta_x  = 42.0646995916
tws.beta_y  = 58.0284165718
tws.alpha_x = -0.996413599281
tws.alpha_y = 2.16792724498
tws.E = 14
# drifts 
d_1 = Drift(l=6.3887, eid='D_1')
d_2 = Drift(l=0.1, eid='D_2')
d_3 = Drift(l=0.7, eid='D_3')
d_4 = Drift(l=0.20895, eid='D_4')
d_5 = Drift(l=0.15395, eid='D_5')
d_6 = Drift(l=6.21, eid='D_6')
d_7 = Drift(l=0.15545, eid='D_7')
d_8 = Drift(l=0.2209, eid='D_8')
d_9 = Drift(l=0.21045, eid='D_9')
d_10 = Drift(l=0.36045, eid='D_10')
d_13 = Drift(l=0.74395, eid='D_13')
d_15 = Drift(l=0.1718, eid='D_15')
d_16 = Drift(l=0.4418, eid='D_16')
d_17 = Drift(l=0.096, eid='D_17')
d_18 = Drift(l=1.954002, eid='D_18')
d_19 = Drift(l=2.733952, eid='D_19')
d_23 = Drift(l=4.2, eid='D_23')
d_24 = Drift(l=0.45, eid='D_24')
d_25 = Drift(l=1.6918, eid='D_25')
d_26 = Drift(l=0.42575, eid='D_26')
d_31 = Drift(l=1.604, eid='D_31')
d_32 = Drift(l=4.6418, eid='D_32')
d_35 = Drift(l=0.93, eid='D_35')
d_36 = Drift(l=1.550002, eid='D_36')
d_37 = Drift(l=2.491802, eid='D_37')
d_42 = Drift(l=2.050002, eid='D_42')
d_64 = Drift(l=0.38, eid='D_64')
d_65 = Drift(l=0.675, eid='D_65')
d_72 = Drift(l=1.31895, eid='D_72')
d_75 = Drift(l=3.28395, eid='D_75')
d_78 = Drift(l=2.28395, eid='D_78')
d_81 = Drift(l=0.4343, eid='D_81')
d_82 = Drift(l=1.849647, eid='D_82')
d_88 = Drift(l=0.685, eid='D_88')
d_95 = Drift(l=1.30895, eid='D_95')
d_111 = Drift(l=1.7, eid='D_111')
d_142 = Drift(l=0.2168, eid='D_142')
d_145 = Drift(l=0.69, eid='D_145')
d_148 = Drift(l=0.5709, eid='D_148')
d_150 = Drift(l=0.41295, eid='D_150')
d_152 = Drift(l=0.3015, eid='D_152')
d_153 = Drift(l=2.0865, eid='D_153')
d_155 = Drift(l=0.33645, eid='D_155')
d_159 = Drift(l=2.325, eid='D_159')
d_162 = Drift(l=3.855, eid='D_162')
d_165 = Drift(l=4.8525, eid='D_165')
d_167 = Drift(l=2.61545, eid='D_167')
d_168 = Drift(l=2.50395, eid='D_168')
d_169 = Drift(l=4.3525, eid='D_169')
d_172 = Drift(l=2.53395, eid='D_172')
d_173 = Drift(l=4.1, eid='D_173')
d_174 = Drift(l=7.73395, eid='D_174')
d_175 = Drift(l=2.71145, eid='D_175')
d_178 = Drift(l=3.525, eid='D_178')
d_184 = Drift(l=1.2775, eid='D_184')
d_186 = Drift(l=1.0715, eid='D_186')
d_187 = Drift(l=0.3, eid='D_187')
d_188 = Drift(l=2.6775, eid='D_188')
d_189 = Drift(l=2.31145, eid='D_189')
d_191 = Drift(l=1.5025, eid='D_191')
d_193 = Drift(l=0.4815, eid='D_193')
d_194 = Drift(l=0.27, eid='D_194')
d_195 = Drift(l=11.663951, eid='D_195')
d_196 = Drift(l=11.933951, eid='D_196')
d_197 = Drift(l=0.64, eid='D_197')
d_198 = Drift(l=1.285, eid='D_198')
d_199 = Drift(l=0.208951, eid='D_199')
d_200 = Drift(l=0.153951, eid='D_200')
d_201 = Drift(l=0.2, eid='D_201')
d_202 = Drift(l=9.0692, eid='D_202')
d_204 = Drift(l=0.15, eid='D_204')
d_206 = Drift(l=1.86074, eid='D_206')

# quadrupoles 
qf_1660_cl = Quadrupole(l=0.5321, k1=0.1781886453, tilt=0.0, eid='QF.1660.CL')
qh_1667_cl = Quadrupole(l=1.0291, k1=-0.1733525799, tilt=0.0, eid='QH.1667.CL')
qh_1669_cl = Quadrupole(l=1.0291, k1=-0.1733525799, tilt=0.0, eid='QH.1669.CL')
qh_1670_cl = Quadrupole(l=1.0291, k1=0.3395033707, tilt=0.0, eid='QH.1670.CL')
qh_1671_cl = Quadrupole(l=1.0291, k1=0.3395033707, tilt=0.0, eid='QH.1671.CL')
qf_1673_cl = Quadrupole(l=0.5321, k1=-0.3013173384, tilt=0.0, eid='QF.1673.CL')
qf_1682_cl = Quadrupole(l=0.5321, k1=0.3013173384, tilt=0.0, eid='QF.1682.CL')
qf_1691_cl = Quadrupole(l=0.5321, k1=-0.3013173384, tilt=0.0, eid='QF.1691.CL')
qf_1700_cl = Quadrupole(l=0.5321, k1=0.3013173384, tilt=0.0, eid='QF.1700.CL')
qf_1709_cl = Quadrupole(l=0.5321, k1=-0.3013173384, tilt=0.0, eid='QF.1709.CL')
qf_1718_cl = Quadrupole(l=0.5321, k1=0.3013173384, tilt=0.0, eid='QF.1718.CL')
qf_1727_cl = Quadrupole(l=0.5321, k1=-0.3013173384, tilt=0.0, eid='QF.1727.CL')
qf_1736_cl = Quadrupole(l=0.5321, k1=0.3013173384, tilt=0.0, eid='QF.1736.CL')
qf_1745_cl = Quadrupole(l=0.5321, k1=-0.3013173384, tilt=0.0, eid='QF.1745.CL')
qh_1748_cl = Quadrupole(l=1.0291, k1=0.3239105019, tilt=0.0, eid='QH.1748.CL')
qh_1749_cl = Quadrupole(l=1.0291, k1=0.3239105019, tilt=0.0, eid='QH.1749.CL')
qh_1751_cl = Quadrupole(l=1.0291, k1=-0.2257174548, tilt=0.0, eid='QH.1751.CL')
qh_1752_cl = Quadrupole(l=1.0291, k1=-0.2257174548, tilt=0.0, eid='QH.1752.CL')
qf_1754_cl = Quadrupole(l=0.5321, k1=0.1420399288, tilt=0.0, eid='QF.1754.CL')
qf_1759_cl = Quadrupole(l=0.5321, k1=0.1625880644, tilt=0.0, eid='QF.1759.CL')
qf_1763_cl = Quadrupole(l=0.5321, k1=-0.2212328696, tilt=0.0, eid='QF.1763.CL')
qf_1767_cl = Quadrupole(l=0.5321, k1=0.1625880644, tilt=0.0, eid='QF.1767.CL')
qf_1772_cl = Quadrupole(l=0.5321, k1=0.1420399288, tilt=0.0, eid='QF.1772.CL')
qh_1775_cl = Quadrupole(l=1.0291, k1=-0.2257174548, tilt=0.0, eid='QH.1775.CL')
qh_1776_cl = Quadrupole(l=1.0291, k1=-0.2257174548, tilt=0.0, eid='QH.1776.CL')
qh_1778_cl = Quadrupole(l=1.0291, k1=0.3239105019, tilt=0.0, eid='QH.1778.CL')
qh_1779_cl = Quadrupole(l=1.0291, k1=0.3239105019, tilt=0.0, eid='QH.1779.CL')
qf_1781_cl = Quadrupole(l=0.5321, k1=-0.3013173384, tilt=0.0, eid='QF.1781.CL')
qf_1790_cl = Quadrupole(l=0.5321, k1=0.3013173384, tilt=0.0, eid='QF.1790.CL')
qf_1799_cl = Quadrupole(l=0.5321, k1=-0.3013173384, tilt=0.0, eid='QF.1799.CL')
qf_1808_cl = Quadrupole(l=0.5321, k1=0.3013173384, tilt=0.0, eid='QF.1808.CL')
qf_1817_cl = Quadrupole(l=0.5321, k1=-0.3013173384, tilt=0.0, eid='QF.1817.CL')
qf_1826_cl = Quadrupole(l=0.5321, k1=0.3013173384, tilt=0.0, eid='QF.1826.CL')
qf_1835_cl = Quadrupole(l=0.5321, k1=-0.3013173384, tilt=0.0, eid='QF.1835.CL')
qf_1844_cl = Quadrupole(l=0.5321, k1=0.3013173384, tilt=0.0, eid='QF.1844.CL')
qf_1853_cl = Quadrupole(l=0.5321, k1=-0.3013173384, tilt=0.0, eid='QF.1853.CL')
qh_1855_tl = Quadrupole(l=1.0291, k1=0.3716633416, tilt=0.0, eid='QH.1855.TL')
qh_1857_tl = Quadrupole(l=1.0291, k1=0.3460558121, tilt=0.0, eid='QH.1857.TL')
qh_1858_tl = Quadrupole(l=1.0291, k1=-0.3787301585, tilt=0.0, eid='QH.1858.TL')
qh_1859_tl = Quadrupole(l=1.0291, k1=-0.0527740841, tilt=0.0, eid='QH.1859.TL')
qf_1864_tl = Quadrupole(l=0.5321, k1=0.1858986039, tilt=0.0, eid='QF.1864.TL')
qf_1868_tl = Quadrupole(l=0.5321, k1=-0.0551258712, tilt=0.0, eid='QF.1868.TL')
qf_1873_tl = Quadrupole(l=0.5321, k1=0.1199289292, tilt=0.0, eid='QF.1873.TL')
qf_1881_tl = Quadrupole(l=0.5321, k1=-0.2009347131, tilt=0.0, eid='QF.1881.TL')
qf_1892_tl = Quadrupole(l=0.5321, k1=0.1791908476, tilt=0.0, eid='QF.1892.TL')
qf_1907_tl = Quadrupole(l=0.5321, k1=-0.1791908476, tilt=0.0, eid='QF.1907.TL')
qf_1922_tl = Quadrupole(l=0.5321, k1=0.1791908476, tilt=0.0, eid='QF.1922.TL')
qf_1937_tl = Quadrupole(l=0.5321, k1=-0.1791908476, tilt=0.0, eid='QF.1937.TL')
qf_1952_tl = Quadrupole(l=0.5321, k1=0.1791908476, tilt=0.0, eid='QF.1952.TL')
qf_1967_tl = Quadrupole(l=0.5321, k1=-0.1791908476, tilt=0.0, eid='QF.1967.TL')

# bending magnets 
be_1678_cl = SBend(l=2.5, angle=0.006233024763, e1=0.003116512, e2=0.003116512, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BE.1678.CL')
bl_1688_cl = SBend(l=0.2, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.1688.CL')
bl_1695_cl = SBend(l=0.2, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.1695.CL')
be_1705_cl = SBend(l=2.5, angle=0.006233024763, e1=0.003116512, e2=0.003116512, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BE.1705.CL')
be_1714_cl = SBend(l=2.5, angle=0.006233024763, e1=0.003116512, e2=0.003116512, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BE.1714.CL')
bl_1724_cl = SBend(l=0.2, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.1724.CL')
bl_1731_cl = SBend(l=0.2, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.1731.CL')
be_1741_cl = SBend(l=2.5, angle=0.006233024763, e1=0.003116512, e2=0.003116512, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BE.1741.CL')
be_1786_cl = SBend(l=2.5, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BE.1786.CL')
bl_1796_cl = SBend(l=0.2, angle=0.000724902792, e1=0.000362451, e2=0.000362451, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.1796.CL')
bl_1803_cl = SBend(l=0.2, angle=0.000724902792, e1=0.000362451, e2=0.000362451, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.1803.CL')
be_1813_cl = SBend(l=2.5, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BE.1813.CL')
be_1822_cl = SBend(l=2.5, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BE.1822.CL')
bl_1832_cl = SBend(l=0.2, angle=0.000724902792, e1=0.000362451, e2=0.000362451, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.1832.CL')
bl_1839_cl = SBend(l=0.2, angle=0.000724902792, e1=0.000362451, e2=0.000362451, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.1839.CL')
be_1849_cl = SBend(l=2.5, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BE.1849.CL')

# correctors 
cfx_1660_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1660.CL')
chy_1667_cl = Vcor(l=0.2, angle=0.0, eid='CHY.1667.CL')
chx_1672_cl = Hcor(l=0.2, angle=0.0, eid='CHX.1672.CL')
cfy_1674_cl = Vcor(l=0.1, angle=0.0, eid='CFY.1674.CL')
cfx_1683_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1683.CL')
cfy_1692_cl = Vcor(l=0.1, angle=0.0, eid='CFY.1692.CL')
cfx_1701_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1701.CL')
cfy_1710_cl = Vcor(l=0.1, angle=0.0, eid='CFY.1710.CL')
cfx_1719_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1719.CL')
cfy_1728_cl = Vcor(l=0.1, angle=0.0, eid='CFY.1728.CL')
cfx_1737_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1737.CL')
cfy_1746_cl = Vcor(l=0.1, angle=0.0, eid='CFY.1746.CL')
chx_1747_cl = Hcor(l=0.2, angle=0.0, eid='CHX.1747.CL')
chy_1753_cl = Vcor(l=0.2, angle=0.0, eid='CHY.1753.CL')
cfx_1755_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1755.CL')
cfy_1760_cl = Vcor(l=0.1, angle=0.0, eid='CFY.1760.CL')
cfx_1764_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1764.CL')
cfy_1768_cl = Vcor(l=0.1, angle=0.0, eid='CFY.1768.CL')
cfx_1773_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1773.CL')
chy_1774_cl = Vcor(l=0.2, angle=0.0, eid='CHY.1774.CL')
chx_1780_cl = Hcor(l=0.2, angle=0.0, eid='CHX.1780.CL')
cfy_1782_cl = Vcor(l=0.1, angle=0.0, eid='CFY.1782.CL')
cfx_1791_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1791.CL')
cfy_1800_cl = Vcor(l=0.1, angle=0.0, eid='CFY.1800.CL')
cfx_1809_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1809.CL')
cfy_1818_cl = Vcor(l=0.1, angle=0.0, eid='CFY.1818.CL')
cfx_1827_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1827.CL')
cfy_1836_cl = Vcor(l=0.1, angle=0.0, eid='CFY.1836.CL')
cfx_1845_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1845.CL')
cfy_1854_tl = Vcor(l=0.1, angle=0.0, eid='CFY.1854.TL')
chx_1855_tl = Hcor(l=0.2, angle=0.0, eid='CHX.1855.TL')
chy_1861_tl = Vcor(l=0.2, angle=0.0, eid='CHY.1861.TL')
cfx_1864_tl = Hcor(l=0.1, angle=0.0, eid='CFX.1864.TL')
cfy_1869_tl = Vcor(l=0.1, angle=0.0, eid='CFY.1869.TL')
cfx_1873_tl = Hcor(l=0.1, angle=0.0, eid='CFX.1873.TL')
cfy_1884_tl = Vcor(l=0.1, angle=0.0, eid='CFY.1884.TL')
cfx_1894_tl = Hcor(l=0.1, angle=0.0, eid='CFX.1894.TL')
cfy_1910_tl = Vcor(l=0.1, angle=0.0, eid='CFY.1910.TL')
cfx_1925_tl = Hcor(l=0.1, angle=0.0, eid='CFX.1925.TL')
cfy_1937_tl = Vcor(l=0.1, angle=0.0, eid='CFY.1937.TL')
bl_1939_tl = Hcor(l=0.2, angle=0.0, eid='BL.1939.TL')
bl_1964_tl = Hcor(l=0.2, angle=0.0, eid='BL.1964.TL')
chx_1965_tl = Hcor(l=0.2, angle=0.0, eid='CHX.1965.TL')
chx_1967_tl = Hcor(l=0.2, angle=0.0, eid='CHX.1967.TL')
chy_1967_tl = Vcor(l=0.2, angle=0.0, eid='CHY.1967.TL')
cnx_1977_tl = Hcor(l=0.3, angle=0.0, eid='CNX.1977.TL')
cny_1977_tl = Vcor(l=0.3, angle=0.0, eid='CNY.1977.TL')

# markers 
stblock_1652_cl = Marker(eid='STBLOCK.1652.CL')
tora_1658_cl = Marker(eid='TORA.1658.CL')
dcm_1659_cl = Marker(eid='DCM.1659.CL')
match_1673_cl = Marker(eid='MATCH.1673.CL')
mpbpmi_1675_cl = Marker(eid='MPBPMI.1675.CL')
otrb_1689_cl = Marker(eid='OTRB.1689.CL')
mpbpmi_1693_cl = Marker(eid='MPBPMI.1693.CL')
otrb_1725_cl = Marker(eid='OTRB.1725.CL')
mpbpmi_1729_cl = Marker(eid='MPBPMI.1729.CL')
tora_1765_cl = Marker(eid='TORA.1765.CL')
otrb_1797_cl = Marker(eid='OTRB.1797.CL')
otrb_1833_cl = Marker(eid='OTRB.1833.CL')
mpbpmi_1837_cl = Marker(eid='MPBPMI.1837.CL')
ensec_1854_cl = Marker(eid='ENSEC.1854.CL')
stsec_1854_tl = Marker(eid='STSEC.1854.TL')
stsub_1854_tl = Marker(eid='STSUB.1854.TL')
mpbpmi_1861_tl = Marker(eid='MPBPMI.1861.TL')
mpbpmi_1863_tl = Marker(eid='MPBPMI.1863.TL')
tora_1865_tl = Marker(eid='TORA.1865.TL')
dcm_1865_tl = Marker(eid='DCM.1865.TL')
mpbpmi_1878_tl = Marker(eid='MPBPMI.1878.TL')
mpbpmi_1889_tl = Marker(eid='MPBPMI.1889.TL')
enblock_1891_cl = Marker(eid='ENBLOCK.1891.CL')
otrbw_1899_tl = Marker(eid='OTRBW.1899.TL')
mpbpmi_1910_tl = Marker(eid='MPBPMI.1910.TL')
otrbw_1914_tl = Marker(eid='OTRBW.1914.TL')
mpbpmi_1925_tl = Marker(eid='MPBPMI.1925.TL')
otrbw_1929_tl = Marker(eid='OTRBW.1929.TL')
mpbpmi_1930_tl = Marker(eid='MPBPMI.1930.TL')
bam_1931_tl = Marker(eid='BAM.1931.TL')
bam_1932_tl = Marker(eid='BAM.1932.TL')
crd_1934_tl = Marker(eid='CRD.1934.TL')
mpbpmi_1939_tl = Marker(eid='MPBPMI.1939.TL')
ensub_1940_tl = Marker(eid='ENSUB.1940.TL')
stsub_1940_tl = Marker(eid='STSUB.1940.TL')
otre_1978_tl = Marker(eid='OTRE.1978.TL')
ensub_1980_tl = Marker(eid='ENSUB.1980.TL')

# monitor 
bpma_1659_cl = Monitor(eid='BPMA.1659.CL')
bpma_1669_cl = Monitor(eid='BPMA.1669.CL')
bpmi_1675_cl = Monitor(eid='BPMI.1675.CL')
bpma_1684_cl = Monitor(eid='BPMA.1684.CL')
bpmi_1693_cl = Monitor(eid='BPMI.1693.CL')
bpma_1702_cl = Monitor(eid='BPMA.1702.CL')
bpma_1711_cl = Monitor(eid='BPMA.1711.CL')
bpma_1720_cl = Monitor(eid='BPMA.1720.CL')
bpmi_1729_cl = Monitor(eid='BPMI.1729.CL')
bpma_1738_cl = Monitor(eid='BPMA.1738.CL')
bpma_1746_cl = Monitor(eid='BPMA.1746.CL')
bpma_1750_cl = Monitor(eid='BPMA.1750.CL')
bpma_1756_cl = Monitor(eid='BPMA.1756.CL')
bpma_1761_cl = Monitor(eid='BPMA.1761.CL')
bpma_1765_cl = Monitor(eid='BPMA.1765.CL')
bpma_1769_cl = Monitor(eid='BPMA.1769.CL')
bpma_1773_cl = Monitor(eid='BPMA.1773.CL')
bpma_1777_cl = Monitor(eid='BPMA.1777.CL')
bpma_1783_cl = Monitor(eid='BPMA.1783.CL')
bpma_1792_cl = Monitor(eid='BPMA.1792.CL')
bpma_1801_cl = Monitor(eid='BPMA.1801.CL')
bpma_1810_cl = Monitor(eid='BPMA.1810.CL')
bpma_1819_cl = Monitor(eid='BPMA.1819.CL')
bpma_1828_cl = Monitor(eid='BPMA.1828.CL')
bpmi_1837_cl = Monitor(eid='BPMI.1837.CL')
bpma_1846_cl = Monitor(eid='BPMA.1846.CL')
bpma_1853_cl = Monitor(eid='BPMA.1853.CL')
bpmi_1860_tl = Monitor(eid='BPMI.1860.TL')
bpmi_1863_tl = Monitor(eid='BPMI.1863.TL')
bpma_1868_tl = Monitor(eid='BPMA.1868.TL')
bpma_1873_tl = Monitor(eid='BPMA.1873.TL')
bpmi_1878_tl = Monitor(eid='BPMI.1878.TL')
bpmi_1889_tl = Monitor(eid='BPMI.1889.TL')
bpmi_1910_tl = Monitor(eid='BPMI.1910.TL')
bpmi_1925_tl = Monitor(eid='BPMI.1925.TL')
bpmi_1930_tl = Monitor(eid='BPMI.1930.TL')
bpmi_1939_tl = Monitor(eid='BPMI.1939.TL')
bpma_1966_tl = Monitor(eid='BPMA.1966.TL')
bpmd_1977_tl = Monitor(eid='BPMD.1977.TL')

# sextupoles 
sa_1674_cl = Sextupole(l=0.3164, k2=5.577060799324, tilt=1.570796327, eid='SA.1674.CL')
sa_1683_cl = Sextupole(l=0.3164, k2=-4.689136800824, tilt=1.570796327, eid='SA.1683.CL')
sa_1691_cl = Sextupole(l=0.3164, k2=0.903939326774, tilt=1.570796327, eid='SA.1691.CL')
sa_1692_cl = Sextupole(l=0.3164, k2=0.903939326774, tilt=1.570796327, eid='SA.1692.CL')
sa_1700_cl = Sextupole(l=0.3164, k2=-4.689136800824, tilt=1.570796327, eid='SA.1700.CL')
sa_1708_cl = Sextupole(l=0.3164, k2=5.577060799324, tilt=1.570796327, eid='SA.1708.CL')
sa_1710_cl = Sextupole(l=0.3164, k2=5.577060799324, tilt=1.570796327, eid='SA.1710.CL')
sa_1719_cl = Sextupole(l=0.3164, k2=-4.689136800824, tilt=1.570796327, eid='SA.1719.CL')
sa_1726_cl = Sextupole(l=0.3164, k2=0.903939326774, tilt=1.570796327, eid='SA.1726.CL')
sa_1728_cl = Sextupole(l=0.3164, k2=0.903939326774, tilt=1.570796327, eid='SA.1728.CL')
sa_1736_cl = Sextupole(l=0.3164, k2=-4.689136800824, tilt=1.570796327, eid='SA.1736.CL')
sa_1744_cl = Sextupole(l=0.3164, k2=5.577060799324, tilt=1.570796327, eid='SA.1744.CL')
sa_1782_cl = Sextupole(l=0.3164, k2=-5.577060799324, tilt=1.570796327, eid='SA.1782.CL')
sa_1791_cl = Sextupole(l=0.3164, k2=4.689136800824, tilt=1.570796327, eid='SA.1791.CL')
sa_1798_cl = Sextupole(l=0.3164, k2=-0.903939326774, tilt=1.570796327, eid='SA.1798.CL')
sa_1800_cl = Sextupole(l=0.3164, k2=-0.903939326774, tilt=1.570796327, eid='SA.1800.CL')
sa_1808_cl = Sextupole(l=0.3164, k2=4.689136800824, tilt=1.570796327, eid='SA.1808.CL')
sa_1816_cl = Sextupole(l=0.3164, k2=-5.577060799324, tilt=1.570796327, eid='SA.1816.CL')
sa_1818_cl = Sextupole(l=0.3164, k2=-5.577060799324, tilt=1.570796327, eid='SA.1818.CL')
sa_1827_cl = Sextupole(l=0.3164, k2=4.689136800824, tilt=1.570796327, eid='SA.1827.CL')
sa_1834_cl = Sextupole(l=0.3164, k2=-0.903939326774, tilt=1.570796327, eid='SA.1834.CL')
sa_1836_cl = Sextupole(l=0.3164, k2=-0.903939326774, tilt=1.570796327, eid='SA.1836.CL')
sa_1844_cl = Sextupole(l=0.3164, k2=4.689136800824, tilt=1.570796327, eid='SA.1844.CL')
sa_1852_cl = Sextupole(l=0.3164, k2=-5.577060799324, tilt=1.570796327, eid='SA.1852.CL')

# octupole 

# undulator 

# cavity 

# tdcavity 

# UnknowElement 

# Matrices 

# Solenoids 

# lattice 
cell = (stblock_1652_cl, d_1, tora_1658_cl, d_2, dcm_1659_cl, d_3, bpma_1659_cl, 
d_4, qf_1660_cl, d_5, cfx_1660_cl, d_6, chy_1667_cl, d_7, qh_1667_cl, 
d_8, qh_1669_cl, d_9, bpma_1669_cl, d_10, qh_1670_cl, d_8, qh_1671_cl, 
d_7, chx_1672_cl, d_13, match_1673_cl, qf_1673_cl, d_5, cfy_1674_cl, d_15, 
sa_1674_cl, d_16, bpmi_1675_cl, d_17, mpbpmi_1675_cl, d_18, be_1678_cl, d_19, 
qf_1682_cl, d_5, cfx_1683_cl, d_15, sa_1683_cl, d_16, bpma_1684_cl, d_23, 
bl_1688_cl, d_24, otrb_1689_cl, d_25, sa_1691_cl, d_26, qf_1691_cl, d_5, 
cfy_1692_cl, d_15, sa_1692_cl, d_16, bpmi_1693_cl, d_17, mpbpmi_1693_cl, d_31, 
bl_1695_cl, d_32, sa_1700_cl, d_26, qf_1700_cl, d_5, cfx_1701_cl, d_35, 
bpma_1702_cl, d_36, be_1705_cl, d_37, sa_1708_cl, d_26, qf_1709_cl, d_5, 
cfy_1710_cl, d_15, sa_1710_cl, d_16, bpma_1711_cl, d_42, be_1714_cl, d_19, 
qf_1718_cl, d_5, cfx_1719_cl, d_15, sa_1719_cl, d_16, bpma_1720_cl, d_23, 
bl_1724_cl, d_24, otrb_1725_cl, d_25, sa_1726_cl, d_26, qf_1727_cl, d_5, 
cfy_1728_cl, d_15, sa_1728_cl, d_16, bpmi_1729_cl, d_17, mpbpmi_1729_cl, d_31, 
bl_1731_cl, d_32, sa_1736_cl, d_26, qf_1736_cl, d_5, cfx_1737_cl, d_35, 
bpma_1738_cl, d_36, be_1741_cl, d_37, sa_1744_cl, d_26, qf_1745_cl, d_5, 
cfy_1746_cl, d_64, bpma_1746_cl, d_65, chx_1747_cl, d_7, qh_1748_cl, d_8, 
qh_1749_cl, d_9, bpma_1750_cl, d_10, qh_1751_cl, d_8, qh_1752_cl, d_7, 
chy_1753_cl, d_72, qf_1754_cl, d_5, cfx_1755_cl, d_35, bpma_1756_cl, d_75, 
qf_1759_cl, d_5, cfy_1760_cl, d_35, bpma_1761_cl, d_78, qf_1763_cl, d_5, 
cfx_1764_cl, d_35, bpma_1765_cl, d_81, tora_1765_cl, d_82, qf_1767_cl, d_5, 
cfy_1768_cl, d_35, bpma_1769_cl, d_75, qf_1772_cl, d_5, cfx_1773_cl, d_64, 
bpma_1773_cl, d_88, chy_1774_cl, d_7, qh_1775_cl, d_8, qh_1776_cl, d_9, 
bpma_1777_cl, d_10, qh_1778_cl, d_8, qh_1779_cl, d_7, chx_1780_cl, d_95, 
qf_1781_cl, d_5, cfy_1782_cl, d_15, sa_1782_cl, d_16, bpma_1783_cl, d_42, 
be_1786_cl, d_19, qf_1790_cl, d_5, cfx_1791_cl, d_15, sa_1791_cl, d_16, 
bpma_1792_cl, d_23, bl_1796_cl, d_24, otrb_1797_cl, d_25, sa_1798_cl, d_26, 
qf_1799_cl, d_5, cfy_1800_cl, d_15, sa_1800_cl, d_16, bpma_1801_cl, d_111, 
bl_1803_cl, d_32, sa_1808_cl, d_26, qf_1808_cl, d_5, cfx_1809_cl, d_35, 
bpma_1810_cl, d_36, be_1813_cl, d_37, sa_1816_cl, d_26, qf_1817_cl, d_5, 
cfy_1818_cl, d_15, sa_1818_cl, d_16, bpma_1819_cl, d_42, be_1822_cl, d_19, 
qf_1826_cl, d_5, cfx_1827_cl, d_15, sa_1827_cl, d_16, bpma_1828_cl, d_23, 
bl_1832_cl, d_24, otrb_1833_cl, d_25, sa_1834_cl, d_26, qf_1835_cl, d_5, 
cfy_1836_cl, d_15, sa_1836_cl, d_16, bpmi_1837_cl, d_17, mpbpmi_1837_cl, d_31, 
bl_1839_cl, d_32, sa_1844_cl, d_26, qf_1844_cl, d_5, cfx_1845_cl, d_35, 
bpma_1846_cl, d_36, be_1849_cl, d_37, sa_1852_cl, d_142, bpma_1853_cl, d_4, 
qf_1853_cl, ensec_1854_cl, stsec_1854_tl, stsub_1854_tl, d_5, cfy_1854_tl, d_145, chx_1855_tl, 
d_7, qh_1855_tl, d_8, qh_1857_tl, d_148, qh_1858_tl, d_8, qh_1859_tl, 
d_150, bpmi_1860_tl, d_17, mpbpmi_1861_tl, d_152, chy_1861_tl, d_153, mpbpmi_1863_tl, 
d_17, bpmi_1863_tl, d_155, qf_1864_tl, d_5, cfx_1864_tl, d_35, tora_1865_tl, 
d_2, dcm_1865_tl, d_159, bpma_1868_tl, d_4, qf_1868_tl, d_5, cfy_1869_tl, 
d_162, bpma_1873_tl, d_4, qf_1873_tl, d_5, cfx_1873_tl, d_165, bpmi_1878_tl, 
d_17, mpbpmi_1878_tl, d_167, qf_1881_tl, d_168, cfy_1884_tl, d_169, bpmi_1889_tl, 
d_17, mpbpmi_1889_tl, d_167, enblock_1891_cl, qf_1892_tl, d_172, cfx_1894_tl, d_173, 
otrbw_1899_tl, d_174, qf_1907_tl, d_175, bpmi_1910_tl, d_17, mpbpmi_1910_tl, d_152, 
cfy_1910_tl, d_178, otrbw_1914_tl, d_174, qf_1922_tl, d_175, bpmi_1925_tl, d_17, 
mpbpmi_1925_tl, d_152, cfx_1925_tl, d_178, otrbw_1929_tl, d_184, bpmi_1930_tl, d_17, 
mpbpmi_1930_tl, d_186, bam_1931_tl, d_187, bam_1932_tl, d_188, crd_1934_tl, d_189, 
qf_1937_tl, d_5, cfy_1937_tl, d_191, bpmi_1939_tl, d_17, mpbpmi_1939_tl, d_193, 
bl_1939_tl, d_194, ensub_1940_tl, stsub_1940_tl, d_195, qf_1952_tl, d_196, bl_1964_tl, 
d_197, chx_1965_tl, d_198, bpma_1966_tl, d_199, qf_1967_tl, d_200, chx_1967_tl, 
d_201, chy_1967_tl, d_202, cnx_1977_tl, d_2, cny_1977_tl, d_204, bpmd_1977_tl, 
d_201, otre_1978_tl, d_206, ensub_1980_tl)
# power supplies 

#  
qf_1660_cl.ps_id = 'QF.3.CL'
qh_1667_cl.ps_id = 'QH.1.CL'
qh_1669_cl.ps_id = 'QH.1.CL'
qh_1670_cl.ps_id = 'QH.2.CL'
qh_1671_cl.ps_id = 'QH.2.CL'
qf_1673_cl.ps_id = 'QF.4.CL'
qf_1682_cl.ps_id = 'QF.4.CL'
qf_1691_cl.ps_id = 'QF.4.CL'
qf_1700_cl.ps_id = 'QF.4.CL'
qf_1709_cl.ps_id = 'QF.4.CL'
qf_1718_cl.ps_id = 'QF.4.CL'
qf_1727_cl.ps_id = 'QF.4.CL'
qf_1736_cl.ps_id = 'QF.4.CL'
qf_1745_cl.ps_id = 'QF.4.CL'
qh_1748_cl.ps_id = 'QH.3.CL'
qh_1749_cl.ps_id = 'QH.3.CL'
qh_1751_cl.ps_id = 'QH.4.CL'
qh_1752_cl.ps_id = 'QH.4.CL'
qf_1754_cl.ps_id = 'QF.5.CL'
qf_1759_cl.ps_id = 'QF.6.CL'
qf_1763_cl.ps_id = 'QF.7.CL'
qf_1767_cl.ps_id = 'QF.6.CL'
qf_1772_cl.ps_id = 'QF.5.CL'
qh_1775_cl.ps_id = 'QH.4.CL'
qh_1776_cl.ps_id = 'QH.4.CL'
qh_1778_cl.ps_id = 'QH.3.CL'
qh_1779_cl.ps_id = 'QH.3.CL'
qf_1781_cl.ps_id = 'QF.4.CL'
qf_1790_cl.ps_id = 'QF.4.CL'
qf_1799_cl.ps_id = 'QF.4.CL'
qf_1808_cl.ps_id = 'QF.4.CL'
qf_1817_cl.ps_id = 'QF.4.CL'
qf_1826_cl.ps_id = 'QF.4.CL'
qf_1835_cl.ps_id = 'QF.4.CL'
qf_1844_cl.ps_id = 'QF.4.CL'
qf_1853_cl.ps_id = 'QF.4.CL'
qh_1855_tl.ps_id = 'QH.5.TL'
qh_1857_tl.ps_id = 'QH.6.TL'
qh_1858_tl.ps_id = 'QH.7.TL'
qh_1859_tl.ps_id = 'QH.8.TL'
qf_1864_tl.ps_id = 'QF.8.TL'
qf_1868_tl.ps_id = 'QF.9.TL'
qf_1873_tl.ps_id = 'QF.10.TL'
qf_1881_tl.ps_id = 'QF.11.TL'
qf_1892_tl.ps_id = 'QF.1.TL'
qf_1907_tl.ps_id = 'QF.2.TL'
qf_1922_tl.ps_id = 'QF.1.TL'
qf_1937_tl.ps_id = 'QF.2.TL'
qf_1952_tl.ps_id = 'QF.1.TL'
qf_1967_tl.ps_id = 'QF.2.TL'

#  
sa_1674_cl.ps_id = 'SA.1.CL'
sa_1683_cl.ps_id = 'SA.2.CL'
sa_1691_cl.ps_id = 'SA.3.CL'
sa_1692_cl.ps_id = 'SA.3.CL'
sa_1700_cl.ps_id = 'SA.2.CL'
sa_1708_cl.ps_id = 'SA.1.CL'
sa_1710_cl.ps_id = 'SA.1.CL'
sa_1719_cl.ps_id = 'SA.2.CL'
sa_1726_cl.ps_id = 'SA.3.CL'
sa_1728_cl.ps_id = 'SA.3.CL'
sa_1736_cl.ps_id = 'SA.2.CL'
sa_1744_cl.ps_id = 'SA.1.CL'
sa_1782_cl.ps_id = 'SA.4.CL'
sa_1791_cl.ps_id = 'SA.5.CL'
sa_1798_cl.ps_id = 'SA.6.CL'
sa_1800_cl.ps_id = 'SA.6.CL'
sa_1808_cl.ps_id = 'SA.5.CL'
sa_1816_cl.ps_id = 'SA.4.CL'
sa_1818_cl.ps_id = 'SA.4.CL'
sa_1827_cl.ps_id = 'SA.5.CL'
sa_1834_cl.ps_id = 'SA.6.CL'
sa_1836_cl.ps_id = 'SA.6.CL'
sa_1844_cl.ps_id = 'SA.5.CL'
sa_1852_cl.ps_id = 'SA.4.CL'

#  

#  

#  
be_1678_cl.ps_id = 'BE.1.CL'
bl_1688_cl.ps_id = 'BL.1.CL'
bl_1695_cl.ps_id = 'BL.1.CL'
be_1705_cl.ps_id = 'BE.1.CL'
be_1714_cl.ps_id = 'BE.1.CL'
bl_1724_cl.ps_id = 'BL.1.CL'
bl_1731_cl.ps_id = 'BL.1.CL'
be_1741_cl.ps_id = 'BE.1.CL'
be_1786_cl.ps_id = 'BE.2.CL'
bl_1796_cl.ps_id = 'BL.2.CL'
bl_1803_cl.ps_id = 'BL.2.CL'
be_1813_cl.ps_id = 'BE.2.CL'
be_1822_cl.ps_id = 'BE.2.CL'
bl_1832_cl.ps_id = 'BL.2.CL'
bl_1839_cl.ps_id = 'BL.2.CL'
be_1849_cl.ps_id = 'BE.2.CL'
