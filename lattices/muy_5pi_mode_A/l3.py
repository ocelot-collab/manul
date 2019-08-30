from ocelot import * 
tws = Twiss()
tws.beta_x  = 29.3441199993
tws.beta_y  = 5.03315033363
tws.alpha_x = 2.62406788463
tws.alpha_y = -1.14732104041
tws.E = 2.4
# drifts 
d_1 = Drift(l=3.50665, eid='D_1')
d_2 = Drift(l=0.13165, eid='D_2')
d_3 = Drift(l=1.21638, eid='D_3')
d_4 = Drift(l=0.1543, eid='D_4')
d_5 = Drift(l=0.16597, eid='D_5')
d_6 = Drift(l=5.11825, eid='D_6')
d_7 = Drift(l=0.3459, eid='D_7')
d_14 = Drift(l=0.2475, eid='D_14')
d_15 = Drift(l=0.0432, eid='D_15')
d_16 = Drift(l=0.085, eid='D_16')
d_17 = Drift(l=0.6795, eid='D_17')
d_138 = Drift(l=3.6773, eid='D_138')
d_598 = Drift(l=0.1282, eid='D_598')
d_885 = Drift(l=5.2537, eid='D_885')
d_886 = Drift(l=16.2017, eid='D_886')
d_887 = Drift(l=0.23555, eid='D_887')
d_888 = Drift(l=0.33555, eid='D_888')
d_889 = Drift(l=22.7834, eid='D_889')
d_892 = Drift(l=23.008175, eid='D_892')
d_893 = Drift(l=18.037275, eid='D_893')
d_894 = Drift(l=0.205, eid='D_894')
d_895 = Drift(l=0.14, eid='D_895')
d_896 = Drift(l=36.03955, eid='D_896')
d_899 = Drift(l=18.002275, eid='D_899')
d_903 = Drift(l=12.90325, eid='D_903')
d_906 = Drift(l=5.81, eid='D_906')
d_907 = Drift(l=5.845, eid='D_907')
d_908 = Drift(l=0.20895, eid='D_908')
d_909 = Drift(l=0.15395, eid='D_909')
d_910 = Drift(l=8.355, eid='D_910')
d_913 = Drift(l=1.1663, eid='D_913')

# quadrupoles 
qd_470_b2 = Quadrupole(l=0.2367, k1=-1.128906739, tilt=0.0, eid='QD.470.B2')
qd_472_b2 = Quadrupole(l=0.2367, k1=0.6611797761, tilt=0.0, eid='QD.472.B2')
q_488_l3 = Quadrupole(l=0.2136, k1=-0.3339147164, tilt=0.0, eid='Q.488.L3')
q_500_l3 = Quadrupole(l=0.2136, k1=0.4269256757, tilt=0.0, eid='Q.500.L3')
q_512_l3 = Quadrupole(l=0.2136, k1=-0.2701007323, tilt=0.0, eid='Q.512.L3')
q_524_l3 = Quadrupole(l=0.2136, k1=-0.0803619504, tilt=0.0, eid='Q.524.L3')
q_536_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.536.L3')
q_548_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.548.L3')
q_560_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.560.L3')
q_572_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.572.L3')
q_584_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.584.L3')
q_596_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.596.L3')
q_608_l3 = Quadrupole(l=0.2136, k1=0.3171476124, tilt=0.0, eid='Q.608.L3')
q_620_l3 = Quadrupole(l=0.2136, k1=-0.2941311798, tilt=0.0, eid='Q.620.L3')
q_635_l3 = Quadrupole(l=0.2136, k1=0.2903606742, tilt=0.0, eid='Q.635.L3')
q_647_l3 = Quadrupole(l=0.2136, k1=-0.306425, tilt=0.0, eid='Q.647.L3')
q_659_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.659.L3')
q_671_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.671.L3')
q_683_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.683.L3')
q_695_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.695.L3')
q_707_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.707.L3')
q_719_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.719.L3')
q_731_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.731.L3')
q_743_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.743.L3')
q_755_l3 = Quadrupole(l=0.2136, k1=0.3171476124, tilt=0.0, eid='Q.755.L3')
q_767_l3 = Quadrupole(l=0.2136, k1=-0.2941311798, tilt=0.0, eid='Q.767.L3')
q_782_l3 = Quadrupole(l=0.2136, k1=0.2903606742, tilt=0.0, eid='Q.782.L3')
q_794_l3 = Quadrupole(l=0.2136, k1=-0.306425, tilt=0.0, eid='Q.794.L3')
q_806_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.806.L3')
q_818_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.818.L3')
q_830_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.830.L3')
q_842_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.842.L3')
q_854_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.854.L3')
q_866_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.866.L3')
q_878_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.878.L3')
q_890_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.890.L3')
q_902_l3 = Quadrupole(l=0.2136, k1=0.3171476124, tilt=0.0, eid='Q.902.L3')
q_914_l3 = Quadrupole(l=0.2136, k1=-0.2941311798, tilt=0.0, eid='Q.914.L3')
q_929_l3 = Quadrupole(l=0.2136, k1=0.2903606742, tilt=0.0, eid='Q.929.L3')
q_941_l3 = Quadrupole(l=0.2136, k1=-0.306425, tilt=0.0, eid='Q.941.L3')
q_953_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.953.L3')
q_965_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.965.L3')
q_977_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.977.L3')
q_989_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.989.L3')
q_1001_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1001.L3')
q_1013_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1013.L3')
q_1025_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1025.L3')
q_1037_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1037.L3')
q_1049_l3 = Quadrupole(l=0.2136, k1=0.3171476124, tilt=0.0, eid='Q.1049.L3')
q_1061_l3 = Quadrupole(l=0.2136, k1=-0.2941311798, tilt=0.0, eid='Q.1061.L3')
q_1076_l3 = Quadrupole(l=0.2136, k1=0.2903606742, tilt=0.0, eid='Q.1076.L3')
q_1088_l3 = Quadrupole(l=0.2136, k1=-0.306425, tilt=0.0, eid='Q.1088.L3')
q_1100_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1100.L3')
q_1112_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1112.L3')
q_1124_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1124.L3')
q_1136_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1136.L3')
q_1147_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1147.L3')
q_1159_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1159.L3')
q_1171_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1171.L3')
q_1183_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1183.L3')
q_1195_l3 = Quadrupole(l=0.2136, k1=0.3171476124, tilt=0.0, eid='Q.1195.L3')
q_1207_l3 = Quadrupole(l=0.2136, k1=-0.2941311798, tilt=0.0, eid='Q.1207.L3')
q_1222_l3 = Quadrupole(l=0.2136, k1=0.2903606742, tilt=0.0, eid='Q.1222.L3')
q_1234_l3 = Quadrupole(l=0.2136, k1=-0.306425, tilt=0.0, eid='Q.1234.L3')
q_1246_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1246.L3')
q_1258_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1258.L3')
q_1270_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1270.L3')
q_1282_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1282.L3')
q_1294_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1294.L3')
q_1306_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1306.L3')
q_1318_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1318.L3')
q_1330_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1330.L3')
q_1342_l3 = Quadrupole(l=0.2136, k1=0.3171476124, tilt=0.0, eid='Q.1342.L3')
q_1354_l3 = Quadrupole(l=0.2136, k1=-0.2941311798, tilt=0.0, eid='Q.1354.L3')
q_1369_l3 = Quadrupole(l=0.2136, k1=0.2903606742, tilt=0.0, eid='Q.1369.L3')
q_1381_l3 = Quadrupole(l=0.2136, k1=-0.306425, tilt=0.0, eid='Q.1381.L3')
q_1393_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1393.L3')
q_1405_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1405.L3')
q_1417_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1417.L3')
q_1429_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1429.L3')
q_1441_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1441.L3')
q_1453_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1453.L3')
qb_1475_l3 = Quadrupole(l=0.3289, k1=0.140392839, tilt=0.0, eid='QB.1475.L3')
qb_1499_l3 = Quadrupole(l=0.3289, k1=-0.1308389927, tilt=0.0, eid='QB.1499.L3')
qe_1542_l3 = Quadrupole(l=0.24, k1=0.1280915, tilt=0.0, eid='QE.1542.L3')
qe_1578_l3 = Quadrupole(l=0.24, k1=-0.1280915, tilt=0.0, eid='QE.1578.L3')
qe_1615_l3 = Quadrupole(l=0.24, k1=0.1280915, tilt=0.0, eid='QE.1615.L3')
qe_1629_l3 = Quadrupole(l=0.24, k1=-0.1214323728, tilt=0.0, eid='QE.1629.L3')
qf_1641_l3 = Quadrupole(l=0.5321, k1=0.0737276389, tilt=0.0, eid='QF.1641.L3')
qf_1650_l3 = Quadrupole(l=0.5321, k1=-0.1121786011, tilt=0.0, eid='QF.1650.L3')

# bending magnets 

# correctors 
ccy_470_b2 = Vcor(l=0.1, angle=0.0, eid='CCY.470.B2')
cx_488_l3 = Hcor(l=0.0, angle=0.0, eid='CX.488.L3')
cy_500_l3 = Vcor(l=0.0, angle=0.0, eid='CY.500.L3')
cx_512_l3 = Hcor(l=0.0, angle=0.0, eid='CX.512.L3')
cy_524_l3 = Vcor(l=0.0, angle=0.0, eid='CY.524.L3')
cx_536_l3 = Hcor(l=0.0, angle=0.0, eid='CX.536.L3')
cy_548_l3 = Vcor(l=0.0, angle=0.0, eid='CY.548.L3')
cx_560_l3 = Hcor(l=0.0, angle=0.0, eid='CX.560.L3')
cy_572_l3 = Vcor(l=0.0, angle=0.0, eid='CY.572.L3')
cx_584_l3 = Hcor(l=0.0, angle=0.0, eid='CX.584.L3')
cy_596_l3 = Vcor(l=0.0, angle=0.0, eid='CY.596.L3')
cx_608_l3 = Hcor(l=0.0, angle=0.0, eid='CX.608.L3')
cy_620_l3 = Vcor(l=0.0, angle=0.0, eid='CY.620.L3')
cx_635_l3 = Hcor(l=0.0, angle=0.0, eid='CX.635.L3')
cy_647_l3 = Vcor(l=0.0, angle=0.0, eid='CY.647.L3')
cx_659_l3 = Hcor(l=0.0, angle=0.0, eid='CX.659.L3')
cy_671_l3 = Vcor(l=0.0, angle=0.0, eid='CY.671.L3')
cx_683_l3 = Hcor(l=0.0, angle=0.0, eid='CX.683.L3')
cy_695_l3 = Vcor(l=0.0, angle=0.0, eid='CY.695.L3')
cx_707_l3 = Hcor(l=0.0, angle=0.0, eid='CX.707.L3')
cy_719_l3 = Vcor(l=0.0, angle=0.0, eid='CY.719.L3')
cx_731_l3 = Hcor(l=0.0, angle=0.0, eid='CX.731.L3')
cy_743_l3 = Vcor(l=0.0, angle=0.0, eid='CY.743.L3')
cx_755_l3 = Hcor(l=0.0, angle=0.0, eid='CX.755.L3')
cy_767_l3 = Vcor(l=0.0, angle=0.0, eid='CY.767.L3')
cx_782_l3 = Hcor(l=0.0, angle=0.0, eid='CX.782.L3')
cy_794_l3 = Vcor(l=0.0, angle=0.0, eid='CY.794.L3')
cx_806_l3 = Hcor(l=0.0, angle=0.0, eid='CX.806.L3')
cy_818_l3 = Vcor(l=0.0, angle=0.0, eid='CY.818.L3')
cx_830_l3 = Hcor(l=0.0, angle=0.0, eid='CX.830.L3')
cy_842_l3 = Vcor(l=0.0, angle=0.0, eid='CY.842.L3')
cx_854_l3 = Hcor(l=0.0, angle=0.0, eid='CX.854.L3')
cy_866_l3 = Vcor(l=0.0, angle=0.0, eid='CY.866.L3')
cx_878_l3 = Hcor(l=0.0, angle=0.0, eid='CX.878.L3')
cy_890_l3 = Vcor(l=0.0, angle=0.0, eid='CY.890.L3')
cx_902_l3 = Hcor(l=0.0, angle=0.0, eid='CX.902.L3')
cy_914_l3 = Vcor(l=0.0, angle=0.0, eid='CY.914.L3')
cx_929_l3 = Hcor(l=0.0, angle=0.0, eid='CX.929.L3')
cy_941_l3 = Vcor(l=0.0, angle=0.0, eid='CY.941.L3')
cx_953_l3 = Hcor(l=0.0, angle=0.0, eid='CX.953.L3')
cy_965_l3 = Vcor(l=0.0, angle=0.0, eid='CY.965.L3')
cx_977_l3 = Hcor(l=0.0, angle=0.0, eid='CX.977.L3')
cy_989_l3 = Vcor(l=0.0, angle=0.0, eid='CY.989.L3')
cx_1001_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1001.L3')
cy_1013_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1013.L3')
cx_1025_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1025.L3')
cy_1037_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1037.L3')
cx_1049_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1049.L3')
cy_1061_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1061.L3')
cx_1076_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1076.L3')
cy_1088_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1088.L3')
cx_1100_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1100.L3')
cy_1112_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1112.L3')
cx_1124_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1124.L3')
cx_1148_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1148.L3')
cy_1148_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1148.L3')
cy_1160_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1160.L3')
cx_1172_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1172.L3')
cy_1184_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1184.L3')
cx_1196_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1196.L3')
cy_1208_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1208.L3')
cx_1223_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1223.L3')
cy_1235_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1235.L3')
cx_1247_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1247.L3')
cy_1259_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1259.L3')
cx_1271_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1271.L3')
cy_1283_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1283.L3')
cx_1295_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1295.L3')
cy_1307_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1307.L3')
cx_1319_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1319.L3')
cy_1331_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1331.L3')
cx_1343_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1343.L3')
cy_1355_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1355.L3')
cx_1369_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1369.L3')
cy_1381_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1381.L3')
cx_1393_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1393.L3')
cy_1405_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1405.L3')
cx_1417_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1417.L3')
cy_1429_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1429.L3')
cx_1441_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1441.L3')
cy_1453_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1453.L3')
cmx_1476_l3 = Hcor(l=0.3, angle=0.0, eid='CMX.1476.L3')
cmy_1500_l3 = Vcor(l=0.3, angle=0.0, eid='CMY.1500.L3')
cex_1542_l3 = Hcor(l=0.1, angle=0.0, eid='CEX.1542.L3')
cey_1579_l3 = Vcor(l=0.1, angle=0.0, eid='CEY.1579.L3')
cex_1615_l3 = Hcor(l=0.1, angle=0.0, eid='CEX.1615.L3')
cey_1629_l3 = Vcor(l=0.1, angle=0.0, eid='CEY.1629.L3')
cfx_1642_l3 = Hcor(l=0.1, angle=0.0, eid='CFX.1642.L3')
cfy_1651_l3 = Vcor(l=0.1, angle=0.0, eid='CFY.1651.L3')

# markers 
stsub_466_b2 = Marker(eid='STSUB.466.B2')
tora_471_b2 = Marker(eid='TORA.471.B2')
tora_1459_l3 = Marker(eid='TORA.1459.L3')
otrbw_1523_l3 = Marker(eid='OTRBW.1523.L3')
otrbw_1597_l3 = Marker(eid='OTRBW.1597.L3')
otrbw_1635_l3 = Marker(eid='OTRBW.1635.L3')
stsec_1652_cl = Marker(eid='STSEC.1652.CL')

# monitor 
bpma_471_b2 = Monitor(eid='BPMA.471.B2')
bpmc_488_l3 = Monitor(eid='BPMC.488.L3')
bpmc_500_l3 = Monitor(eid='BPMC.500.L3')
bpmc_512_l3 = Monitor(eid='BPMC.512.L3')
bpmc_524_l3 = Monitor(eid='BPMC.524.L3')
bpmc_536_l3 = Monitor(eid='BPMC.536.L3')
bpmc_548_l3 = Monitor(eid='BPMC.548.L3')
bpmc_560_l3 = Monitor(eid='BPMC.560.L3')
bpmr_572_l3 = Monitor(eid='BPMR.572.L3')
bpmc_584_l3 = Monitor(eid='BPMC.584.L3')
bpmc_596_l3 = Monitor(eid='BPMC.596.L3')
bpmr_608_l3 = Monitor(eid='BPMR.608.L3')
bpmc_620_l3 = Monitor(eid='BPMC.620.L3')
bpmc_635_l3 = Monitor(eid='BPMC.635.L3')
bpmc_647_l3 = Monitor(eid='BPMC.647.L3')
bpmc_659_l3 = Monitor(eid='BPMC.659.L3')
bpmc_671_l3 = Monitor(eid='BPMC.671.L3')
bpmc_683_l3 = Monitor(eid='BPMC.683.L3')
bpmr_695_l3 = Monitor(eid='BPMR.695.L3')
bpmr_707_l3 = Monitor(eid='BPMR.707.L3')
bpmc_719_l3 = Monitor(eid='BPMC.719.L3')
bpmc_731_l3 = Monitor(eid='BPMC.731.L3')
bpmc_743_l3 = Monitor(eid='BPMC.743.L3')
bpmr_755_l3 = Monitor(eid='BPMR.755.L3')
bpmc_767_l3 = Monitor(eid='BPMC.767.L3')
bpmc_782_l3 = Monitor(eid='BPMC.782.L3')
bpmc_794_l3 = Monitor(eid='BPMC.794.L3')
bpmr_806_l3 = Monitor(eid='BPMR.806.L3')
bpmr_818_l3 = Monitor(eid='BPMR.818.L3')
bpmc_830_l3 = Monitor(eid='BPMC.830.L3')
bpmc_842_l3 = Monitor(eid='BPMC.842.L3')
bpmc_854_l3 = Monitor(eid='BPMC.854.L3')
bpmc_866_l3 = Monitor(eid='BPMC.866.L3')
bpmc_878_l3 = Monitor(eid='BPMC.878.L3')
bpmc_890_l3 = Monitor(eid='BPMC.890.L3')
bpmc_902_l3 = Monitor(eid='BPMC.902.L3')
bpmc_914_l3 = Monitor(eid='BPMC.914.L3')
bpmc_929_l3 = Monitor(eid='BPMC.929.L3')
bpmc_941_l3 = Monitor(eid='BPMC.941.L3')
bpmc_953_l3 = Monitor(eid='BPMC.953.L3')
bpmc_965_l3 = Monitor(eid='BPMC.965.L3')
bpmc_977_l3 = Monitor(eid='BPMC.977.L3')
bpmc_989_l3 = Monitor(eid='BPMC.989.L3')
bpmc_1001_l3 = Monitor(eid='BPMC.1001.L3')
bpmc_1013_l3 = Monitor(eid='BPMC.1013.L3')
bpmc_1025_l3 = Monitor(eid='BPMC.1025.L3')
bpmc_1037_l3 = Monitor(eid='BPMC.1037.L3')
bpmc_1049_l3 = Monitor(eid='BPMC.1049.L3')
bpmc_1061_l3 = Monitor(eid='BPMC.1061.L3')
bpmc_1076_l3 = Monitor(eid='BPMC.1076.L3')
bpmr_1088_l3 = Monitor(eid='BPMR.1088.L3')
bpmc_1100_l3 = Monitor(eid='BPMC.1100.L3')
bpmr_1112_l3 = Monitor(eid='BPMR.1112.L3')
bpmc_1124_l3 = Monitor(eid='BPMC.1124.L3')
bpmc_1136_l3 = Monitor(eid='BPMC.1136.L3')
bpmc_1148_l3 = Monitor(eid='BPMC.1148.L3')
bpmc_1160_l3 = Monitor(eid='BPMC.1160.L3')
bpmr_1172_l3 = Monitor(eid='BPMR.1172.L3')
bpmr_1184_l3 = Monitor(eid='BPMR.1184.L3')
bpmc_1196_l3 = Monitor(eid='BPMC.1196.L3')
bpmc_1208_l3 = Monitor(eid='BPMC.1208.L3')
bpmr_1223_l3 = Monitor(eid='BPMR.1223.L3')
bpmc_1235_l3 = Monitor(eid='BPMC.1235.L3')
bpmc_1247_l3 = Monitor(eid='BPMC.1247.L3')
bpmc_1259_l3 = Monitor(eid='BPMC.1259.L3')
bpmc_1271_l3 = Monitor(eid='BPMC.1271.L3')
bpmc_1283_l3 = Monitor(eid='BPMC.1283.L3')
bpmc_1295_l3 = Monitor(eid='BPMC.1295.L3')
bpmr_1307_l3 = Monitor(eid='BPMR.1307.L3')
bpmc_1319_l3 = Monitor(eid='BPMC.1319.L3')
bpmc_1331_l3 = Monitor(eid='BPMC.1331.L3')
bpmc_1343_l3 = Monitor(eid='BPMC.1343.L3')
bpmc_1355_l3 = Monitor(eid='BPMC.1355.L3')
bpmc_1370_l3 = Monitor(eid='BPMC.1370.L3')
bpmc_1382_l3 = Monitor(eid='BPMC.1382.L3')
bpmc_1394_l3 = Monitor(eid='BPMC.1394.L3')
bpmr_1406_l3 = Monitor(eid='BPMR.1406.L3')
bpmc_1418_l3 = Monitor(eid='BPMC.1418.L3')
bpmr_1430_l3 = Monitor(eid='BPMR.1430.L3')
bpmc_1442_l3 = Monitor(eid='BPMC.1442.L3')
bpmc_1454_l3 = Monitor(eid='BPMC.1454.L3')
bpma_1475_l3 = Monitor(eid='BPMA.1475.L3')
bpma_1499_l3 = Monitor(eid='BPMA.1499.L3')
bpma_1541_l3 = Monitor(eid='BPMA.1541.L3')
bpma_1578_l3 = Monitor(eid='BPMA.1578.L3')
bpma_1615_l3 = Monitor(eid='BPMA.1615.L3')
bpma_1628_l3 = Monitor(eid='BPMA.1628.L3')
bpma_1641_l3 = Monitor(eid='BPMA.1641.L3')
bpma_1650_l3 = Monitor(eid='BPMA.1650.L3')

# sextupoles 

# octupole 

# undulator 

# cavity 
c_a6_1_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.1.1.L3')
c_a6_1_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.1.2.L3')
c_a6_1_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.1.3.L3')
c_a6_1_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.1.4.L3')
c_a6_1_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.1.5.L3')
c_a6_1_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.1.6.L3')
c_a6_1_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.1.7.L3')
c_a6_1_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.1.8.L3')
c_a6_2_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.2.1.L3')
c_a6_2_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.2.2.L3')
c_a6_2_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.2.3.L3')
c_a6_2_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.2.4.L3')
c_a6_2_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.2.5.L3')
c_a6_2_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.2.6.L3')
c_a6_2_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.2.7.L3')
c_a6_2_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.2.8.L3')
c_a6_3_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.3.1.L3')
c_a6_3_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.3.2.L3')
c_a6_3_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.3.3.L3')
c_a6_3_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.3.4.L3')
c_a6_3_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.3.5.L3')
c_a6_3_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.3.6.L3')
c_a6_3_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.3.7.L3')
c_a6_3_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.3.8.L3')
c_a6_4_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.4.1.L3')
c_a6_4_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.4.2.L3')
c_a6_4_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.4.3.L3')
c_a6_4_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.4.4.L3')
c_a6_4_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.4.5.L3')
c_a6_4_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.4.6.L3')
c_a6_4_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.4.7.L3')
c_a6_4_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A6.4.8.L3')
c_a7_1_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.1.1.L3')
c_a7_1_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.1.2.L3')
c_a7_1_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.1.3.L3')
c_a7_1_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.1.4.L3')
c_a7_1_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.1.5.L3')
c_a7_1_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.1.6.L3')
c_a7_1_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.1.7.L3')
c_a7_1_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.1.8.L3')
c_a7_2_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.2.1.L3')
c_a7_2_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.2.2.L3')
c_a7_2_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.2.3.L3')
c_a7_2_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.2.4.L3')
c_a7_2_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.2.5.L3')
c_a7_2_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.2.6.L3')
c_a7_2_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.2.7.L3')
c_a7_2_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.2.8.L3')
c_a7_3_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.3.1.L3')
c_a7_3_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.3.2.L3')
c_a7_3_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.3.3.L3')
c_a7_3_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.3.4.L3')
c_a7_3_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.3.5.L3')
c_a7_3_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.3.6.L3')
c_a7_3_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.3.7.L3')
c_a7_3_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.3.8.L3')
c_a7_4_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.4.1.L3')
c_a7_4_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.4.2.L3')
c_a7_4_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.4.3.L3')
c_a7_4_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.4.4.L3')
c_a7_4_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.4.5.L3')
c_a7_4_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.4.6.L3')
c_a7_4_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.4.7.L3')
c_a7_4_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A7.4.8.L3')
c_a8_1_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.1.1.L3')
c_a8_1_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.1.2.L3')
c_a8_1_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.1.3.L3')
c_a8_1_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.1.4.L3')
c_a8_1_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.1.5.L3')
c_a8_1_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.1.6.L3')
c_a8_1_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.1.7.L3')
c_a8_1_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.1.8.L3')
c_a8_2_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.2.1.L3')
c_a8_2_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.2.2.L3')
c_a8_2_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.2.3.L3')
c_a8_2_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.2.4.L3')
c_a8_2_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.2.5.L3')
c_a8_2_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.2.6.L3')
c_a8_2_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.2.7.L3')
c_a8_2_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.2.8.L3')
c_a8_3_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.3.1.L3')
c_a8_3_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.3.2.L3')
c_a8_3_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.3.3.L3')
c_a8_3_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.3.4.L3')
c_a8_3_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.3.5.L3')
c_a8_3_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.3.6.L3')
c_a8_3_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.3.7.L3')
c_a8_3_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.3.8.L3')
c_a8_4_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.4.1.L3')
c_a8_4_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.4.2.L3')
c_a8_4_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.4.3.L3')
c_a8_4_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.4.4.L3')
c_a8_4_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.4.5.L3')
c_a8_4_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.4.6.L3')
c_a8_4_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.4.7.L3')
c_a8_4_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A8.4.8.L3')
c_a9_1_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.1.1.L3')
c_a9_1_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.1.2.L3')
c_a9_1_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.1.3.L3')
c_a9_1_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.1.4.L3')
c_a9_1_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.1.5.L3')
c_a9_1_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.1.6.L3')
c_a9_1_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.1.7.L3')
c_a9_1_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.1.8.L3')
c_a9_2_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.2.1.L3')
c_a9_2_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.2.2.L3')
c_a9_2_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.2.3.L3')
c_a9_2_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.2.4.L3')
c_a9_2_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.2.5.L3')
c_a9_2_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.2.6.L3')
c_a9_2_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.2.7.L3')
c_a9_2_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.2.8.L3')
c_a9_3_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.3.1.L3')
c_a9_3_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.3.2.L3')
c_a9_3_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.3.3.L3')
c_a9_3_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.3.4.L3')
c_a9_3_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.3.5.L3')
c_a9_3_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.3.6.L3')
c_a9_3_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.3.7.L3')
c_a9_3_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.3.8.L3')
c_a9_4_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.4.1.L3')
c_a9_4_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.4.2.L3')
c_a9_4_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.4.3.L3')
c_a9_4_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.4.4.L3')
c_a9_4_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.4.5.L3')
c_a9_4_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.4.6.L3')
c_a9_4_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.4.7.L3')
c_a9_4_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A9.4.8.L3')
c_a10_1_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.1.1.L3')
c_a10_1_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.1.2.L3')
c_a10_1_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.1.3.L3')
c_a10_1_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.1.4.L3')
c_a10_1_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.1.5.L3')
c_a10_1_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.1.6.L3')
c_a10_1_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.1.7.L3')
c_a10_1_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.1.8.L3')
c_a10_2_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.2.1.L3')
c_a10_2_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.2.2.L3')
c_a10_2_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.2.3.L3')
c_a10_2_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.2.4.L3')
c_a10_2_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.2.5.L3')
c_a10_2_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.2.6.L3')
c_a10_2_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.2.7.L3')
c_a10_2_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.2.8.L3')
c_a10_3_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.3.1.L3')
c_a10_3_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.3.2.L3')
c_a10_3_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.3.3.L3')
c_a10_3_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.3.4.L3')
c_a10_3_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.3.5.L3')
c_a10_3_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.3.6.L3')
c_a10_3_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.3.7.L3')
c_a10_3_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.3.8.L3')
c_a10_4_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.4.1.L3')
c_a10_4_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.4.2.L3')
c_a10_4_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.4.3.L3')
c_a10_4_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.4.4.L3')
c_a10_4_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.4.5.L3')
c_a10_4_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.4.6.L3')
c_a10_4_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.4.7.L3')
c_a10_4_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A10.4.8.L3')
c_a11_1_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.1.1.L3')
c_a11_1_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.1.2.L3')
c_a11_1_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.1.3.L3')
c_a11_1_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.1.4.L3')
c_a11_1_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.1.5.L3')
c_a11_1_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.1.6.L3')
c_a11_1_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.1.7.L3')
c_a11_1_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.1.8.L3')
c_a11_2_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.2.1.L3')
c_a11_2_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.2.2.L3')
c_a11_2_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.2.3.L3')
c_a11_2_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.2.4.L3')
c_a11_2_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.2.5.L3')
c_a11_2_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.2.6.L3')
c_a11_2_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.2.7.L3')
c_a11_2_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.2.8.L3')
c_a11_3_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.3.1.L3')
c_a11_3_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.3.2.L3')
c_a11_3_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.3.3.L3')
c_a11_3_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.3.4.L3')
c_a11_3_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.3.5.L3')
c_a11_3_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.3.6.L3')
c_a11_3_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.3.7.L3')
c_a11_3_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.3.8.L3')
c_a11_4_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.4.1.L3')
c_a11_4_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.4.2.L3')
c_a11_4_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.4.3.L3')
c_a11_4_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.4.4.L3')
c_a11_4_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.4.5.L3')
c_a11_4_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.4.6.L3')
c_a11_4_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.4.7.L3')
c_a11_4_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A11.4.8.L3')
c_a12_1_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.1.1.L3')
c_a12_1_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.1.2.L3')
c_a12_1_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.1.3.L3')
c_a12_1_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.1.4.L3')
c_a12_1_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.1.5.L3')
c_a12_1_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.1.6.L3')
c_a12_1_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.1.7.L3')
c_a12_1_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.1.8.L3')
c_a12_2_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.2.1.L3')
c_a12_2_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.2.2.L3')
c_a12_2_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.2.3.L3')
c_a12_2_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.2.4.L3')
c_a12_2_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.2.5.L3')
c_a12_2_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.2.6.L3')
c_a12_2_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.2.7.L3')
c_a12_2_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.2.8.L3')
c_a12_3_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.3.1.L3')
c_a12_3_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.3.2.L3')
c_a12_3_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.3.3.L3')
c_a12_3_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.3.4.L3')
c_a12_3_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.3.5.L3')
c_a12_3_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.3.6.L3')
c_a12_3_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.3.7.L3')
c_a12_3_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.3.8.L3')
c_a12_4_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.4.1.L3')
c_a12_4_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.4.2.L3')
c_a12_4_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.4.3.L3')
c_a12_4_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.4.4.L3')
c_a12_4_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.4.5.L3')
c_a12_4_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.4.6.L3')
c_a12_4_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.4.7.L3')
c_a12_4_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A12.4.8.L3')
c_a13_1_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.1.1.L3')
c_a13_1_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.1.2.L3')
c_a13_1_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.1.3.L3')
c_a13_1_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.1.4.L3')
c_a13_1_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.1.5.L3')
c_a13_1_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.1.6.L3')
c_a13_1_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.1.7.L3')
c_a13_1_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.1.8.L3')
c_a13_2_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.2.1.L3')
c_a13_2_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.2.2.L3')
c_a13_2_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.2.3.L3')
c_a13_2_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.2.4.L3')
c_a13_2_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.2.5.L3')
c_a13_2_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.2.6.L3')
c_a13_2_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.2.7.L3')
c_a13_2_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.2.8.L3')
c_a13_3_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.3.1.L3')
c_a13_3_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.3.2.L3')
c_a13_3_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.3.3.L3')
c_a13_3_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.3.4.L3')
c_a13_3_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.3.5.L3')
c_a13_3_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.3.6.L3')
c_a13_3_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.3.7.L3')
c_a13_3_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.3.8.L3')
c_a13_4_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.4.1.L3')
c_a13_4_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.4.2.L3')
c_a13_4_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.4.3.L3')
c_a13_4_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.4.4.L3')
c_a13_4_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.4.5.L3')
c_a13_4_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.4.6.L3')
c_a13_4_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.4.7.L3')
c_a13_4_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A13.4.8.L3')
c_a14_1_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.1.1.L3')
c_a14_1_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.1.2.L3')
c_a14_1_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.1.3.L3')
c_a14_1_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.1.4.L3')
c_a14_1_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.1.5.L3')
c_a14_1_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.1.6.L3')
c_a14_1_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.1.7.L3')
c_a14_1_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.1.8.L3')
c_a14_2_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.2.1.L3')
c_a14_2_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.2.2.L3')
c_a14_2_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.2.3.L3')
c_a14_2_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.2.4.L3')
c_a14_2_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.2.5.L3')
c_a14_2_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.2.6.L3')
c_a14_2_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.2.7.L3')
c_a14_2_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.2.8.L3')
c_a14_3_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.3.1.L3')
c_a14_3_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.3.2.L3')
c_a14_3_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.3.3.L3')
c_a14_3_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.3.4.L3')
c_a14_3_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.3.5.L3')
c_a14_3_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.3.6.L3')
c_a14_3_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.3.7.L3')
c_a14_3_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.3.8.L3')
c_a14_4_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.4.1.L3')
c_a14_4_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.4.2.L3')
c_a14_4_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.4.3.L3')
c_a14_4_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.4.4.L3')
c_a14_4_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.4.5.L3')
c_a14_4_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.4.6.L3')
c_a14_4_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.4.7.L3')
c_a14_4_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A14.4.8.L3')
c_a15_1_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.1.1.L3')
c_a15_1_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.1.2.L3')
c_a15_1_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.1.3.L3')
c_a15_1_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.1.4.L3')
c_a15_1_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.1.5.L3')
c_a15_1_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.1.6.L3')
c_a15_1_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.1.7.L3')
c_a15_1_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.1.8.L3')
c_a15_2_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.2.1.L3')
c_a15_2_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.2.2.L3')
c_a15_2_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.2.3.L3')
c_a15_2_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.2.4.L3')
c_a15_2_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.2.5.L3')
c_a15_2_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.2.6.L3')
c_a15_2_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.2.7.L3')
c_a15_2_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.2.8.L3')
c_a15_3_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.3.1.L3')
c_a15_3_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.3.2.L3')
c_a15_3_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.3.3.L3')
c_a15_3_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.3.4.L3')
c_a15_3_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.3.5.L3')
c_a15_3_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.3.6.L3')
c_a15_3_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.3.7.L3')
c_a15_3_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.3.8.L3')
c_a15_4_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.4.1.L3')
c_a15_4_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.4.2.L3')
c_a15_4_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.4.3.L3')
c_a15_4_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.4.4.L3')
c_a15_4_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.4.5.L3')
c_a15_4_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.4.6.L3')
c_a15_4_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.4.7.L3')
c_a15_4_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A15.4.8.L3')
c_a16_1_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.1.1.L3')
c_a16_1_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.1.2.L3')
c_a16_1_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.1.3.L3')
c_a16_1_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.1.4.L3')
c_a16_1_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.1.5.L3')
c_a16_1_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.1.6.L3')
c_a16_1_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.1.7.L3')
c_a16_1_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.1.8.L3')
c_a16_2_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.2.1.L3')
c_a16_2_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.2.2.L3')
c_a16_2_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.2.3.L3')
c_a16_2_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.2.4.L3')
c_a16_2_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.2.5.L3')
c_a16_2_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.2.6.L3')
c_a16_2_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.2.7.L3')
c_a16_2_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.2.8.L3')
c_a16_3_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.3.1.L3')
c_a16_3_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.3.2.L3')
c_a16_3_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.3.3.L3')
c_a16_3_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.3.4.L3')
c_a16_3_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.3.5.L3')
c_a16_3_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.3.6.L3')
c_a16_3_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.3.7.L3')
c_a16_3_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.3.8.L3')
c_a16_4_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.4.1.L3')
c_a16_4_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.4.2.L3')
c_a16_4_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.4.3.L3')
c_a16_4_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.4.4.L3')
c_a16_4_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.4.5.L3')
c_a16_4_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.4.6.L3')
c_a16_4_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.4.7.L3')
c_a16_4_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A16.4.8.L3')
c_a17_1_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.1.1.L3')
c_a17_1_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.1.2.L3')
c_a17_1_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.1.3.L3')
c_a17_1_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.1.4.L3')
c_a17_1_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.1.5.L3')
c_a17_1_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.1.6.L3')
c_a17_1_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.1.7.L3')
c_a17_1_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.1.8.L3')
c_a17_2_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.2.1.L3')
c_a17_2_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.2.2.L3')
c_a17_2_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.2.3.L3')
c_a17_2_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.2.4.L3')
c_a17_2_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.2.5.L3')
c_a17_2_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.2.6.L3')
c_a17_2_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.2.7.L3')
c_a17_2_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.2.8.L3')
c_a17_3_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.3.1.L3')
c_a17_3_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.3.2.L3')
c_a17_3_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.3.3.L3')
c_a17_3_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.3.4.L3')
c_a17_3_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.3.5.L3')
c_a17_3_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.3.6.L3')
c_a17_3_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.3.7.L3')
c_a17_3_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.3.8.L3')
c_a17_4_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.4.1.L3')
c_a17_4_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.4.2.L3')
c_a17_4_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.4.3.L3')
c_a17_4_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.4.4.L3')
c_a17_4_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.4.5.L3')
c_a17_4_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.4.6.L3')
c_a17_4_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.4.7.L3')
c_a17_4_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A17.4.8.L3')
c_a18_1_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.1.1.L3')
c_a18_1_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.1.2.L3')
c_a18_1_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.1.3.L3')
c_a18_1_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.1.4.L3')
c_a18_1_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.1.5.L3')
c_a18_1_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.1.6.L3')
c_a18_1_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.1.7.L3')
c_a18_1_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.1.8.L3')
c_a18_2_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.2.1.L3')
c_a18_2_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.2.2.L3')
c_a18_2_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.2.3.L3')
c_a18_2_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.2.4.L3')
c_a18_2_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.2.5.L3')
c_a18_2_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.2.6.L3')
c_a18_2_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.2.7.L3')
c_a18_2_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.2.8.L3')
c_a18_3_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.3.1.L3')
c_a18_3_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.3.2.L3')
c_a18_3_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.3.3.L3')
c_a18_3_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.3.4.L3')
c_a18_3_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.3.5.L3')
c_a18_3_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.3.6.L3')
c_a18_3_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.3.7.L3')
c_a18_3_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.3.8.L3')
c_a18_4_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.4.1.L3')
c_a18_4_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.4.2.L3')
c_a18_4_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.4.3.L3')
c_a18_4_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.4.4.L3')
c_a18_4_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.4.5.L3')
c_a18_4_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.4.6.L3')
c_a18_4_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.4.7.L3')
c_a18_4_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A18.4.8.L3')
c_a19_1_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.1.1.L3')
c_a19_1_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.1.2.L3')
c_a19_1_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.1.3.L3')
c_a19_1_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.1.4.L3')
c_a19_1_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.1.5.L3')
c_a19_1_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.1.6.L3')
c_a19_1_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.1.7.L3')
c_a19_1_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.1.8.L3')
c_a19_2_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.2.1.L3')
c_a19_2_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.2.2.L3')
c_a19_2_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.2.3.L3')
c_a19_2_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.2.4.L3')
c_a19_2_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.2.5.L3')
c_a19_2_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.2.6.L3')
c_a19_2_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.2.7.L3')
c_a19_2_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.2.8.L3')
c_a19_3_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.3.1.L3')
c_a19_3_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.3.2.L3')
c_a19_3_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.3.3.L3')
c_a19_3_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.3.4.L3')
c_a19_3_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.3.5.L3')
c_a19_3_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.3.6.L3')
c_a19_3_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.3.7.L3')
c_a19_3_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.3.8.L3')
c_a19_4_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.4.1.L3')
c_a19_4_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.4.2.L3')
c_a19_4_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.4.3.L3')
c_a19_4_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.4.4.L3')
c_a19_4_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.4.5.L3')
c_a19_4_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.4.6.L3')
c_a19_4_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.4.7.L3')
c_a19_4_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A19.4.8.L3')
c_a20_1_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.1.1.L3')
c_a20_1_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.1.2.L3')
c_a20_1_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.1.3.L3')
c_a20_1_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.1.4.L3')
c_a20_1_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.1.5.L3')
c_a20_1_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.1.6.L3')
c_a20_1_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.1.7.L3')
c_a20_1_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.1.8.L3')
c_a20_2_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.2.1.L3')
c_a20_2_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.2.2.L3')
c_a20_2_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.2.3.L3')
c_a20_2_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.2.4.L3')
c_a20_2_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.2.5.L3')
c_a20_2_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.2.6.L3')
c_a20_2_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.2.7.L3')
c_a20_2_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.2.8.L3')
c_a20_3_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.3.1.L3')
c_a20_3_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.3.2.L3')
c_a20_3_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.3.3.L3')
c_a20_3_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.3.4.L3')
c_a20_3_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.3.5.L3')
c_a20_3_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.3.6.L3')
c_a20_3_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.3.7.L3')
c_a20_3_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.3.8.L3')
c_a20_4_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.4.1.L3')
c_a20_4_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.4.2.L3')
c_a20_4_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.4.3.L3')
c_a20_4_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.4.4.L3')
c_a20_4_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.4.5.L3')
c_a20_4_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.4.6.L3')
c_a20_4_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.4.7.L3')
c_a20_4_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A20.4.8.L3')
c_a21_1_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.1.1.L3')
c_a21_1_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.1.2.L3')
c_a21_1_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.1.3.L3')
c_a21_1_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.1.4.L3')
c_a21_1_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.1.5.L3')
c_a21_1_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.1.6.L3')
c_a21_1_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.1.7.L3')
c_a21_1_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.1.8.L3')
c_a21_2_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.2.1.L3')
c_a21_2_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.2.2.L3')
c_a21_2_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.2.3.L3')
c_a21_2_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.2.4.L3')
c_a21_2_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.2.5.L3')
c_a21_2_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.2.6.L3')
c_a21_2_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.2.7.L3')
c_a21_2_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.2.8.L3')
c_a21_3_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.3.1.L3')
c_a21_3_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.3.2.L3')
c_a21_3_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.3.3.L3')
c_a21_3_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.3.4.L3')
c_a21_3_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.3.5.L3')
c_a21_3_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.3.6.L3')
c_a21_3_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.3.7.L3')
c_a21_3_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.3.8.L3')
c_a21_4_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.4.1.L3')
c_a21_4_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.4.2.L3')
c_a21_4_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.4.3.L3')
c_a21_4_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.4.4.L3')
c_a21_4_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.4.5.L3')
c_a21_4_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.4.6.L3')
c_a21_4_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.4.7.L3')
c_a21_4_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A21.4.8.L3')
c_a22_1_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.1.1.L3')
c_a22_1_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.1.2.L3')
c_a22_1_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.1.3.L3')
c_a22_1_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.1.4.L3')
c_a22_1_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.1.5.L3')
c_a22_1_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.1.6.L3')
c_a22_1_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.1.7.L3')
c_a22_1_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.1.8.L3')
c_a22_2_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.2.1.L3')
c_a22_2_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.2.2.L3')
c_a22_2_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.2.3.L3')
c_a22_2_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.2.4.L3')
c_a22_2_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.2.5.L3')
c_a22_2_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.2.6.L3')
c_a22_2_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.2.7.L3')
c_a22_2_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.2.8.L3')
c_a22_3_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.3.1.L3')
c_a22_3_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.3.2.L3')
c_a22_3_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.3.3.L3')
c_a22_3_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.3.4.L3')
c_a22_3_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.3.5.L3')
c_a22_3_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.3.6.L3')
c_a22_3_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.3.7.L3')
c_a22_3_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.3.8.L3')
c_a22_4_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.4.1.L3')
c_a22_4_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.4.2.L3')
c_a22_4_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.4.3.L3')
c_a22_4_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.4.4.L3')
c_a22_4_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.4.5.L3')
c_a22_4_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.4.6.L3')
c_a22_4_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.4.7.L3')
c_a22_4_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A22.4.8.L3')
c_a23_1_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.1.1.L3')
c_a23_1_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.1.2.L3')
c_a23_1_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.1.3.L3')
c_a23_1_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.1.4.L3')
c_a23_1_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.1.5.L3')
c_a23_1_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.1.6.L3')
c_a23_1_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.1.7.L3')
c_a23_1_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.1.8.L3')
c_a23_2_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.2.1.L3')
c_a23_2_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.2.2.L3')
c_a23_2_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.2.3.L3')
c_a23_2_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.2.4.L3')
c_a23_2_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.2.5.L3')
c_a23_2_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.2.6.L3')
c_a23_2_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.2.7.L3')
c_a23_2_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.2.8.L3')
c_a23_3_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.3.1.L3')
c_a23_3_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.3.2.L3')
c_a23_3_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.3.3.L3')
c_a23_3_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.3.4.L3')
c_a23_3_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.3.5.L3')
c_a23_3_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.3.6.L3')
c_a23_3_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.3.7.L3')
c_a23_3_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.3.8.L3')
c_a23_4_1_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.4.1.L3')
c_a23_4_2_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.4.2.L3')
c_a23_4_3_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.4.3.L3')
c_a23_4_4_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.4.4.L3')
c_a23_4_5_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.4.5.L3')
c_a23_4_6_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.4.6.L3')
c_a23_4_7_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.4.7.L3')
c_a23_4_8_l3 = Cavity(l=1.0377, v=0.020138888875, freq=1300000000.0, phi=0.0, eid='C.A23.4.8.L3')
c_a24_1_1_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.1.1.L3')
c_a24_1_2_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.1.2.L3')
c_a24_1_3_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.1.3.L3')
c_a24_1_4_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.1.4.L3')
c_a24_1_5_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.1.5.L3')
c_a24_1_6_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.1.6.L3')
c_a24_1_7_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.1.7.L3')
c_a24_1_8_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.1.8.L3')
c_a24_2_1_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.2.1.L3')
c_a24_2_2_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.2.2.L3')
c_a24_2_3_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.2.3.L3')
c_a24_2_4_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.2.4.L3')
c_a24_2_5_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.2.5.L3')
c_a24_2_6_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.2.6.L3')
c_a24_2_7_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.2.7.L3')
c_a24_2_8_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.2.8.L3')
c_a24_3_1_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.3.1.L3')
c_a24_3_2_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.3.2.L3')
c_a24_3_3_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.3.3.L3')
c_a24_3_4_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.3.4.L3')
c_a24_3_5_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.3.5.L3')
c_a24_3_6_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.3.6.L3')
c_a24_3_7_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.3.7.L3')
c_a24_3_8_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.3.8.L3')
c_a24_4_1_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.4.1.L3')
c_a24_4_2_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.4.2.L3')
c_a24_4_3_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.4.3.L3')
c_a24_4_4_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.4.4.L3')
c_a24_4_5_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.4.5.L3')
c_a24_4_6_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.4.6.L3')
c_a24_4_7_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.4.7.L3')
c_a24_4_8_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A24.4.8.L3')
c_a25_1_1_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.1.1.L3')
c_a25_1_2_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.1.2.L3')
c_a25_1_3_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.1.3.L3')
c_a25_1_4_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.1.4.L3')
c_a25_1_5_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.1.5.L3')
c_a25_1_6_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.1.6.L3')
c_a25_1_7_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.1.7.L3')
c_a25_1_8_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.1.8.L3')
c_a25_2_1_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.2.1.L3')
c_a25_2_2_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.2.2.L3')
c_a25_2_3_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.2.3.L3')
c_a25_2_4_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.2.4.L3')
c_a25_2_5_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.2.5.L3')
c_a25_2_6_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.2.6.L3')
c_a25_2_7_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.2.7.L3')
c_a25_2_8_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.2.8.L3')
c_a25_3_1_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.3.1.L3')
c_a25_3_2_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.3.2.L3')
c_a25_3_3_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.3.3.L3')
c_a25_3_4_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.3.4.L3')
c_a25_3_5_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.3.5.L3')
c_a25_3_6_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.3.6.L3')
c_a25_3_7_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.3.7.L3')
c_a25_3_8_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.3.8.L3')
c_a25_4_1_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.4.1.L3')
c_a25_4_2_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.4.2.L3')
c_a25_4_3_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.4.3.L3')
c_a25_4_4_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.4.4.L3')
c_a25_4_5_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.4.5.L3')
c_a25_4_6_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.4.6.L3')
c_a25_4_7_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.4.7.L3')
c_a25_4_8_l3 = Cavity(l=1.0377, v=0.0, freq=1300000000.0, phi=0.0, eid='C.A25.4.8.L3')

# tdcavity 

# UnknowElement 

# Matrices 

# Solenoids 

# lattice 
cell = (stsub_466_b2, d_1, qd_470_b2, d_2, ccy_470_b2, d_3, tora_471_b2, 
d_4, bpma_471_b2, d_5, qd_472_b2, d_6, c_a6_1_1_l3, d_7, c_a6_1_2_l3, 
d_7, c_a6_1_3_l3, d_7, c_a6_1_4_l3, d_7, c_a6_1_5_l3, d_7, c_a6_1_6_l3, 
d_7, c_a6_1_7_l3, d_7, c_a6_1_8_l3, d_14, q_488_l3, d_15, cx_488_l3, 
d_16, bpmc_488_l3, d_17, c_a6_2_1_l3, d_7, c_a6_2_2_l3, d_7, c_a6_2_3_l3, 
d_7, c_a6_2_4_l3, d_7, c_a6_2_5_l3, d_7, c_a6_2_6_l3, d_7, c_a6_2_7_l3, 
d_7, c_a6_2_8_l3, d_14, q_500_l3, d_15, cy_500_l3, d_16, bpmc_500_l3, 
d_17, c_a6_3_1_l3, d_7, c_a6_3_2_l3, d_7, c_a6_3_3_l3, d_7, c_a6_3_4_l3, 
d_7, c_a6_3_5_l3, d_7, c_a6_3_6_l3, d_7, c_a6_3_7_l3, d_7, c_a6_3_8_l3, 
d_14, q_512_l3, d_15, cx_512_l3, d_16, bpmc_512_l3, d_17, c_a6_4_1_l3, 
d_7, c_a6_4_2_l3, d_7, c_a6_4_3_l3, d_7, c_a6_4_4_l3, d_7, c_a6_4_5_l3, 
d_7, c_a6_4_6_l3, d_7, c_a6_4_7_l3, d_7, c_a6_4_8_l3, d_14, q_524_l3, 
d_15, cy_524_l3, d_16, bpmc_524_l3, d_17, c_a7_1_1_l3, d_7, c_a7_1_2_l3, 
d_7, c_a7_1_3_l3, d_7, c_a7_1_4_l3, d_7, c_a7_1_5_l3, d_7, c_a7_1_6_l3, 
d_7, c_a7_1_7_l3, d_7, c_a7_1_8_l3, d_14, q_536_l3, d_15, cx_536_l3, 
d_16, bpmc_536_l3, d_17, c_a7_2_1_l3, d_7, c_a7_2_2_l3, d_7, c_a7_2_3_l3, 
d_7, c_a7_2_4_l3, d_7, c_a7_2_5_l3, d_7, c_a7_2_6_l3, d_7, c_a7_2_7_l3, 
d_7, c_a7_2_8_l3, d_14, q_548_l3, d_15, cy_548_l3, d_16, bpmc_548_l3, 
d_17, c_a7_3_1_l3, d_7, c_a7_3_2_l3, d_7, c_a7_3_3_l3, d_7, c_a7_3_4_l3, 
d_7, c_a7_3_5_l3, d_7, c_a7_3_6_l3, d_7, c_a7_3_7_l3, d_7, c_a7_3_8_l3, 
d_14, q_560_l3, d_15, cx_560_l3, d_16, bpmc_560_l3, d_17, c_a7_4_1_l3, 
d_7, c_a7_4_2_l3, d_7, c_a7_4_3_l3, d_7, c_a7_4_4_l3, d_7, c_a7_4_5_l3, 
d_7, c_a7_4_6_l3, d_7, c_a7_4_7_l3, d_7, c_a7_4_8_l3, d_14, q_572_l3, 
d_15, cy_572_l3, d_16, bpmr_572_l3, d_17, c_a8_1_1_l3, d_7, c_a8_1_2_l3, 
d_7, c_a8_1_3_l3, d_7, c_a8_1_4_l3, d_7, c_a8_1_5_l3, d_7, c_a8_1_6_l3, 
d_7, c_a8_1_7_l3, d_7, c_a8_1_8_l3, d_14, q_584_l3, d_15, cx_584_l3, 
d_16, bpmc_584_l3, d_17, c_a8_2_1_l3, d_7, c_a8_2_2_l3, d_7, c_a8_2_3_l3, 
d_7, c_a8_2_4_l3, d_7, c_a8_2_5_l3, d_7, c_a8_2_6_l3, d_7, c_a8_2_7_l3, 
d_7, c_a8_2_8_l3, d_14, q_596_l3, d_15, cy_596_l3, d_16, bpmc_596_l3, 
d_17, c_a8_3_1_l3, d_7, c_a8_3_2_l3, d_7, c_a8_3_3_l3, d_7, c_a8_3_4_l3, 
d_7, c_a8_3_5_l3, d_7, c_a8_3_6_l3, d_7, c_a8_3_7_l3, d_7, c_a8_3_8_l3, 
d_14, q_608_l3, d_15, cx_608_l3, d_16, bpmr_608_l3, d_17, c_a8_4_1_l3, 
d_7, c_a8_4_2_l3, d_7, c_a8_4_3_l3, d_7, c_a8_4_4_l3, d_7, c_a8_4_5_l3, 
d_7, c_a8_4_6_l3, d_7, c_a8_4_7_l3, d_7, c_a8_4_8_l3, d_14, q_620_l3, 
d_15, cy_620_l3, d_16, bpmc_620_l3, d_138, c_a9_1_1_l3, d_7, c_a9_1_2_l3, 
d_7, c_a9_1_3_l3, d_7, c_a9_1_4_l3, d_7, c_a9_1_5_l3, d_7, c_a9_1_6_l3, 
d_7, c_a9_1_7_l3, d_7, c_a9_1_8_l3, d_14, q_635_l3, d_15, cx_635_l3, 
d_16, bpmc_635_l3, d_17, c_a9_2_1_l3, d_7, c_a9_2_2_l3, d_7, c_a9_2_3_l3, 
d_7, c_a9_2_4_l3, d_7, c_a9_2_5_l3, d_7, c_a9_2_6_l3, d_7, c_a9_2_7_l3, 
d_7, c_a9_2_8_l3, d_14, q_647_l3, d_15, cy_647_l3, d_16, bpmc_647_l3, 
d_17, c_a9_3_1_l3, d_7, c_a9_3_2_l3, d_7, c_a9_3_3_l3, d_7, c_a9_3_4_l3, 
d_7, c_a9_3_5_l3, d_7, c_a9_3_6_l3, d_7, c_a9_3_7_l3, d_7, c_a9_3_8_l3, 
d_14, q_659_l3, d_15, cx_659_l3, d_16, bpmc_659_l3, d_17, c_a9_4_1_l3, 
d_7, c_a9_4_2_l3, d_7, c_a9_4_3_l3, d_7, c_a9_4_4_l3, d_7, c_a9_4_5_l3, 
d_7, c_a9_4_6_l3, d_7, c_a9_4_7_l3, d_7, c_a9_4_8_l3, d_14, q_671_l3, 
d_15, cy_671_l3, d_16, bpmc_671_l3, d_17, c_a10_1_1_l3, d_7, c_a10_1_2_l3, 
d_7, c_a10_1_3_l3, d_7, c_a10_1_4_l3, d_7, c_a10_1_5_l3, d_7, c_a10_1_6_l3, 
d_7, c_a10_1_7_l3, d_7, c_a10_1_8_l3, d_14, q_683_l3, d_15, cx_683_l3, 
d_16, bpmc_683_l3, d_17, c_a10_2_1_l3, d_7, c_a10_2_2_l3, d_7, c_a10_2_3_l3, 
d_7, c_a10_2_4_l3, d_7, c_a10_2_5_l3, d_7, c_a10_2_6_l3, d_7, c_a10_2_7_l3, 
d_7, c_a10_2_8_l3, d_14, q_695_l3, d_15, cy_695_l3, d_16, bpmr_695_l3, 
d_17, c_a10_3_1_l3, d_7, c_a10_3_2_l3, d_7, c_a10_3_3_l3, d_7, c_a10_3_4_l3, 
d_7, c_a10_3_5_l3, d_7, c_a10_3_6_l3, d_7, c_a10_3_7_l3, d_7, c_a10_3_8_l3, 
d_14, q_707_l3, d_15, cx_707_l3, d_16, bpmr_707_l3, d_17, c_a10_4_1_l3, 
d_7, c_a10_4_2_l3, d_7, c_a10_4_3_l3, d_7, c_a10_4_4_l3, d_7, c_a10_4_5_l3, 
d_7, c_a10_4_6_l3, d_7, c_a10_4_7_l3, d_7, c_a10_4_8_l3, d_14, q_719_l3, 
d_15, cy_719_l3, d_16, bpmc_719_l3, d_17, c_a11_1_1_l3, d_7, c_a11_1_2_l3, 
d_7, c_a11_1_3_l3, d_7, c_a11_1_4_l3, d_7, c_a11_1_5_l3, d_7, c_a11_1_6_l3, 
d_7, c_a11_1_7_l3, d_7, c_a11_1_8_l3, d_14, q_731_l3, d_15, cx_731_l3, 
d_16, bpmc_731_l3, d_17, c_a11_2_1_l3, d_7, c_a11_2_2_l3, d_7, c_a11_2_3_l3, 
d_7, c_a11_2_4_l3, d_7, c_a11_2_5_l3, d_7, c_a11_2_6_l3, d_7, c_a11_2_7_l3, 
d_7, c_a11_2_8_l3, d_14, q_743_l3, d_15, cy_743_l3, d_16, bpmc_743_l3, 
d_17, c_a11_3_1_l3, d_7, c_a11_3_2_l3, d_7, c_a11_3_3_l3, d_7, c_a11_3_4_l3, 
d_7, c_a11_3_5_l3, d_7, c_a11_3_6_l3, d_7, c_a11_3_7_l3, d_7, c_a11_3_8_l3, 
d_14, q_755_l3, d_15, cx_755_l3, d_16, bpmr_755_l3, d_17, c_a11_4_1_l3, 
d_7, c_a11_4_2_l3, d_7, c_a11_4_3_l3, d_7, c_a11_4_4_l3, d_7, c_a11_4_5_l3, 
d_7, c_a11_4_6_l3, d_7, c_a11_4_7_l3, d_7, c_a11_4_8_l3, d_14, q_767_l3, 
d_15, cy_767_l3, d_16, bpmc_767_l3, d_138, c_a12_1_1_l3, d_7, c_a12_1_2_l3, 
d_7, c_a12_1_3_l3, d_7, c_a12_1_4_l3, d_7, c_a12_1_5_l3, d_7, c_a12_1_6_l3, 
d_7, c_a12_1_7_l3, d_7, c_a12_1_8_l3, d_14, q_782_l3, d_15, cx_782_l3, 
d_16, bpmc_782_l3, d_17, c_a12_2_1_l3, d_7, c_a12_2_2_l3, d_7, c_a12_2_3_l3, 
d_7, c_a12_2_4_l3, d_7, c_a12_2_5_l3, d_7, c_a12_2_6_l3, d_7, c_a12_2_7_l3, 
d_7, c_a12_2_8_l3, d_14, q_794_l3, d_15, cy_794_l3, d_16, bpmc_794_l3, 
d_17, c_a12_3_1_l3, d_7, c_a12_3_2_l3, d_7, c_a12_3_3_l3, d_7, c_a12_3_4_l3, 
d_7, c_a12_3_5_l3, d_7, c_a12_3_6_l3, d_7, c_a12_3_7_l3, d_7, c_a12_3_8_l3, 
d_14, q_806_l3, d_15, cx_806_l3, d_16, bpmr_806_l3, d_17, c_a12_4_1_l3, 
d_7, c_a12_4_2_l3, d_7, c_a12_4_3_l3, d_7, c_a12_4_4_l3, d_7, c_a12_4_5_l3, 
d_7, c_a12_4_6_l3, d_7, c_a12_4_7_l3, d_7, c_a12_4_8_l3, d_14, q_818_l3, 
d_15, cy_818_l3, d_16, bpmr_818_l3, d_17, c_a13_1_1_l3, d_7, c_a13_1_2_l3, 
d_7, c_a13_1_3_l3, d_7, c_a13_1_4_l3, d_7, c_a13_1_5_l3, d_7, c_a13_1_6_l3, 
d_7, c_a13_1_7_l3, d_7, c_a13_1_8_l3, d_14, q_830_l3, d_15, cx_830_l3, 
d_16, bpmc_830_l3, d_17, c_a13_2_1_l3, d_7, c_a13_2_2_l3, d_7, c_a13_2_3_l3, 
d_7, c_a13_2_4_l3, d_7, c_a13_2_5_l3, d_7, c_a13_2_6_l3, d_7, c_a13_2_7_l3, 
d_7, c_a13_2_8_l3, d_14, q_842_l3, d_15, cy_842_l3, d_16, bpmc_842_l3, 
d_17, c_a13_3_1_l3, d_7, c_a13_3_2_l3, d_7, c_a13_3_3_l3, d_7, c_a13_3_4_l3, 
d_7, c_a13_3_5_l3, d_7, c_a13_3_6_l3, d_7, c_a13_3_7_l3, d_7, c_a13_3_8_l3, 
d_14, q_854_l3, d_15, cx_854_l3, d_16, bpmc_854_l3, d_17, c_a13_4_1_l3, 
d_7, c_a13_4_2_l3, d_7, c_a13_4_3_l3, d_7, c_a13_4_4_l3, d_7, c_a13_4_5_l3, 
d_7, c_a13_4_6_l3, d_7, c_a13_4_7_l3, d_7, c_a13_4_8_l3, d_14, q_866_l3, 
d_15, cy_866_l3, d_16, bpmc_866_l3, d_17, c_a14_1_1_l3, d_7, c_a14_1_2_l3, 
d_7, c_a14_1_3_l3, d_7, c_a14_1_4_l3, d_7, c_a14_1_5_l3, d_7, c_a14_1_6_l3, 
d_7, c_a14_1_7_l3, d_7, c_a14_1_8_l3, d_14, q_878_l3, d_15, cx_878_l3, 
d_16, bpmc_878_l3, d_17, c_a14_2_1_l3, d_7, c_a14_2_2_l3, d_7, c_a14_2_3_l3, 
d_7, c_a14_2_4_l3, d_7, c_a14_2_5_l3, d_7, c_a14_2_6_l3, d_7, c_a14_2_7_l3, 
d_7, c_a14_2_8_l3, d_14, q_890_l3, d_15, cy_890_l3, d_16, bpmc_890_l3, 
d_17, c_a14_3_1_l3, d_7, c_a14_3_2_l3, d_7, c_a14_3_3_l3, d_7, c_a14_3_4_l3, 
d_7, c_a14_3_5_l3, d_7, c_a14_3_6_l3, d_7, c_a14_3_7_l3, d_7, c_a14_3_8_l3, 
d_14, q_902_l3, d_15, cx_902_l3, d_16, bpmc_902_l3, d_17, c_a14_4_1_l3, 
d_7, c_a14_4_2_l3, d_7, c_a14_4_3_l3, d_7, c_a14_4_4_l3, d_7, c_a14_4_5_l3, 
d_7, c_a14_4_6_l3, d_7, c_a14_4_7_l3, d_7, c_a14_4_8_l3, d_14, q_914_l3, 
d_15, cy_914_l3, d_16, bpmc_914_l3, d_138, c_a15_1_1_l3, d_7, c_a15_1_2_l3, 
d_7, c_a15_1_3_l3, d_7, c_a15_1_4_l3, d_7, c_a15_1_5_l3, d_7, c_a15_1_6_l3, 
d_7, c_a15_1_7_l3, d_7, c_a15_1_8_l3, d_14, q_929_l3, d_15, cx_929_l3, 
d_16, bpmc_929_l3, d_17, c_a15_2_1_l3, d_7, c_a15_2_2_l3, d_7, c_a15_2_3_l3, 
d_7, c_a15_2_4_l3, d_7, c_a15_2_5_l3, d_7, c_a15_2_6_l3, d_7, c_a15_2_7_l3, 
d_7, c_a15_2_8_l3, d_14, q_941_l3, d_15, cy_941_l3, d_16, bpmc_941_l3, 
d_17, c_a15_3_1_l3, d_7, c_a15_3_2_l3, d_7, c_a15_3_3_l3, d_7, c_a15_3_4_l3, 
d_7, c_a15_3_5_l3, d_7, c_a15_3_6_l3, d_7, c_a15_3_7_l3, d_7, c_a15_3_8_l3, 
d_14, q_953_l3, d_15, cx_953_l3, d_16, bpmc_953_l3, d_17, c_a15_4_1_l3, 
d_7, c_a15_4_2_l3, d_7, c_a15_4_3_l3, d_7, c_a15_4_4_l3, d_7, c_a15_4_5_l3, 
d_7, c_a15_4_6_l3, d_7, c_a15_4_7_l3, d_7, c_a15_4_8_l3, d_14, q_965_l3, 
d_15, cy_965_l3, d_16, bpmc_965_l3, d_17, c_a16_1_1_l3, d_7, c_a16_1_2_l3, 
d_7, c_a16_1_3_l3, d_7, c_a16_1_4_l3, d_7, c_a16_1_5_l3, d_7, c_a16_1_6_l3, 
d_7, c_a16_1_7_l3, d_7, c_a16_1_8_l3, d_14, q_977_l3, d_15, cx_977_l3, 
d_16, bpmc_977_l3, d_17, c_a16_2_1_l3, d_7, c_a16_2_2_l3, d_7, c_a16_2_3_l3, 
d_7, c_a16_2_4_l3, d_7, c_a16_2_5_l3, d_7, c_a16_2_6_l3, d_7, c_a16_2_7_l3, 
d_7, c_a16_2_8_l3, d_14, q_989_l3, d_15, cy_989_l3, d_16, bpmc_989_l3, 
d_17, c_a16_3_1_l3, d_7, c_a16_3_2_l3, d_7, c_a16_3_3_l3, d_7, c_a16_3_4_l3, 
d_7, c_a16_3_5_l3, d_7, c_a16_3_6_l3, d_7, c_a16_3_7_l3, d_7, c_a16_3_8_l3, 
d_14, q_1001_l3, d_15, cx_1001_l3, d_16, bpmc_1001_l3, d_17, c_a16_4_1_l3, 
d_7, c_a16_4_2_l3, d_7, c_a16_4_3_l3, d_7, c_a16_4_4_l3, d_7, c_a16_4_5_l3, 
d_7, c_a16_4_6_l3, d_7, c_a16_4_7_l3, d_7, c_a16_4_8_l3, d_14, q_1013_l3, 
d_15, cy_1013_l3, d_16, bpmc_1013_l3, d_17, c_a17_1_1_l3, d_7, c_a17_1_2_l3, 
d_7, c_a17_1_3_l3, d_7, c_a17_1_4_l3, d_7, c_a17_1_5_l3, d_7, c_a17_1_6_l3, 
d_7, c_a17_1_7_l3, d_7, c_a17_1_8_l3, d_14, q_1025_l3, d_15, cx_1025_l3, 
d_16, bpmc_1025_l3, d_17, c_a17_2_1_l3, d_7, c_a17_2_2_l3, d_7, c_a17_2_3_l3, 
d_7, c_a17_2_4_l3, d_7, c_a17_2_5_l3, d_7, c_a17_2_6_l3, d_7, c_a17_2_7_l3, 
d_7, c_a17_2_8_l3, d_14, q_1037_l3, d_15, cy_1037_l3, d_16, bpmc_1037_l3, 
d_17, c_a17_3_1_l3, d_7, c_a17_3_2_l3, d_7, c_a17_3_3_l3, d_7, c_a17_3_4_l3, 
d_7, c_a17_3_5_l3, d_7, c_a17_3_6_l3, d_7, c_a17_3_7_l3, d_7, c_a17_3_8_l3, 
d_14, q_1049_l3, d_15, cx_1049_l3, d_16, bpmc_1049_l3, d_17, c_a17_4_1_l3, 
d_7, c_a17_4_2_l3, d_7, c_a17_4_3_l3, d_7, c_a17_4_4_l3, d_7, c_a17_4_5_l3, 
d_7, c_a17_4_6_l3, d_7, c_a17_4_7_l3, d_7, c_a17_4_8_l3, d_14, q_1061_l3, 
d_15, cy_1061_l3, d_16, bpmc_1061_l3, d_138, c_a18_1_1_l3, d_7, c_a18_1_2_l3, 
d_7, c_a18_1_3_l3, d_7, c_a18_1_4_l3, d_7, c_a18_1_5_l3, d_7, c_a18_1_6_l3, 
d_7, c_a18_1_7_l3, d_7, c_a18_1_8_l3, d_14, q_1076_l3, d_15, cx_1076_l3, 
d_16, bpmc_1076_l3, d_17, c_a18_2_1_l3, d_7, c_a18_2_2_l3, d_7, c_a18_2_3_l3, 
d_7, c_a18_2_4_l3, d_7, c_a18_2_5_l3, d_7, c_a18_2_6_l3, d_7, c_a18_2_7_l3, 
d_7, c_a18_2_8_l3, d_14, q_1088_l3, d_15, cy_1088_l3, d_16, bpmr_1088_l3, 
d_17, c_a18_3_1_l3, d_7, c_a18_3_2_l3, d_7, c_a18_3_3_l3, d_7, c_a18_3_4_l3, 
d_7, c_a18_3_5_l3, d_7, c_a18_3_6_l3, d_7, c_a18_3_7_l3, d_7, c_a18_3_8_l3, 
d_14, q_1100_l3, d_15, cx_1100_l3, d_16, bpmc_1100_l3, d_17, c_a18_4_1_l3, 
d_7, c_a18_4_2_l3, d_7, c_a18_4_3_l3, d_7, c_a18_4_4_l3, d_7, c_a18_4_5_l3, 
d_7, c_a18_4_6_l3, d_7, c_a18_4_7_l3, d_7, c_a18_4_8_l3, d_14, q_1112_l3, 
d_15, cy_1112_l3, d_16, bpmr_1112_l3, d_17, c_a19_1_1_l3, d_7, c_a19_1_2_l3, 
d_7, c_a19_1_3_l3, d_7, c_a19_1_4_l3, d_7, c_a19_1_5_l3, d_7, c_a19_1_6_l3, 
d_7, c_a19_1_7_l3, d_7, c_a19_1_8_l3, d_14, q_1124_l3, d_15, cx_1124_l3, 
d_16, bpmc_1124_l3, d_17, c_a19_2_1_l3, d_7, c_a19_2_2_l3, d_7, c_a19_2_3_l3, 
d_7, c_a19_2_4_l3, d_7, c_a19_2_5_l3, d_7, c_a19_2_6_l3, d_7, c_a19_2_7_l3, 
d_7, c_a19_2_8_l3, d_14, q_1136_l3, d_598, bpmc_1136_l3, d_17, c_a19_3_1_l3, 
d_7, c_a19_3_2_l3, d_7, c_a19_3_3_l3, d_7, c_a19_3_4_l3, d_7, c_a19_3_5_l3, 
d_7, c_a19_3_6_l3, d_7, c_a19_3_7_l3, d_7, c_a19_3_8_l3, d_14, q_1147_l3, 
d_15, cx_1148_l3, cy_1148_l3, d_16, bpmc_1148_l3, d_17, c_a19_4_1_l3, d_7, 
c_a19_4_2_l3, d_7, c_a19_4_3_l3, d_7, c_a19_4_4_l3, d_7, c_a19_4_5_l3, d_7, 
c_a19_4_6_l3, d_7, c_a19_4_7_l3, d_7, c_a19_4_8_l3, d_14, q_1159_l3, d_15, 
cy_1160_l3, d_16, bpmc_1160_l3, d_17, c_a20_1_1_l3, d_7, c_a20_1_2_l3, d_7, 
c_a20_1_3_l3, d_7, c_a20_1_4_l3, d_7, c_a20_1_5_l3, d_7, c_a20_1_6_l3, d_7, 
c_a20_1_7_l3, d_7, c_a20_1_8_l3, d_14, q_1171_l3, d_15, cx_1172_l3, d_16, 
bpmr_1172_l3, d_17, c_a20_2_1_l3, d_7, c_a20_2_2_l3, d_7, c_a20_2_3_l3, d_7, 
c_a20_2_4_l3, d_7, c_a20_2_5_l3, d_7, c_a20_2_6_l3, d_7, c_a20_2_7_l3, d_7, 
c_a20_2_8_l3, d_14, q_1183_l3, d_15, cy_1184_l3, d_16, bpmr_1184_l3, d_17, 
c_a20_3_1_l3, d_7, c_a20_3_2_l3, d_7, c_a20_3_3_l3, d_7, c_a20_3_4_l3, d_7, 
c_a20_3_5_l3, d_7, c_a20_3_6_l3, d_7, c_a20_3_7_l3, d_7, c_a20_3_8_l3, d_14, 
q_1195_l3, d_15, cx_1196_l3, d_16, bpmc_1196_l3, d_17, c_a20_4_1_l3, d_7, 
c_a20_4_2_l3, d_7, c_a20_4_3_l3, d_7, c_a20_4_4_l3, d_7, c_a20_4_5_l3, d_7, 
c_a20_4_6_l3, d_7, c_a20_4_7_l3, d_7, c_a20_4_8_l3, d_14, q_1207_l3, d_15, 
cy_1208_l3, d_16, bpmc_1208_l3, d_138, c_a21_1_1_l3, d_7, c_a21_1_2_l3, d_7, 
c_a21_1_3_l3, d_7, c_a21_1_4_l3, d_7, c_a21_1_5_l3, d_7, c_a21_1_6_l3, d_7, 
c_a21_1_7_l3, d_7, c_a21_1_8_l3, d_14, q_1222_l3, d_15, cx_1223_l3, d_16, 
bpmr_1223_l3, d_17, c_a21_2_1_l3, d_7, c_a21_2_2_l3, d_7, c_a21_2_3_l3, d_7, 
c_a21_2_4_l3, d_7, c_a21_2_5_l3, d_7, c_a21_2_6_l3, d_7, c_a21_2_7_l3, d_7, 
c_a21_2_8_l3, d_14, q_1234_l3, d_15, cy_1235_l3, d_16, bpmc_1235_l3, d_17, 
c_a21_3_1_l3, d_7, c_a21_3_2_l3, d_7, c_a21_3_3_l3, d_7, c_a21_3_4_l3, d_7, 
c_a21_3_5_l3, d_7, c_a21_3_6_l3, d_7, c_a21_3_7_l3, d_7, c_a21_3_8_l3, d_14, 
q_1246_l3, d_15, cx_1247_l3, d_16, bpmc_1247_l3, d_17, c_a21_4_1_l3, d_7, 
c_a21_4_2_l3, d_7, c_a21_4_3_l3, d_7, c_a21_4_4_l3, d_7, c_a21_4_5_l3, d_7, 
c_a21_4_6_l3, d_7, c_a21_4_7_l3, d_7, c_a21_4_8_l3, d_14, q_1258_l3, d_15, 
cy_1259_l3, d_16, bpmc_1259_l3, d_17, c_a22_1_1_l3, d_7, c_a22_1_2_l3, d_7, 
c_a22_1_3_l3, d_7, c_a22_1_4_l3, d_7, c_a22_1_5_l3, d_7, c_a22_1_6_l3, d_7, 
c_a22_1_7_l3, d_7, c_a22_1_8_l3, d_14, q_1270_l3, d_15, cx_1271_l3, d_16, 
bpmc_1271_l3, d_17, c_a22_2_1_l3, d_7, c_a22_2_2_l3, d_7, c_a22_2_3_l3, d_7, 
c_a22_2_4_l3, d_7, c_a22_2_5_l3, d_7, c_a22_2_6_l3, d_7, c_a22_2_7_l3, d_7, 
c_a22_2_8_l3, d_14, q_1282_l3, d_15, cy_1283_l3, d_16, bpmc_1283_l3, d_17, 
c_a22_3_1_l3, d_7, c_a22_3_2_l3, d_7, c_a22_3_3_l3, d_7, c_a22_3_4_l3, d_7, 
c_a22_3_5_l3, d_7, c_a22_3_6_l3, d_7, c_a22_3_7_l3, d_7, c_a22_3_8_l3, d_14, 
q_1294_l3, d_15, cx_1295_l3, d_16, bpmc_1295_l3, d_17, c_a22_4_1_l3, d_7, 
c_a22_4_2_l3, d_7, c_a22_4_3_l3, d_7, c_a22_4_4_l3, d_7, c_a22_4_5_l3, d_7, 
c_a22_4_6_l3, d_7, c_a22_4_7_l3, d_7, c_a22_4_8_l3, d_14, q_1306_l3, d_15, 
cy_1307_l3, d_16, bpmr_1307_l3, d_17, c_a23_1_1_l3, d_7, c_a23_1_2_l3, d_7, 
c_a23_1_3_l3, d_7, c_a23_1_4_l3, d_7, c_a23_1_5_l3, d_7, c_a23_1_6_l3, d_7, 
c_a23_1_7_l3, d_7, c_a23_1_8_l3, d_14, q_1318_l3, d_15, cx_1319_l3, d_16, 
bpmc_1319_l3, d_17, c_a23_2_1_l3, d_7, c_a23_2_2_l3, d_7, c_a23_2_3_l3, d_7, 
c_a23_2_4_l3, d_7, c_a23_2_5_l3, d_7, c_a23_2_6_l3, d_7, c_a23_2_7_l3, d_7, 
c_a23_2_8_l3, d_14, q_1330_l3, d_15, cy_1331_l3, d_16, bpmc_1331_l3, d_17, 
c_a23_3_1_l3, d_7, c_a23_3_2_l3, d_7, c_a23_3_3_l3, d_7, c_a23_3_4_l3, d_7, 
c_a23_3_5_l3, d_7, c_a23_3_6_l3, d_7, c_a23_3_7_l3, d_7, c_a23_3_8_l3, d_14, 
q_1342_l3, d_15, cx_1343_l3, d_16, bpmc_1343_l3, d_17, c_a23_4_1_l3, d_7, 
c_a23_4_2_l3, d_7, c_a23_4_3_l3, d_7, c_a23_4_4_l3, d_7, c_a23_4_5_l3, d_7, 
c_a23_4_6_l3, d_7, c_a23_4_7_l3, d_7, c_a23_4_8_l3, d_14, q_1354_l3, d_15, 
cy_1355_l3, d_16, bpmc_1355_l3, d_138, c_a24_1_1_l3, d_7, c_a24_1_2_l3, d_7, 
c_a24_1_3_l3, d_7, c_a24_1_4_l3, d_7, c_a24_1_5_l3, d_7, c_a24_1_6_l3, d_7, 
c_a24_1_7_l3, d_7, c_a24_1_8_l3, d_14, q_1369_l3, d_15, cx_1369_l3, d_16, 
bpmc_1370_l3, d_17, c_a24_2_1_l3, d_7, c_a24_2_2_l3, d_7, c_a24_2_3_l3, d_7, 
c_a24_2_4_l3, d_7, c_a24_2_5_l3, d_7, c_a24_2_6_l3, d_7, c_a24_2_7_l3, d_7, 
c_a24_2_8_l3, d_14, q_1381_l3, d_15, cy_1381_l3, d_16, bpmc_1382_l3, d_17, 
c_a24_3_1_l3, d_7, c_a24_3_2_l3, d_7, c_a24_3_3_l3, d_7, c_a24_3_4_l3, d_7, 
c_a24_3_5_l3, d_7, c_a24_3_6_l3, d_7, c_a24_3_7_l3, d_7, c_a24_3_8_l3, d_14, 
q_1393_l3, d_15, cx_1393_l3, d_16, bpmc_1394_l3, d_17, c_a24_4_1_l3, d_7, 
c_a24_4_2_l3, d_7, c_a24_4_3_l3, d_7, c_a24_4_4_l3, d_7, c_a24_4_5_l3, d_7, 
c_a24_4_6_l3, d_7, c_a24_4_7_l3, d_7, c_a24_4_8_l3, d_14, q_1405_l3, d_15, 
cy_1405_l3, d_16, bpmr_1406_l3, d_17, c_a25_1_1_l3, d_7, c_a25_1_2_l3, d_7, 
c_a25_1_3_l3, d_7, c_a25_1_4_l3, d_7, c_a25_1_5_l3, d_7, c_a25_1_6_l3, d_7, 
c_a25_1_7_l3, d_7, c_a25_1_8_l3, d_14, q_1417_l3, d_15, cx_1417_l3, d_16, 
bpmc_1418_l3, d_17, c_a25_2_1_l3, d_7, c_a25_2_2_l3, d_7, c_a25_2_3_l3, d_7, 
c_a25_2_4_l3, d_7, c_a25_2_5_l3, d_7, c_a25_2_6_l3, d_7, c_a25_2_7_l3, d_7, 
c_a25_2_8_l3, d_14, q_1429_l3, d_15, cy_1429_l3, d_16, bpmr_1430_l3, d_17, 
c_a25_3_1_l3, d_7, c_a25_3_2_l3, d_7, c_a25_3_3_l3, d_7, c_a25_3_4_l3, d_7, 
c_a25_3_5_l3, d_7, c_a25_3_6_l3, d_7, c_a25_3_7_l3, d_7, c_a25_3_8_l3, d_14, 
q_1441_l3, d_15, cx_1441_l3, d_16, bpmc_1442_l3, d_17, c_a25_4_1_l3, d_7, 
c_a25_4_2_l3, d_7, c_a25_4_3_l3, d_7, c_a25_4_4_l3, d_7, c_a25_4_5_l3, d_7, 
c_a25_4_6_l3, d_7, c_a25_4_7_l3, d_7, c_a25_4_8_l3, d_14, q_1453_l3, d_15, 
cy_1453_l3, d_16, bpmc_1454_l3, d_885, tora_1459_l3, d_886, bpma_1475_l3, d_887, 
qb_1475_l3, d_888, cmx_1476_l3, d_889, bpma_1499_l3, d_887, qb_1499_l3, d_888, 
cmy_1500_l3, d_892, otrbw_1523_l3, d_893, bpma_1541_l3, d_894, qe_1542_l3, d_895, 
cex_1542_l3, d_896, bpma_1578_l3, d_894, qe_1578_l3, d_895, cey_1579_l3, d_899, 
otrbw_1597_l3, d_893, bpma_1615_l3, d_894, qe_1615_l3, d_895, cex_1615_l3, d_903, 
bpma_1628_l3, d_894, qe_1629_l3, d_895, cey_1629_l3, d_906, otrbw_1635_l3, d_907, 
bpma_1641_l3, d_908, qf_1641_l3, d_909, cfx_1642_l3, d_910, bpma_1650_l3, d_908, 
qf_1650_l3, d_909, cfy_1651_l3, d_913, stsec_1652_cl)
# power supplies 

#  
qd_470_b2.ps_id = 'QD.24.B2'
qd_472_b2.ps_id = 'QD.25.B2'
q_488_l3.ps_id = 'Q.A6.1.L3'
q_500_l3.ps_id = 'Q.A6.2.L3'
q_512_l3.ps_id = 'Q.A6.3.L3'
q_524_l3.ps_id = 'Q.A6.4.L3'
q_536_l3.ps_id = 'Q.A7.1.L3'
q_548_l3.ps_id = 'Q.A7.2.L3'
q_560_l3.ps_id = 'Q.A7.3.L3'
q_572_l3.ps_id = 'Q.A7.4.L3'
q_584_l3.ps_id = 'Q.A8.1.L3'
q_596_l3.ps_id = 'Q.A8.2.L3'
q_608_l3.ps_id = 'Q.A8.3.L3'
q_620_l3.ps_id = 'Q.A8.4.L3'
q_635_l3.ps_id = 'Q.A9.1.L3'
q_647_l3.ps_id = 'Q.A9.2.L3'
q_659_l3.ps_id = 'Q.A9.3.L3'
q_671_l3.ps_id = 'Q.A9.4.L3'
q_683_l3.ps_id = 'Q.A10.1.L3'
q_695_l3.ps_id = 'Q.A10.2.L3'
q_707_l3.ps_id = 'Q.A10.3.L3'
q_719_l3.ps_id = 'Q.A10.4.L3'
q_731_l3.ps_id = 'Q.A11.1.L3'
q_743_l3.ps_id = 'Q.A11.2.L3'
q_755_l3.ps_id = 'Q.A11.3.L3'
q_767_l3.ps_id = 'Q.A11.4.L3'
q_782_l3.ps_id = 'Q.A12.1.L3'
q_794_l3.ps_id = 'Q.A12.2.L3'
q_806_l3.ps_id = 'Q.A12.3.L3'
q_818_l3.ps_id = 'Q.A12.4.L3'
q_830_l3.ps_id = 'Q.A13.1.L3'
q_842_l3.ps_id = 'Q.A13.2.L3'
q_854_l3.ps_id = 'Q.A13.3.L3'
q_866_l3.ps_id = 'Q.A13.4.L3'
q_878_l3.ps_id = 'Q.A14.1.L3'
q_890_l3.ps_id = 'Q.A14.2.L3'
q_902_l3.ps_id = 'Q.A14.3.L3'
q_914_l3.ps_id = 'Q.A14.4.L3'
q_929_l3.ps_id = 'Q.A15.1.L3'
q_941_l3.ps_id = 'Q.A15.2.L3'
q_953_l3.ps_id = 'Q.A15.3.L3'
q_965_l3.ps_id = 'Q.A15.4.L3'
q_977_l3.ps_id = 'Q.A16.1.L3'
q_989_l3.ps_id = 'Q.A16.2.L3'
q_1001_l3.ps_id = 'Q.A16.3.L3'
q_1013_l3.ps_id = 'Q.A16.4.L3'
q_1025_l3.ps_id = 'Q.A17.1.L3'
q_1037_l3.ps_id = 'Q.A17.2.L3'
q_1049_l3.ps_id = 'Q.A17.3.L3'
q_1061_l3.ps_id = 'Q.A17.4.L3'
q_1076_l3.ps_id = 'Q.A18.1.L3'
q_1088_l3.ps_id = 'Q.A18.2.L3'
q_1100_l3.ps_id = 'Q.A18.3.L3'
q_1112_l3.ps_id = 'Q.A18.4.L3'
q_1124_l3.ps_id = 'Q.A19.1.L3'
q_1136_l3.ps_id = 'Q.A19.2.L3'
q_1147_l3.ps_id = 'Q.A19.3.L3'
q_1159_l3.ps_id = 'Q.A19.4.L3'
q_1171_l3.ps_id = 'Q.A20.1.L3'
q_1183_l3.ps_id = 'Q.A20.2.L3'
q_1195_l3.ps_id = 'Q.A20.3.L3'
q_1207_l3.ps_id = 'Q.A20.4.L3'
q_1222_l3.ps_id = 'Q.A21.1.L3'
q_1234_l3.ps_id = 'Q.A21.2.L3'
q_1246_l3.ps_id = 'Q.A21.3.L3'
q_1258_l3.ps_id = 'Q.A21.4.L3'
q_1270_l3.ps_id = 'Q.A22.1.L3'
q_1282_l3.ps_id = 'Q.A22.2.L3'
q_1294_l3.ps_id = 'Q.A22.3.L3'
q_1306_l3.ps_id = 'Q.A22.4.L3'
q_1318_l3.ps_id = 'Q.A23.1.L3'
q_1330_l3.ps_id = 'Q.A23.2.L3'
q_1342_l3.ps_id = 'Q.A23.3.L3'
q_1354_l3.ps_id = 'Q.A23.4.L3'
q_1369_l3.ps_id = 'Q.A24.1.L3'
q_1381_l3.ps_id = 'Q.A24.2.L3'
q_1393_l3.ps_id = 'Q.A24.3.L3'
q_1405_l3.ps_id = 'Q.A24.4.L3'
q_1417_l3.ps_id = 'Q.A25.1.L3'
q_1429_l3.ps_id = 'Q.A25.2.L3'
q_1441_l3.ps_id = 'Q.A25.3.L3'
q_1453_l3.ps_id = 'Q.A25.4.L3'
qb_1475_l3.ps_id = 'QB.1.L3'
qb_1499_l3.ps_id = 'QB.2.L3'
qe_1542_l3.ps_id = 'QE.1.L3'
qe_1578_l3.ps_id = 'QE.1.L3'
qe_1615_l3.ps_id = 'QE.1.L3'
qe_1629_l3.ps_id = 'QE.2.L3'
qf_1641_l3.ps_id = 'QF.1.L3'
qf_1650_l3.ps_id = 'QF.2.L3'

#  

#  

#  
c_a6_1_1_l3.ps_id = 'C.A6.L3'
c_a6_1_2_l3.ps_id = 'C.A6.L3'
c_a6_1_3_l3.ps_id = 'C.A6.L3'
c_a6_1_4_l3.ps_id = 'C.A6.L3'
c_a6_1_5_l3.ps_id = 'C.A6.L3'
c_a6_1_6_l3.ps_id = 'C.A6.L3'
c_a6_1_7_l3.ps_id = 'C.A6.L3'
c_a6_1_8_l3.ps_id = 'C.A6.L3'
c_a6_2_1_l3.ps_id = 'C.A6.L3'
c_a6_2_2_l3.ps_id = 'C.A6.L3'
c_a6_2_3_l3.ps_id = 'C.A6.L3'
c_a6_2_4_l3.ps_id = 'C.A6.L3'
c_a6_2_5_l3.ps_id = 'C.A6.L3'
c_a6_2_6_l3.ps_id = 'C.A6.L3'
c_a6_2_7_l3.ps_id = 'C.A6.L3'
c_a6_2_8_l3.ps_id = 'C.A6.L3'
c_a6_3_1_l3.ps_id = 'C.A6.L3'
c_a6_3_2_l3.ps_id = 'C.A6.L3'
c_a6_3_3_l3.ps_id = 'C.A6.L3'
c_a6_3_4_l3.ps_id = 'C.A6.L3'
c_a6_3_5_l3.ps_id = 'C.A6.L3'
c_a6_3_6_l3.ps_id = 'C.A6.L3'
c_a6_3_7_l3.ps_id = 'C.A6.L3'
c_a6_3_8_l3.ps_id = 'C.A6.L3'
c_a6_4_1_l3.ps_id = 'C.A6.L3'
c_a6_4_2_l3.ps_id = 'C.A6.L3'
c_a6_4_3_l3.ps_id = 'C.A6.L3'
c_a6_4_4_l3.ps_id = 'C.A6.L3'
c_a6_4_5_l3.ps_id = 'C.A6.L3'
c_a6_4_6_l3.ps_id = 'C.A6.L3'
c_a6_4_7_l3.ps_id = 'C.A6.L3'
c_a6_4_8_l3.ps_id = 'C.A6.L3'
c_a7_1_1_l3.ps_id = 'C.A7.L3'
c_a7_1_2_l3.ps_id = 'C.A7.L3'
c_a7_1_3_l3.ps_id = 'C.A7.L3'
c_a7_1_4_l3.ps_id = 'C.A7.L3'
c_a7_1_5_l3.ps_id = 'C.A7.L3'
c_a7_1_6_l3.ps_id = 'C.A7.L3'
c_a7_1_7_l3.ps_id = 'C.A7.L3'
c_a7_1_8_l3.ps_id = 'C.A7.L3'
c_a7_2_1_l3.ps_id = 'C.A7.L3'
c_a7_2_2_l3.ps_id = 'C.A7.L3'
c_a7_2_3_l3.ps_id = 'C.A7.L3'
c_a7_2_4_l3.ps_id = 'C.A7.L3'
c_a7_2_5_l3.ps_id = 'C.A7.L3'
c_a7_2_6_l3.ps_id = 'C.A7.L3'
c_a7_2_7_l3.ps_id = 'C.A7.L3'
c_a7_2_8_l3.ps_id = 'C.A7.L3'
c_a7_3_1_l3.ps_id = 'C.A7.L3'
c_a7_3_2_l3.ps_id = 'C.A7.L3'
c_a7_3_3_l3.ps_id = 'C.A7.L3'
c_a7_3_4_l3.ps_id = 'C.A7.L3'
c_a7_3_5_l3.ps_id = 'C.A7.L3'
c_a7_3_6_l3.ps_id = 'C.A7.L3'
c_a7_3_7_l3.ps_id = 'C.A7.L3'
c_a7_3_8_l3.ps_id = 'C.A7.L3'
c_a7_4_1_l3.ps_id = 'C.A7.L3'
c_a7_4_2_l3.ps_id = 'C.A7.L3'
c_a7_4_3_l3.ps_id = 'C.A7.L3'
c_a7_4_4_l3.ps_id = 'C.A7.L3'
c_a7_4_5_l3.ps_id = 'C.A7.L3'
c_a7_4_6_l3.ps_id = 'C.A7.L3'
c_a7_4_7_l3.ps_id = 'C.A7.L3'
c_a7_4_8_l3.ps_id = 'C.A7.L3'
c_a8_1_1_l3.ps_id = 'C.A8.L3'
c_a8_1_2_l3.ps_id = 'C.A8.L3'
c_a8_1_3_l3.ps_id = 'C.A8.L3'
c_a8_1_4_l3.ps_id = 'C.A8.L3'
c_a8_1_5_l3.ps_id = 'C.A8.L3'
c_a8_1_6_l3.ps_id = 'C.A8.L3'
c_a8_1_7_l3.ps_id = 'C.A8.L3'
c_a8_1_8_l3.ps_id = 'C.A8.L3'
c_a8_2_1_l3.ps_id = 'C.A8.L3'
c_a8_2_2_l3.ps_id = 'C.A8.L3'
c_a8_2_3_l3.ps_id = 'C.A8.L3'
c_a8_2_4_l3.ps_id = 'C.A8.L3'
c_a8_2_5_l3.ps_id = 'C.A8.L3'
c_a8_2_6_l3.ps_id = 'C.A8.L3'
c_a8_2_7_l3.ps_id = 'C.A8.L3'
c_a8_2_8_l3.ps_id = 'C.A8.L3'
c_a8_3_1_l3.ps_id = 'C.A8.L3'
c_a8_3_2_l3.ps_id = 'C.A8.L3'
c_a8_3_3_l3.ps_id = 'C.A8.L3'
c_a8_3_4_l3.ps_id = 'C.A8.L3'
c_a8_3_5_l3.ps_id = 'C.A8.L3'
c_a8_3_6_l3.ps_id = 'C.A8.L3'
c_a8_3_7_l3.ps_id = 'C.A8.L3'
c_a8_3_8_l3.ps_id = 'C.A8.L3'
c_a8_4_1_l3.ps_id = 'C.A8.L3'
c_a8_4_2_l3.ps_id = 'C.A8.L3'
c_a8_4_3_l3.ps_id = 'C.A8.L3'
c_a8_4_4_l3.ps_id = 'C.A8.L3'
c_a8_4_5_l3.ps_id = 'C.A8.L3'
c_a8_4_6_l3.ps_id = 'C.A8.L3'
c_a8_4_7_l3.ps_id = 'C.A8.L3'
c_a8_4_8_l3.ps_id = 'C.A8.L3'
c_a9_1_1_l3.ps_id = 'C.A9.L3'
c_a9_1_2_l3.ps_id = 'C.A9.L3'
c_a9_1_3_l3.ps_id = 'C.A9.L3'
c_a9_1_4_l3.ps_id = 'C.A9.L3'
c_a9_1_5_l3.ps_id = 'C.A9.L3'
c_a9_1_6_l3.ps_id = 'C.A9.L3'
c_a9_1_7_l3.ps_id = 'C.A9.L3'
c_a9_1_8_l3.ps_id = 'C.A9.L3'
c_a9_2_1_l3.ps_id = 'C.A9.L3'
c_a9_2_2_l3.ps_id = 'C.A9.L3'
c_a9_2_3_l3.ps_id = 'C.A9.L3'
c_a9_2_4_l3.ps_id = 'C.A9.L3'
c_a9_2_5_l3.ps_id = 'C.A9.L3'
c_a9_2_6_l3.ps_id = 'C.A9.L3'
c_a9_2_7_l3.ps_id = 'C.A9.L3'
c_a9_2_8_l3.ps_id = 'C.A9.L3'
c_a9_3_1_l3.ps_id = 'C.A9.L3'
c_a9_3_2_l3.ps_id = 'C.A9.L3'
c_a9_3_3_l3.ps_id = 'C.A9.L3'
c_a9_3_4_l3.ps_id = 'C.A9.L3'
c_a9_3_5_l3.ps_id = 'C.A9.L3'
c_a9_3_6_l3.ps_id = 'C.A9.L3'
c_a9_3_7_l3.ps_id = 'C.A9.L3'
c_a9_3_8_l3.ps_id = 'C.A9.L3'
c_a9_4_1_l3.ps_id = 'C.A9.L3'
c_a9_4_2_l3.ps_id = 'C.A9.L3'
c_a9_4_3_l3.ps_id = 'C.A9.L3'
c_a9_4_4_l3.ps_id = 'C.A9.L3'
c_a9_4_5_l3.ps_id = 'C.A9.L3'
c_a9_4_6_l3.ps_id = 'C.A9.L3'
c_a9_4_7_l3.ps_id = 'C.A9.L3'
c_a9_4_8_l3.ps_id = 'C.A9.L3'
c_a10_1_1_l3.ps_id = 'C.A10.L3'
c_a10_1_2_l3.ps_id = 'C.A10.L3'
c_a10_1_3_l3.ps_id = 'C.A10.L3'
c_a10_1_4_l3.ps_id = 'C.A10.L3'
c_a10_1_5_l3.ps_id = 'C.A10.L3'
c_a10_1_6_l3.ps_id = 'C.A10.L3'
c_a10_1_7_l3.ps_id = 'C.A10.L3'
c_a10_1_8_l3.ps_id = 'C.A10.L3'
c_a10_2_1_l3.ps_id = 'C.A10.L3'
c_a10_2_2_l3.ps_id = 'C.A10.L3'
c_a10_2_3_l3.ps_id = 'C.A10.L3'
c_a10_2_4_l3.ps_id = 'C.A10.L3'
c_a10_2_5_l3.ps_id = 'C.A10.L3'
c_a10_2_6_l3.ps_id = 'C.A10.L3'
c_a10_2_7_l3.ps_id = 'C.A10.L3'
c_a10_2_8_l3.ps_id = 'C.A10.L3'
c_a10_3_1_l3.ps_id = 'C.A10.L3'
c_a10_3_2_l3.ps_id = 'C.A10.L3'
c_a10_3_3_l3.ps_id = 'C.A10.L3'
c_a10_3_4_l3.ps_id = 'C.A10.L3'
c_a10_3_5_l3.ps_id = 'C.A10.L3'
c_a10_3_6_l3.ps_id = 'C.A10.L3'
c_a10_3_7_l3.ps_id = 'C.A10.L3'
c_a10_3_8_l3.ps_id = 'C.A10.L3'
c_a10_4_1_l3.ps_id = 'C.A10.L3'
c_a10_4_2_l3.ps_id = 'C.A10.L3'
c_a10_4_3_l3.ps_id = 'C.A10.L3'
c_a10_4_4_l3.ps_id = 'C.A10.L3'
c_a10_4_5_l3.ps_id = 'C.A10.L3'
c_a10_4_6_l3.ps_id = 'C.A10.L3'
c_a10_4_7_l3.ps_id = 'C.A10.L3'
c_a10_4_8_l3.ps_id = 'C.A10.L3'
c_a11_1_1_l3.ps_id = 'C.A11.L3'
c_a11_1_2_l3.ps_id = 'C.A11.L3'
c_a11_1_3_l3.ps_id = 'C.A11.L3'
c_a11_1_4_l3.ps_id = 'C.A11.L3'
c_a11_1_5_l3.ps_id = 'C.A11.L3'
c_a11_1_6_l3.ps_id = 'C.A11.L3'
c_a11_1_7_l3.ps_id = 'C.A11.L3'
c_a11_1_8_l3.ps_id = 'C.A11.L3'
c_a11_2_1_l3.ps_id = 'C.A11.L3'
c_a11_2_2_l3.ps_id = 'C.A11.L3'
c_a11_2_3_l3.ps_id = 'C.A11.L3'
c_a11_2_4_l3.ps_id = 'C.A11.L3'
c_a11_2_5_l3.ps_id = 'C.A11.L3'
c_a11_2_6_l3.ps_id = 'C.A11.L3'
c_a11_2_7_l3.ps_id = 'C.A11.L3'
c_a11_2_8_l3.ps_id = 'C.A11.L3'
c_a11_3_1_l3.ps_id = 'C.A11.L3'
c_a11_3_2_l3.ps_id = 'C.A11.L3'
c_a11_3_3_l3.ps_id = 'C.A11.L3'
c_a11_3_4_l3.ps_id = 'C.A11.L3'
c_a11_3_5_l3.ps_id = 'C.A11.L3'
c_a11_3_6_l3.ps_id = 'C.A11.L3'
c_a11_3_7_l3.ps_id = 'C.A11.L3'
c_a11_3_8_l3.ps_id = 'C.A11.L3'
c_a11_4_1_l3.ps_id = 'C.A11.L3'
c_a11_4_2_l3.ps_id = 'C.A11.L3'
c_a11_4_3_l3.ps_id = 'C.A11.L3'
c_a11_4_4_l3.ps_id = 'C.A11.L3'
c_a11_4_5_l3.ps_id = 'C.A11.L3'
c_a11_4_6_l3.ps_id = 'C.A11.L3'
c_a11_4_7_l3.ps_id = 'C.A11.L3'
c_a11_4_8_l3.ps_id = 'C.A11.L3'
c_a12_1_1_l3.ps_id = 'C.A12.L3'
c_a12_1_2_l3.ps_id = 'C.A12.L3'
c_a12_1_3_l3.ps_id = 'C.A12.L3'
c_a12_1_4_l3.ps_id = 'C.A12.L3'
c_a12_1_5_l3.ps_id = 'C.A12.L3'
c_a12_1_6_l3.ps_id = 'C.A12.L3'
c_a12_1_7_l3.ps_id = 'C.A12.L3'
c_a12_1_8_l3.ps_id = 'C.A12.L3'
c_a12_2_1_l3.ps_id = 'C.A12.L3'
c_a12_2_2_l3.ps_id = 'C.A12.L3'
c_a12_2_3_l3.ps_id = 'C.A12.L3'
c_a12_2_4_l3.ps_id = 'C.A12.L3'
c_a12_2_5_l3.ps_id = 'C.A12.L3'
c_a12_2_6_l3.ps_id = 'C.A12.L3'
c_a12_2_7_l3.ps_id = 'C.A12.L3'
c_a12_2_8_l3.ps_id = 'C.A12.L3'
c_a12_3_1_l3.ps_id = 'C.A12.L3'
c_a12_3_2_l3.ps_id = 'C.A12.L3'
c_a12_3_3_l3.ps_id = 'C.A12.L3'
c_a12_3_4_l3.ps_id = 'C.A12.L3'
c_a12_3_5_l3.ps_id = 'C.A12.L3'
c_a12_3_6_l3.ps_id = 'C.A12.L3'
c_a12_3_7_l3.ps_id = 'C.A12.L3'
c_a12_3_8_l3.ps_id = 'C.A12.L3'
c_a12_4_1_l3.ps_id = 'C.A12.L3'
c_a12_4_2_l3.ps_id = 'C.A12.L3'
c_a12_4_3_l3.ps_id = 'C.A12.L3'
c_a12_4_4_l3.ps_id = 'C.A12.L3'
c_a12_4_5_l3.ps_id = 'C.A12.L3'
c_a12_4_6_l3.ps_id = 'C.A12.L3'
c_a12_4_7_l3.ps_id = 'C.A12.L3'
c_a12_4_8_l3.ps_id = 'C.A12.L3'
c_a13_1_1_l3.ps_id = 'C.A13.L3'
c_a13_1_2_l3.ps_id = 'C.A13.L3'
c_a13_1_3_l3.ps_id = 'C.A13.L3'
c_a13_1_4_l3.ps_id = 'C.A13.L3'
c_a13_1_5_l3.ps_id = 'C.A13.L3'
c_a13_1_6_l3.ps_id = 'C.A13.L3'
c_a13_1_7_l3.ps_id = 'C.A13.L3'
c_a13_1_8_l3.ps_id = 'C.A13.L3'
c_a13_2_1_l3.ps_id = 'C.A13.L3'
c_a13_2_2_l3.ps_id = 'C.A13.L3'
c_a13_2_3_l3.ps_id = 'C.A13.L3'
c_a13_2_4_l3.ps_id = 'C.A13.L3'
c_a13_2_5_l3.ps_id = 'C.A13.L3'
c_a13_2_6_l3.ps_id = 'C.A13.L3'
c_a13_2_7_l3.ps_id = 'C.A13.L3'
c_a13_2_8_l3.ps_id = 'C.A13.L3'
c_a13_3_1_l3.ps_id = 'C.A13.L3'
c_a13_3_2_l3.ps_id = 'C.A13.L3'
c_a13_3_3_l3.ps_id = 'C.A13.L3'
c_a13_3_4_l3.ps_id = 'C.A13.L3'
c_a13_3_5_l3.ps_id = 'C.A13.L3'
c_a13_3_6_l3.ps_id = 'C.A13.L3'
c_a13_3_7_l3.ps_id = 'C.A13.L3'
c_a13_3_8_l3.ps_id = 'C.A13.L3'
c_a13_4_1_l3.ps_id = 'C.A13.L3'
c_a13_4_2_l3.ps_id = 'C.A13.L3'
c_a13_4_3_l3.ps_id = 'C.A13.L3'
c_a13_4_4_l3.ps_id = 'C.A13.L3'
c_a13_4_5_l3.ps_id = 'C.A13.L3'
c_a13_4_6_l3.ps_id = 'C.A13.L3'
c_a13_4_7_l3.ps_id = 'C.A13.L3'
c_a13_4_8_l3.ps_id = 'C.A13.L3'
c_a14_1_1_l3.ps_id = 'C.A14.L3'
c_a14_1_2_l3.ps_id = 'C.A14.L3'
c_a14_1_3_l3.ps_id = 'C.A14.L3'
c_a14_1_4_l3.ps_id = 'C.A14.L3'
c_a14_1_5_l3.ps_id = 'C.A14.L3'
c_a14_1_6_l3.ps_id = 'C.A14.L3'
c_a14_1_7_l3.ps_id = 'C.A14.L3'
c_a14_1_8_l3.ps_id = 'C.A14.L3'
c_a14_2_1_l3.ps_id = 'C.A14.L3'
c_a14_2_2_l3.ps_id = 'C.A14.L3'
c_a14_2_3_l3.ps_id = 'C.A14.L3'
c_a14_2_4_l3.ps_id = 'C.A14.L3'
c_a14_2_5_l3.ps_id = 'C.A14.L3'
c_a14_2_6_l3.ps_id = 'C.A14.L3'
c_a14_2_7_l3.ps_id = 'C.A14.L3'
c_a14_2_8_l3.ps_id = 'C.A14.L3'
c_a14_3_1_l3.ps_id = 'C.A14.L3'
c_a14_3_2_l3.ps_id = 'C.A14.L3'
c_a14_3_3_l3.ps_id = 'C.A14.L3'
c_a14_3_4_l3.ps_id = 'C.A14.L3'
c_a14_3_5_l3.ps_id = 'C.A14.L3'
c_a14_3_6_l3.ps_id = 'C.A14.L3'
c_a14_3_7_l3.ps_id = 'C.A14.L3'
c_a14_3_8_l3.ps_id = 'C.A14.L3'
c_a14_4_1_l3.ps_id = 'C.A14.L3'
c_a14_4_2_l3.ps_id = 'C.A14.L3'
c_a14_4_3_l3.ps_id = 'C.A14.L3'
c_a14_4_4_l3.ps_id = 'C.A14.L3'
c_a14_4_5_l3.ps_id = 'C.A14.L3'
c_a14_4_6_l3.ps_id = 'C.A14.L3'
c_a14_4_7_l3.ps_id = 'C.A14.L3'
c_a14_4_8_l3.ps_id = 'C.A14.L3'
c_a15_1_1_l3.ps_id = 'C.A15.L3'
c_a15_1_2_l3.ps_id = 'C.A15.L3'
c_a15_1_3_l3.ps_id = 'C.A15.L3'
c_a15_1_4_l3.ps_id = 'C.A15.L3'
c_a15_1_5_l3.ps_id = 'C.A15.L3'
c_a15_1_6_l3.ps_id = 'C.A15.L3'
c_a15_1_7_l3.ps_id = 'C.A15.L3'
c_a15_1_8_l3.ps_id = 'C.A15.L3'
c_a15_2_1_l3.ps_id = 'C.A15.L3'
c_a15_2_2_l3.ps_id = 'C.A15.L3'
c_a15_2_3_l3.ps_id = 'C.A15.L3'
c_a15_2_4_l3.ps_id = 'C.A15.L3'
c_a15_2_5_l3.ps_id = 'C.A15.L3'
c_a15_2_6_l3.ps_id = 'C.A15.L3'
c_a15_2_7_l3.ps_id = 'C.A15.L3'
c_a15_2_8_l3.ps_id = 'C.A15.L3'
c_a15_3_1_l3.ps_id = 'C.A15.L3'
c_a15_3_2_l3.ps_id = 'C.A15.L3'
c_a15_3_3_l3.ps_id = 'C.A15.L3'
c_a15_3_4_l3.ps_id = 'C.A15.L3'
c_a15_3_5_l3.ps_id = 'C.A15.L3'
c_a15_3_6_l3.ps_id = 'C.A15.L3'
c_a15_3_7_l3.ps_id = 'C.A15.L3'
c_a15_3_8_l3.ps_id = 'C.A15.L3'
c_a15_4_1_l3.ps_id = 'C.A15.L3'
c_a15_4_2_l3.ps_id = 'C.A15.L3'
c_a15_4_3_l3.ps_id = 'C.A15.L3'
c_a15_4_4_l3.ps_id = 'C.A15.L3'
c_a15_4_5_l3.ps_id = 'C.A15.L3'
c_a15_4_6_l3.ps_id = 'C.A15.L3'
c_a15_4_7_l3.ps_id = 'C.A15.L3'
c_a15_4_8_l3.ps_id = 'C.A15.L3'
c_a16_1_1_l3.ps_id = 'C.A16.L3'
c_a16_1_2_l3.ps_id = 'C.A16.L3'
c_a16_1_3_l3.ps_id = 'C.A16.L3'
c_a16_1_4_l3.ps_id = 'C.A16.L3'
c_a16_1_5_l3.ps_id = 'C.A16.L3'
c_a16_1_6_l3.ps_id = 'C.A16.L3'
c_a16_1_7_l3.ps_id = 'C.A16.L3'
c_a16_1_8_l3.ps_id = 'C.A16.L3'
c_a16_2_1_l3.ps_id = 'C.A16.L3'
c_a16_2_2_l3.ps_id = 'C.A16.L3'
c_a16_2_3_l3.ps_id = 'C.A16.L3'
c_a16_2_4_l3.ps_id = 'C.A16.L3'
c_a16_2_5_l3.ps_id = 'C.A16.L3'
c_a16_2_6_l3.ps_id = 'C.A16.L3'
c_a16_2_7_l3.ps_id = 'C.A16.L3'
c_a16_2_8_l3.ps_id = 'C.A16.L3'
c_a16_3_1_l3.ps_id = 'C.A16.L3'
c_a16_3_2_l3.ps_id = 'C.A16.L3'
c_a16_3_3_l3.ps_id = 'C.A16.L3'
c_a16_3_4_l3.ps_id = 'C.A16.L3'
c_a16_3_5_l3.ps_id = 'C.A16.L3'
c_a16_3_6_l3.ps_id = 'C.A16.L3'
c_a16_3_7_l3.ps_id = 'C.A16.L3'
c_a16_3_8_l3.ps_id = 'C.A16.L3'
c_a16_4_1_l3.ps_id = 'C.A16.L3'
c_a16_4_2_l3.ps_id = 'C.A16.L3'
c_a16_4_3_l3.ps_id = 'C.A16.L3'
c_a16_4_4_l3.ps_id = 'C.A16.L3'
c_a16_4_5_l3.ps_id = 'C.A16.L3'
c_a16_4_6_l3.ps_id = 'C.A16.L3'
c_a16_4_7_l3.ps_id = 'C.A16.L3'
c_a16_4_8_l3.ps_id = 'C.A16.L3'
c_a17_1_1_l3.ps_id = 'C.A17.L3'
c_a17_1_2_l3.ps_id = 'C.A17.L3'
c_a17_1_3_l3.ps_id = 'C.A17.L3'
c_a17_1_4_l3.ps_id = 'C.A17.L3'
c_a17_1_5_l3.ps_id = 'C.A17.L3'
c_a17_1_6_l3.ps_id = 'C.A17.L3'
c_a17_1_7_l3.ps_id = 'C.A17.L3'
c_a17_1_8_l3.ps_id = 'C.A17.L3'
c_a17_2_1_l3.ps_id = 'C.A17.L3'
c_a17_2_2_l3.ps_id = 'C.A17.L3'
c_a17_2_3_l3.ps_id = 'C.A17.L3'
c_a17_2_4_l3.ps_id = 'C.A17.L3'
c_a17_2_5_l3.ps_id = 'C.A17.L3'
c_a17_2_6_l3.ps_id = 'C.A17.L3'
c_a17_2_7_l3.ps_id = 'C.A17.L3'
c_a17_2_8_l3.ps_id = 'C.A17.L3'
c_a17_3_1_l3.ps_id = 'C.A17.L3'
c_a17_3_2_l3.ps_id = 'C.A17.L3'
c_a17_3_3_l3.ps_id = 'C.A17.L3'
c_a17_3_4_l3.ps_id = 'C.A17.L3'
c_a17_3_5_l3.ps_id = 'C.A17.L3'
c_a17_3_6_l3.ps_id = 'C.A17.L3'
c_a17_3_7_l3.ps_id = 'C.A17.L3'
c_a17_3_8_l3.ps_id = 'C.A17.L3'
c_a17_4_1_l3.ps_id = 'C.A17.L3'
c_a17_4_2_l3.ps_id = 'C.A17.L3'
c_a17_4_3_l3.ps_id = 'C.A17.L3'
c_a17_4_4_l3.ps_id = 'C.A17.L3'
c_a17_4_5_l3.ps_id = 'C.A17.L3'
c_a17_4_6_l3.ps_id = 'C.A17.L3'
c_a17_4_7_l3.ps_id = 'C.A17.L3'
c_a17_4_8_l3.ps_id = 'C.A17.L3'
c_a18_1_1_l3.ps_id = 'C.A18.L3'
c_a18_1_2_l3.ps_id = 'C.A18.L3'
c_a18_1_3_l3.ps_id = 'C.A18.L3'
c_a18_1_4_l3.ps_id = 'C.A18.L3'
c_a18_1_5_l3.ps_id = 'C.A18.L3'
c_a18_1_6_l3.ps_id = 'C.A18.L3'
c_a18_1_7_l3.ps_id = 'C.A18.L3'
c_a18_1_8_l3.ps_id = 'C.A18.L3'
c_a18_2_1_l3.ps_id = 'C.A18.L3'
c_a18_2_2_l3.ps_id = 'C.A18.L3'
c_a18_2_3_l3.ps_id = 'C.A18.L3'
c_a18_2_4_l3.ps_id = 'C.A18.L3'
c_a18_2_5_l3.ps_id = 'C.A18.L3'
c_a18_2_6_l3.ps_id = 'C.A18.L3'
c_a18_2_7_l3.ps_id = 'C.A18.L3'
c_a18_2_8_l3.ps_id = 'C.A18.L3'
c_a18_3_1_l3.ps_id = 'C.A18.L3'
c_a18_3_2_l3.ps_id = 'C.A18.L3'
c_a18_3_3_l3.ps_id = 'C.A18.L3'
c_a18_3_4_l3.ps_id = 'C.A18.L3'
c_a18_3_5_l3.ps_id = 'C.A18.L3'
c_a18_3_6_l3.ps_id = 'C.A18.L3'
c_a18_3_7_l3.ps_id = 'C.A18.L3'
c_a18_3_8_l3.ps_id = 'C.A18.L3'
c_a18_4_1_l3.ps_id = 'C.A18.L3'
c_a18_4_2_l3.ps_id = 'C.A18.L3'
c_a18_4_3_l3.ps_id = 'C.A18.L3'
c_a18_4_4_l3.ps_id = 'C.A18.L3'
c_a18_4_5_l3.ps_id = 'C.A18.L3'
c_a18_4_6_l3.ps_id = 'C.A18.L3'
c_a18_4_7_l3.ps_id = 'C.A18.L3'
c_a18_4_8_l3.ps_id = 'C.A18.L3'
c_a19_1_1_l3.ps_id = 'C.A19.L3'
c_a19_1_2_l3.ps_id = 'C.A19.L3'
c_a19_1_3_l3.ps_id = 'C.A19.L3'
c_a19_1_4_l3.ps_id = 'C.A19.L3'
c_a19_1_5_l3.ps_id = 'C.A19.L3'
c_a19_1_6_l3.ps_id = 'C.A19.L3'
c_a19_1_7_l3.ps_id = 'C.A19.L3'
c_a19_1_8_l3.ps_id = 'C.A19.L3'
c_a19_2_1_l3.ps_id = 'C.A19.L3'
c_a19_2_2_l3.ps_id = 'C.A19.L3'
c_a19_2_3_l3.ps_id = 'C.A19.L3'
c_a19_2_4_l3.ps_id = 'C.A19.L3'
c_a19_2_5_l3.ps_id = 'C.A19.L3'
c_a19_2_6_l3.ps_id = 'C.A19.L3'
c_a19_2_7_l3.ps_id = 'C.A19.L3'
c_a19_2_8_l3.ps_id = 'C.A19.L3'
c_a19_3_1_l3.ps_id = 'C.A19.L3'
c_a19_3_2_l3.ps_id = 'C.A19.L3'
c_a19_3_3_l3.ps_id = 'C.A19.L3'
c_a19_3_4_l3.ps_id = 'C.A19.L3'
c_a19_3_5_l3.ps_id = 'C.A19.L3'
c_a19_3_6_l3.ps_id = 'C.A19.L3'
c_a19_3_7_l3.ps_id = 'C.A19.L3'
c_a19_3_8_l3.ps_id = 'C.A19.L3'
c_a19_4_1_l3.ps_id = 'C.A19.L3'
c_a19_4_2_l3.ps_id = 'C.A19.L3'
c_a19_4_3_l3.ps_id = 'C.A19.L3'
c_a19_4_4_l3.ps_id = 'C.A19.L3'
c_a19_4_5_l3.ps_id = 'C.A19.L3'
c_a19_4_6_l3.ps_id = 'C.A19.L3'
c_a19_4_7_l3.ps_id = 'C.A19.L3'
c_a19_4_8_l3.ps_id = 'C.A19.L3'
c_a20_1_1_l3.ps_id = 'C.A20.L3'
c_a20_1_2_l3.ps_id = 'C.A20.L3'
c_a20_1_3_l3.ps_id = 'C.A20.L3'
c_a20_1_4_l3.ps_id = 'C.A20.L3'
c_a20_1_5_l3.ps_id = 'C.A20.L3'
c_a20_1_6_l3.ps_id = 'C.A20.L3'
c_a20_1_7_l3.ps_id = 'C.A20.L3'
c_a20_1_8_l3.ps_id = 'C.A20.L3'
c_a20_2_1_l3.ps_id = 'C.A20.L3'
c_a20_2_2_l3.ps_id = 'C.A20.L3'
c_a20_2_3_l3.ps_id = 'C.A20.L3'
c_a20_2_4_l3.ps_id = 'C.A20.L3'
c_a20_2_5_l3.ps_id = 'C.A20.L3'
c_a20_2_6_l3.ps_id = 'C.A20.L3'
c_a20_2_7_l3.ps_id = 'C.A20.L3'
c_a20_2_8_l3.ps_id = 'C.A20.L3'
c_a20_3_1_l3.ps_id = 'C.A20.L3'
c_a20_3_2_l3.ps_id = 'C.A20.L3'
c_a20_3_3_l3.ps_id = 'C.A20.L3'
c_a20_3_4_l3.ps_id = 'C.A20.L3'
c_a20_3_5_l3.ps_id = 'C.A20.L3'
c_a20_3_6_l3.ps_id = 'C.A20.L3'
c_a20_3_7_l3.ps_id = 'C.A20.L3'
c_a20_3_8_l3.ps_id = 'C.A20.L3'
c_a20_4_1_l3.ps_id = 'C.A20.L3'
c_a20_4_2_l3.ps_id = 'C.A20.L3'
c_a20_4_3_l3.ps_id = 'C.A20.L3'
c_a20_4_4_l3.ps_id = 'C.A20.L3'
c_a20_4_5_l3.ps_id = 'C.A20.L3'
c_a20_4_6_l3.ps_id = 'C.A20.L3'
c_a20_4_7_l3.ps_id = 'C.A20.L3'
c_a20_4_8_l3.ps_id = 'C.A20.L3'
c_a21_1_1_l3.ps_id = 'C.A21.L3'
c_a21_1_2_l3.ps_id = 'C.A21.L3'
c_a21_1_3_l3.ps_id = 'C.A21.L3'
c_a21_1_4_l3.ps_id = 'C.A21.L3'
c_a21_1_5_l3.ps_id = 'C.A21.L3'
c_a21_1_6_l3.ps_id = 'C.A21.L3'
c_a21_1_7_l3.ps_id = 'C.A21.L3'
c_a21_1_8_l3.ps_id = 'C.A21.L3'
c_a21_2_1_l3.ps_id = 'C.A21.L3'
c_a21_2_2_l3.ps_id = 'C.A21.L3'
c_a21_2_3_l3.ps_id = 'C.A21.L3'
c_a21_2_4_l3.ps_id = 'C.A21.L3'
c_a21_2_5_l3.ps_id = 'C.A21.L3'
c_a21_2_6_l3.ps_id = 'C.A21.L3'
c_a21_2_7_l3.ps_id = 'C.A21.L3'
c_a21_2_8_l3.ps_id = 'C.A21.L3'
c_a21_3_1_l3.ps_id = 'C.A21.L3'
c_a21_3_2_l3.ps_id = 'C.A21.L3'
c_a21_3_3_l3.ps_id = 'C.A21.L3'
c_a21_3_4_l3.ps_id = 'C.A21.L3'
c_a21_3_5_l3.ps_id = 'C.A21.L3'
c_a21_3_6_l3.ps_id = 'C.A21.L3'
c_a21_3_7_l3.ps_id = 'C.A21.L3'
c_a21_3_8_l3.ps_id = 'C.A21.L3'
c_a21_4_1_l3.ps_id = 'C.A21.L3'
c_a21_4_2_l3.ps_id = 'C.A21.L3'
c_a21_4_3_l3.ps_id = 'C.A21.L3'
c_a21_4_4_l3.ps_id = 'C.A21.L3'
c_a21_4_5_l3.ps_id = 'C.A21.L3'
c_a21_4_6_l3.ps_id = 'C.A21.L3'
c_a21_4_7_l3.ps_id = 'C.A21.L3'
c_a21_4_8_l3.ps_id = 'C.A21.L3'
c_a22_1_1_l3.ps_id = 'C.A22.L3'
c_a22_1_2_l3.ps_id = 'C.A22.L3'
c_a22_1_3_l3.ps_id = 'C.A22.L3'
c_a22_1_4_l3.ps_id = 'C.A22.L3'
c_a22_1_5_l3.ps_id = 'C.A22.L3'
c_a22_1_6_l3.ps_id = 'C.A22.L3'
c_a22_1_7_l3.ps_id = 'C.A22.L3'
c_a22_1_8_l3.ps_id = 'C.A22.L3'
c_a22_2_1_l3.ps_id = 'C.A22.L3'
c_a22_2_2_l3.ps_id = 'C.A22.L3'
c_a22_2_3_l3.ps_id = 'C.A22.L3'
c_a22_2_4_l3.ps_id = 'C.A22.L3'
c_a22_2_5_l3.ps_id = 'C.A22.L3'
c_a22_2_6_l3.ps_id = 'C.A22.L3'
c_a22_2_7_l3.ps_id = 'C.A22.L3'
c_a22_2_8_l3.ps_id = 'C.A22.L3'
c_a22_3_1_l3.ps_id = 'C.A22.L3'
c_a22_3_2_l3.ps_id = 'C.A22.L3'
c_a22_3_3_l3.ps_id = 'C.A22.L3'
c_a22_3_4_l3.ps_id = 'C.A22.L3'
c_a22_3_5_l3.ps_id = 'C.A22.L3'
c_a22_3_6_l3.ps_id = 'C.A22.L3'
c_a22_3_7_l3.ps_id = 'C.A22.L3'
c_a22_3_8_l3.ps_id = 'C.A22.L3'
c_a22_4_1_l3.ps_id = 'C.A22.L3'
c_a22_4_2_l3.ps_id = 'C.A22.L3'
c_a22_4_3_l3.ps_id = 'C.A22.L3'
c_a22_4_4_l3.ps_id = 'C.A22.L3'
c_a22_4_5_l3.ps_id = 'C.A22.L3'
c_a22_4_6_l3.ps_id = 'C.A22.L3'
c_a22_4_7_l3.ps_id = 'C.A22.L3'
c_a22_4_8_l3.ps_id = 'C.A22.L3'
c_a23_1_1_l3.ps_id = 'C.A23.L3'
c_a23_1_2_l3.ps_id = 'C.A23.L3'
c_a23_1_3_l3.ps_id = 'C.A23.L3'
c_a23_1_4_l3.ps_id = 'C.A23.L3'
c_a23_1_5_l3.ps_id = 'C.A23.L3'
c_a23_1_6_l3.ps_id = 'C.A23.L3'
c_a23_1_7_l3.ps_id = 'C.A23.L3'
c_a23_1_8_l3.ps_id = 'C.A23.L3'
c_a23_2_1_l3.ps_id = 'C.A23.L3'
c_a23_2_2_l3.ps_id = 'C.A23.L3'
c_a23_2_3_l3.ps_id = 'C.A23.L3'
c_a23_2_4_l3.ps_id = 'C.A23.L3'
c_a23_2_5_l3.ps_id = 'C.A23.L3'
c_a23_2_6_l3.ps_id = 'C.A23.L3'
c_a23_2_7_l3.ps_id = 'C.A23.L3'
c_a23_2_8_l3.ps_id = 'C.A23.L3'
c_a23_3_1_l3.ps_id = 'C.A23.L3'
c_a23_3_2_l3.ps_id = 'C.A23.L3'
c_a23_3_3_l3.ps_id = 'C.A23.L3'
c_a23_3_4_l3.ps_id = 'C.A23.L3'
c_a23_3_5_l3.ps_id = 'C.A23.L3'
c_a23_3_6_l3.ps_id = 'C.A23.L3'
c_a23_3_7_l3.ps_id = 'C.A23.L3'
c_a23_3_8_l3.ps_id = 'C.A23.L3'
c_a23_4_1_l3.ps_id = 'C.A23.L3'
c_a23_4_2_l3.ps_id = 'C.A23.L3'
c_a23_4_3_l3.ps_id = 'C.A23.L3'
c_a23_4_4_l3.ps_id = 'C.A23.L3'
c_a23_4_5_l3.ps_id = 'C.A23.L3'
c_a23_4_6_l3.ps_id = 'C.A23.L3'
c_a23_4_7_l3.ps_id = 'C.A23.L3'
c_a23_4_8_l3.ps_id = 'C.A23.L3'
c_a24_1_1_l3.ps_id = 'C.A24.L3'
c_a24_1_2_l3.ps_id = 'C.A24.L3'
c_a24_1_3_l3.ps_id = 'C.A24.L3'
c_a24_1_4_l3.ps_id = 'C.A24.L3'
c_a24_1_5_l3.ps_id = 'C.A24.L3'
c_a24_1_6_l3.ps_id = 'C.A24.L3'
c_a24_1_7_l3.ps_id = 'C.A24.L3'
c_a24_1_8_l3.ps_id = 'C.A24.L3'
c_a24_2_1_l3.ps_id = 'C.A24.L3'
c_a24_2_2_l3.ps_id = 'C.A24.L3'
c_a24_2_3_l3.ps_id = 'C.A24.L3'
c_a24_2_4_l3.ps_id = 'C.A24.L3'
c_a24_2_5_l3.ps_id = 'C.A24.L3'
c_a24_2_6_l3.ps_id = 'C.A24.L3'
c_a24_2_7_l3.ps_id = 'C.A24.L3'
c_a24_2_8_l3.ps_id = 'C.A24.L3'
c_a24_3_1_l3.ps_id = 'C.A24.L3'
c_a24_3_2_l3.ps_id = 'C.A24.L3'
c_a24_3_3_l3.ps_id = 'C.A24.L3'
c_a24_3_4_l3.ps_id = 'C.A24.L3'
c_a24_3_5_l3.ps_id = 'C.A24.L3'
c_a24_3_6_l3.ps_id = 'C.A24.L3'
c_a24_3_7_l3.ps_id = 'C.A24.L3'
c_a24_3_8_l3.ps_id = 'C.A24.L3'
c_a24_4_1_l3.ps_id = 'C.A24.L3'
c_a24_4_2_l3.ps_id = 'C.A24.L3'
c_a24_4_3_l3.ps_id = 'C.A24.L3'
c_a24_4_4_l3.ps_id = 'C.A24.L3'
c_a24_4_5_l3.ps_id = 'C.A24.L3'
c_a24_4_6_l3.ps_id = 'C.A24.L3'
c_a24_4_7_l3.ps_id = 'C.A24.L3'
c_a24_4_8_l3.ps_id = 'C.A24.L3'
c_a25_1_1_l3.ps_id = 'C.A25.L3'
c_a25_1_2_l3.ps_id = 'C.A25.L3'
c_a25_1_3_l3.ps_id = 'C.A25.L3'
c_a25_1_4_l3.ps_id = 'C.A25.L3'
c_a25_1_5_l3.ps_id = 'C.A25.L3'
c_a25_1_6_l3.ps_id = 'C.A25.L3'
c_a25_1_7_l3.ps_id = 'C.A25.L3'
c_a25_1_8_l3.ps_id = 'C.A25.L3'
c_a25_2_1_l3.ps_id = 'C.A25.L3'
c_a25_2_2_l3.ps_id = 'C.A25.L3'
c_a25_2_3_l3.ps_id = 'C.A25.L3'
c_a25_2_4_l3.ps_id = 'C.A25.L3'
c_a25_2_5_l3.ps_id = 'C.A25.L3'
c_a25_2_6_l3.ps_id = 'C.A25.L3'
c_a25_2_7_l3.ps_id = 'C.A25.L3'
c_a25_2_8_l3.ps_id = 'C.A25.L3'
c_a25_3_1_l3.ps_id = 'C.A25.L3'
c_a25_3_2_l3.ps_id = 'C.A25.L3'
c_a25_3_3_l3.ps_id = 'C.A25.L3'
c_a25_3_4_l3.ps_id = 'C.A25.L3'
c_a25_3_5_l3.ps_id = 'C.A25.L3'
c_a25_3_6_l3.ps_id = 'C.A25.L3'
c_a25_3_7_l3.ps_id = 'C.A25.L3'
c_a25_3_8_l3.ps_id = 'C.A25.L3'
c_a25_4_1_l3.ps_id = 'C.A25.L3'
c_a25_4_2_l3.ps_id = 'C.A25.L3'
c_a25_4_3_l3.ps_id = 'C.A25.L3'
c_a25_4_4_l3.ps_id = 'C.A25.L3'
c_a25_4_5_l3.ps_id = 'C.A25.L3'
c_a25_4_6_l3.ps_id = 'C.A25.L3'
c_a25_4_7_l3.ps_id = 'C.A25.L3'
c_a25_4_8_l3.ps_id = 'C.A25.L3'

#  
