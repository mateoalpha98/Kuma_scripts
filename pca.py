from __future__ import print_function
import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

#%matplotlib inline

#%config InlineBackend.figure_format = 'retina'  # high resolution
import matplotlib

import pytraj as pt
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')
#from pytraj.plot import show_config  ###it's like this function plot doesn't exist.

# we use `load` method to load all data to memory. This is good for small data size.
# use `pytraj.iterload` for out-of-core traj.

traj = pt.load('react_kuma1.dcd', 'KUMA1_wat.prmtop')
#print(traj)
pca = PCA(n_components=2)

# superpose to 1st frame
a=pt.superpose(traj, ref=0, mask='!@H=')
#print(a)

# create average structure

avg = pt.mean_structure(traj)
print(avg)

# superpose all structures to average frame
b=pt.superpose(traj, ref=avg, mask='!@H=')
#print(b)

# perform PCA calculation and get transformed coords
# we need to reshape 3D traj.xyz array to 2D to make sklearn happy
# make a new traj by stripping all H atoms
traj_new = traj['!@H=']
xyz_2d = traj_new.xyz.reshape(traj_new.n_frames, traj_new.n_atoms * 3)
#print(xyz_2d.shape) # (n_frames, n_dimensions) 35 , 109023
reduced_cartesian = pca.fit_transform(xyz_2d)
#print(reduced_cartesian.shape) # (n_frames, n_dimensions)

# ignore warning
import warnings
warnings.filterwarnings('ignore')

plt.figure()
plt.scatter(reduced_cartesian[:, 0], reduced_cartesian[:,1], marker='o', c=range(traj_new.n_frames), alpha=0.5)
plt.xlabel('PC1')
plt.ylabel('PC2')
cbar = plt.colorbar()
cbar.set_label('frame #')
plt.savefig("pca_de_kuma1_wat_truncada")
plt.show()