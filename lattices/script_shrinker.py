"""
S.Tomin, March, 2018
"""
from ocelot.cpbd.magnetic_lattice import *
from ocelot import *
from ocelot.gui.accelerator import *

from phase_advance_5pi_sase2 import t4 as section

filename = "./mux_5pi_sase2/t4.py"

lat = MagneticLattice(section.cell)
tws1 = twiss(lat, tws0=section.tws)
#plot_opt_func(lat, tws1)
#print(tws[-1])
#plt.show()

print("length before = ", len(section.cell))
cell = exclude_zero_length_element(section.cell, elem_type=[UnknownElement, Marker], except_elems=[section.ensub_2583_t4])
cell = merge_drifts(cell)
print("length after = ", len(cell))


lat = MagneticLattice(cell)
tws = twiss(lat, tws0=section.tws)
plot_opt_func(lat, tws)
print("d_beta_x = ", tws[-1].beta_x - tws1[-1].beta_x)
print("d_beta_y = ", tws[-1].beta_y - tws1[-1].beta_y)
print("d_alpha_x = ", tws[-1].alpha_x - tws1[-1].alpha_x)
print("d_alpha_y = ", tws[-1].alpha_y - tws1[-1].alpha_y)
print("d_Dx = ", tws[-1].Dx - tws1[-1].Dx)
print("d_Dy = ", tws[-1].Dy - tws1[-1].Dy)
print(tws[-1])
plt.show()

#lat_new = shrinker(lat, remaining_types=[Monitor, SBend, Bend, RBend, Cavity, Quadrupole, Undulator, Hcor, Vcor], init_energy=tws.E)

#tws = twiss(lat_new, tws0=tws)
#plot_opt_func(lat_new, tws)
#plt.show()

write_lattice(lat, file_name=filename, power_supply=True)