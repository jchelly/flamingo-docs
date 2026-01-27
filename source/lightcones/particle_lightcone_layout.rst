Particle lightcone directory layout
===================================

Each FLAMINGO simulation has a directory ``particle_lightcones`` which
contains the particle lightcone data. Several observers were placed in
each simulation and so there is a separate subdirectory
``lightconeX_particles`` containing the lightcone particle data for
each observer ``X``.

The particles for each observer are distributed over a set of files
``lightconeX_0000.Y.hdf5``, where the integer ``Y`` numbers the files
within the set. This structure is illustrated below.

.. mermaid::

   flowchart LR
     lcp["particle_lightcones/"]

     lcp --> obs0["`**Observer 0**
     lightcone0_particles/`"]
     lcp --> obs1["`**Observer 1**
     lightcone1_particles/`"]

     obs0 --> data0["`**Particle data**
     lightcone0_0000.0.hdf5
     lightcone0_0000.1.hdf5
     lightcone0_0000.2.hdf5
     ...`"]

     obs1 --> data1["`**Particle data**
     lightcone1_0000.0.hdf5
     lightcone1_0000.1.hdf5
     lightcone1_0000.2.hdf5
     ...`"]

As an example, see `/FLAMINGO/L1_m9/L1_m9/particle_lightcones/
</flamingo/viewer.html?path=/FLAMINGO/L1_m9/L1_m9/particle_lightcones>`__
for the ``L1_m9`` particle lightcones.
