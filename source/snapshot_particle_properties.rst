Particle properties
===================

This page documents all of the properties which are stored for each
type of particle in a FLAMINGO snapshot.

Dark matter particles
---------------------

Dark matter particles are stored in the HDF5 group ``/PartType1``,
which is also soft-linked as ``/DMParticles``. This group contains
HDF5 datasets which store the following particle properties:

===============  =========  =========  ======  ===========
Dataset name     Units      Data type  Shape   Description
===============  =========  =========  ======  ===========
Coordinates      cMpc       float64    [N,3]   Comoving positions of the particles
Velocities       km/s       float32    [N,3]   Physical peculiar velocities of the particles
ParticleIDs      -          uint64     [N,]    Unique identifiers for the particles
===============  =========  =========  ======  ===========

Gas particles
-------------

Star particles
--------------

Black hole particles
--------------------

Neutrino particles
------------------
