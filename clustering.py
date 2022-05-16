from __future__ import print_function
import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
import pytraj as pt
import scipy
import scipy.cluster.hierarchy
import matplotlib.pyplot as plt

traj = pt.iterload('react_kuma1.dcd', 'KUMA1_wat.prmtop')
print(traj)
#output: pytraj.TrajectoryIterator, 35 frames: 
# Size: 0.083185 (GB)
# <Topology: 106333 atoms, 34160 residues, 33806 mols, PBC with box type = orthorhombic>

# calculate pairwise rmsd with `autoimage=True`
# generally we only need to cluster a subset of atoms.
# cluster for 'CA' atoms

distances = pt.pairwise_rmsd(traj(autoimage=True), mask='@CA')
print(distances)
print(type(distances))
print(distances.shape)
# use `scipy` to perform clustering
linkage = scipy.cluster.hierarchy.ward(distances)

scipy.cluster.hierarchy.dendrogram(linkage, no_labels=True, count_sort='descendent')
print(linkage)
#plt.show()
plt.savefig("cluster_kuma1_wat_truncated")
#/home/mateoc/miniconda3/envs/amber/lib/python3.9/site-packages/scipy/cluster/hierarchy.py:834:
# ClusterWarning: scipy.cluster: The symmetric non-negative hollow observation matrix looks suspiciously like an uncondensed distance matrix

#m'hauria de surtir una imatge que no puc veure

# cluster for all atoms but H

# distances = pt.pairwise_rmsd(traj(autoimage=True), mask='!@H=')
# linkage = scipy.cluster.hierarchy.ward(distances)
# scipy.cluster.hierarchy.dendrogram(linkage, no_labels=True, count_sort='descendent')
# None
