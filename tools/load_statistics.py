import numpy as np
import os
import matplotlib.pyplot as plt

def rolling_mean(x, N):
    cumsum = np.cumsum(np.insert(x, 0, 0))
    return (cumsum[N:] - cumsum[:-N]) / float(N)

def rolling_window(a, window):
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)

files = []
for file in os.listdir("."):
    if file.endswith(".npz") and "screen" in file:
        files.append(file)

files.sort()


def load_data(filename):
    table = {}
    with np.load(filename) as data:
        for key in data.keys():
            table[key] = data[key]
    return table

print("files: ", files)

Table = load_data(files[0])
print("keys: ", Table.keys())
print(files[0], len(Table["orbit_x"]))
for file in files[1:]:
    data = load_data(file)
    print(file, len(data["orbit_x"]))
    for key in data.keys():
        Table[key] = np.append(Table[key], data[key])

#a = load_particle_array("data_10Hz_123.npz")
print(len(Table["orbit_x"]))

orbit_x = Table["orbit_x"]
orbit_y = Table["orbit_y"]

fb_status = Table['fb_status']
pointing = Table['pointing']

print(np.shape(pointing), np.shape(fb_status))

x_15 = orbit_x[15::37]
x15_mean = rolling_mean(x_15, 500)
x15_std = np.std(rolling_window(x_15, 500), 1)
#plt.plot(pointing[1::5], 'r.')
plt.plot(fb_status, 'r.', alpha=0.1)
plt.plot(x15_mean, 'b.')
plt.plot(x15_std, 'k.')
plt.show()