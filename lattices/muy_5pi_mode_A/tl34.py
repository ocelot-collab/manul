from ocelot import * 
tws = Twiss()
#tws.beta_x  = 42.548281572
#tws.beta_y  = 11.0277770725
#tws.alpha_x = -2.18143348313
#tws.alpha_y = 0.703868806111
#tws.E       = 17.4999999889

tws.beta_x  = 42.5926362197
tws.beta_y  = 10.9082466875
tws.alpha_x = -2.15596779978
tws.alpha_y = 0.701693329439
tws.E = 14
#tws_sase1.s        = 1957.1856390000232
# drifts 
d_1 = Drift(l=1.472401, eid='D_1')
d_2 = Drift(l=13.047401, eid='D_2')
d_3 = Drift(l=1.15895, eid='D_3')
d_4 = Drift(l=0.15395, eid='D_4')
d_5 = Drift(l=6.505, eid='D_5')
d_6 = Drift(l=6.5, eid='D_6')
d_7 = Drift(l=0.4457, eid='D_7')
d_8 = Drift(l=0.1543, eid='D_8')
d_9 = Drift(l=0.208951, eid='D_9')
d_10 = Drift(l=0.153951, eid='D_10')
d_11 = Drift(l=0.2, eid='D_11')
d_12 = Drift(l=7.7847, eid='D_12')
d_13 = Drift(l=0.1, eid='D_13')
d_14 = Drift(l=1.4347, eid='D_14')
d_16 = Drift(l=1.86072, eid='D_16')

# quadrupoles 
qk_1982_tl = Quadrupole(l=1.0552, k1=0.0903596001, tilt=0.0, eid='QK.1982.TL')
qf_1997_tl = Quadrupole(l=0.5321, k1=-0.1791908476, tilt=0.0, eid='QF.1997.TL')
qf_2012_tl = Quadrupole(l=0.5321, k1=0.1791908476, tilt=0.0, eid='QF.2012.TL')

# bending magnets 

# correctors 
chy_1997_tl = Vcor(l=0.2, angle=0.0, eid='CHY.1997.TL')
chy_2004_tl = Vcor(l=0.2, angle=0.0, eid='CHY.2004.TL')
cfy_2010_tl = Vcor(l=0.1, angle=0.0, eid='CFY.2010.TL')
chx_2012_tl = Hcor(l=0.2, angle=0.0, eid='CHX.2012.TL')
chy_2012_tl = Vcor(l=0.2, angle=0.0, eid='CHY.2012.TL')
cnx_2021_tl = Hcor(l=0.3, angle=0.0, eid='CNX.2021.TL')
cny_2021_tl = Vcor(l=0.3, angle=0.0, eid='CNY.2021.TL')

# markers 
stsub_1980_tl = Marker(eid='STSUB.1980.TL')
ensub_1997_tl = Marker(eid='ENSUB.1997.TL')
stsub_1997_tl = Marker(eid='STSUB.1997.TL')
tora_2011_tl = Marker(eid='TORA.2011.TL')
otre_2023_tl = Marker(eid='OTRE.2023.TL')
ensub_2025_tl = Marker(eid='ENSUB.2025.TL')
stsub_2025_tl = Marker(eid='STSUB.2025.TL')

# monitor 
bpma_1995_tl = Monitor(eid='BPMA.1995.TL')
bpma_2011_tl = Monitor(eid='BPMA.2011.TL')
bpmd_2022_tl = Monitor(eid='BPMD.2022.TL')

# sextupoles 

# octupole 

# undulator 

# cavity 

# UnknowElement 

# Matrices 

# Solenoids 

# lattice 
cell = (stsub_1980_tl, d_1, qk_1982_tl, d_2, bpma_1995_tl, d_3, qf_1997_tl, 
d_4, chy_1997_tl, ensub_1997_tl, stsub_1997_tl, d_5, chy_2004_tl, d_6, cfy_2010_tl, 
d_7, tora_2011_tl, d_8, bpma_2011_tl, d_9, qf_2012_tl, d_10, chx_2012_tl, 
d_11, chy_2012_tl, d_12, cnx_2021_tl, d_13, cny_2021_tl, d_14, bpmd_2022_tl, 
d_11, otre_2023_tl, d_16, ensub_2025_tl, stsub_2025_tl)
# power supplies 

#  
qk_1982_tl.ps_id = 'QK.1.TL'
qf_1997_tl.ps_id = 'QF.2.TL'
qf_2012_tl.ps_id = 'QF.1.TL'

#  

#  

#  

#  
