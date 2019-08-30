from ocelot import *
from ocelot.gui.accelerator import *
import i1
import l1_full
import l2_full
import l3_full
import cl_full
import sase1
import b2d
import sase3
import t4
import t4d
#from ocelot.test.xfel_lat.I1 import *
import numpy as np
from copy import deepcopy

c_lat = t4

#undu_49_i1.lperiod = 0.074
#undu_49_i1.nperiods = 10
#undu_49_i1.Kx = 1.935248
#undu_49_i1.l = 0.74
# Undulator(lperiod=0.074, nperiods=10, Kx=1.935248*2, Ky=0.0, eid='UNDU.49.I1')
lat = MagneticLattice( c_lat.cell )# + l1.cell + l2.cell + b2d.cell) #+cell_l1 + cell_l2 + cell_l3)

#lat.update_transfer_maps()
for elem in lat.sequence:
    if elem.__class__ == Undulator:
        print(elem.Kx)
        print(elem.transfer_map.R(0.130))


tws = twiss(lat, c_lat.tws)
print(tws[-1])
#plt.figure(1)
plot_opt_func(lat, tws, top_plot=["Dx", "Dy"])
plt.show()


f = open("design_t4d_2018_07_12_SA3_15m.txt")
params = {}
for line in f:
    li=line.strip()
    if not li.startswith("#") and not("TWISS" in line):
        parts = line.rstrip().split()
        indx = parts.index("#") if "#" in parts else -1
        parts = parts[:indx]
        if len(parts) >= 2 and not("=" in parts):
            #print(parts)
            params[parts[0]] = [float(p) for p in parts[1:]]
        #print(parts)
    #print(line)
marker_imp = ["OTR", "TORA", 'ENGRD.419.B2', 'MPBPMI.1693.CL', 'BPMR.1307.L3', 'STSUB.2583.T4']
L = 0
elems = []
for elem in lat.sequence:
    L += elem.l
    if elem.__class__ == Drift:
        continue
    if elem.__class__ == Marker and len([mark for mark in marker_imp if mark in elem.id]) == 0 and elem not in [lat.sequence[0], lat.sequence[-1]] :
        continue
    elems.append([elem, L-elem.l/2.])
    if "ps_id" in dir(elem):

        if elem.__class__ == Quadrupole:
            param = params[elem.ps_id]
            if np.sign(elem.k1) != np.sign(param[0]):
                print("polyarity", elem.id, param[0], elem.k1)
            elem.k1 = np.abs(param[0])*np.sign(elem.k1)/elem.l
            #elem.k1 = np.abs(param[1])*np.sign(elem.k1)
            #elem.l = param[2]

            #if elem.id in ['Q.37.I1', 'Q.38.I1']:
            #
        elif elem.__class__ in [SBend, Bend, RBend] and "BB" in elem.ps_id:
            #pass
            param = params[elem.ps_id]
            #print("BEND = ", elem.ps_id, param, elem.__class__.__name__, elem.id)
            elem.angle = np.abs(param[0])*np.sign(elem.angle)
            elem.e1 = np.abs(elem.angle) * np.sign(elem.e1)
            elem.e2 = np.abs(elem.angle) * np.sign(elem.e2)
            elem.l = param[3]
        elif elem.__class__ == Cavity and not (".AH1." in elem.id) and not (".A1." in elem.id) and not  (".L2" in elem.id) and not  (".L3" in elem.id):
            id_parts = elem.id.split(".")
            ps_id = id_parts[0]+ "." + id_parts[1] + "." + id_parts[-1]
            #param = params[ps_id]
            #print(param)
            elem.coupler_kick = True
            elem.vx_up = -56.813 + 10.751j
            elem.vy_up = -41.091 + 0.5739j
            elem.vxx_up = 0.99943 - 0.81401j
            elem.vxy_up = 3.4065 - 0.4146j
            elem.vx_down = -24.014 + 12.492j
            elem.vy_down = 36.481 + 7.9888j
            elem.vxx_down = -4.057 - 0.1369j
            elem.vxy_down = 2.9243 - 0.012891j
            #if ".L1" in elem.id:
            #    elem.v =14.6875*0.001

from ocelot.cpbd.magnetic_lattice import lattice_format_converter as lconvector

cell = lconvector(elems)
#for elem in cell:
#    print(elem.id, elem.l)

lat = MagneticLattice(cell)
write_lattice(lat, file_name="t4_new.py", power_supply=True)
#
import t4_new
lat = MagneticLattice(t4_new.cell)
##undu_49_i1.Kx = 0
#lat.update_transfer_maps()

#tws0 = Twiss()
#tws0.E = 0.005000000
#tws0.beta_x = 29.171000000
#tws0.alpha_x = 10.955000000
#tws0.beta_y = 29.171000
#tws0.alpha_y = 10.955000

tws = twiss(lat, c_lat.tws)
print(tws[-1])
#plt.figure(4)
plot_opt_func(lat, tws, top_plot=["E"])
plt.show()




