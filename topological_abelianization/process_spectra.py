import numpy as np
# import mpl_scatter_density
import matplotlib.pyplot as plt
import matplotlib.colors as colors

from input import N
from scipy.interpolate import Rbf

ms = np.load('./spectra/ms.npy')
nm = len(ms)

xs = []
ys = []
zs = []
for i in range(nm):
    fname = './spectra/'+str(i).zfill(5)+'.npy'
    spec = np.load(fname)
    energy = np.linspace(-20,20,len(spec))
    # print(spec)

    for j in range(len(spec)):
        xs.append(ms[i])
        ys.append(energy[j])
        zs.append(spec[j])

z = np.array(zs)
zz = z.reshape((len(ms),len(spec)))

plt.imshow(
        zz.transpose(), 
        extent=(np.amin(ms),np.amax(ms), np.amin(energy), np.amax(energy)), 
        origin='lower', aspect='auto',cmap='Blues', interpolation='spline16', 
        norm=colors.SymLogNorm(
            linthresh=0.01, linscale=0.4, vmin=0, vmax=np.amax(zz), base=10
            )
        ) 
    
plt.colorbar(label='DOS')
ax=plt.gca()
ax.set_ylim((-1.2,1.2))
ax.set_xlabel(r"$m$")
ax.set_ylabel(r"Energy")
plt.tight_layout()
plt.savefig("topo_spectrum.png",dpi=300)
plt.show()

# print('hi')

# x_min, x_max = np.amin(xs), np.amax(xs)
# y_min, y_max = np.amin(ys), np.amax(ys)

# # Make a grid with spacing 0.002.
# grid_x, grid_y = np.mgrid[x_min:x_max:0.1, y_min:y_max:0.1]

# # Make an n-dimensional interpolator.
# rbfi = Rbf(xs, ys, zs, smooth=2)

# # Predict on the regular grid.
# di = rbfi(grid_x, grid_y)

# plt.imshow(di)

# plt.scatter(xs,ys,s=0.1)
# plt.title(f'N={N}')
# ax = plt.gca()
# ax.set_xlim(-5,5)
# ax.set_ylim(-5, 5)
# ax.set_xlabel(r'$m$')
# ax.set_ylabel(r'$\mathrm{Spec}(H)$')
# plt.grid()
# plt.savefig('./topo_spectrum.png', dpi=300)
# plt.show()

# # Make the plot - note that for the projection option to work, the
# # mpl_scatter_density module has to be imported above.

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1, projection='scatter_density')
# ax.scatter_density(xs, ys)
# # ax.set_xlim(-5, 10)
# # ax.set_ylim(-5, 10)
# fig.savefig('gaussian.png')