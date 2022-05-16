import mdtraj as md
import numpy as np
t = md.load('react_kuma1.dcd', top='KUMA1_wat.prmtop')
print(t)
#fist ten frames:
print(t[1:10])
# or maybe the last frame?
print(t[-1])
#There’s a lot of information in the trajectory object. The most obvious is the Cartesian coordinates. 
# They’re stored as a numpy array under xyz. All of the distances in the Trajectory are stored in nanometers. 
# The time unit is picoseconds. Angles are stored in degrees (not radians).
print(t.xyz.shape)
# result (35, 106333, 3)
print(np.mean(t.xyz))
# r/ 5.1946163

# the simulation time (in picoseconds) of th first 10 frames
print(t.time[0:10])

 # or the unitcell lengths in the last frame? (in nanometers of course)
f=t.unitcell_lengths[-1]
print(f)

#Saving the trajectory back to disk is easy.
t[::2].save('halftraj.h5')

# the format will be parsed based on the extension, or you can call the
# format-specific save methods
t[0:10].save_dcd('first-ten-frames.dcd')


#The trajectory contains a reference to a topology object, which can come in handy. 
#For example, if you want to save a copy of your trajectory with only alpha carbons present, you can do that pretty easily.
atoms_to_keep = [a.index for a in t.topology.atoms if a.name == 'CA']
t.restrict_atoms(atoms_to_keep)  # this acts inplace on the trajectory
t.save('CA-only.h5')