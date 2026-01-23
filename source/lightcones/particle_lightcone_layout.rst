Particle lightcone directory layout
===================================

Each FLAMINGO simulation has a directory ``particle_lightcones`` which
contains the particle lightcone data. Several observers were placed in
each simulation and so there is a separate subdirectory
``lightconeX_particles`` containing the lightcone particle data for
each observer ``X``.

The particles for each observer are distributed over a set of files
``lightconeX_0000.Y.hdf5``, where the integer ``Y`` numbers the files
within the set.

For example, the lightcone particle data for the fiducial ``L1_m9``
model can be viewed in the file browser at
`/FLAMINGO/L1_m9/L1_m9/particle_lightcones/
</flamingo/viewer.html?path=/FLAMINGO/L1_m9/L1_m9/particle_lightcones>`__.
