Snapshots
=========

FLAMINGO simulation snapshots record the full distribution of
particles in the simulation volume at an instant in time. The dark
matter only runs contain dark matter and neutrino particles. The hydro
runs also include gas, star and black hole particles.

For more details of the SWIFT simulation snapshot format, see the
`SWIFT documentation
<https://swift.strw.leidenuniv.nl/docs/Snapshots/index.html>`__.

File and directory layout
-------------------------

The snapshots for each simulation are stored in directories with names
of the form ``snapshots/flamingo_XXXX``, where ``XXXX`` is the snapshot
number. Lower snapshot numbers correspond to higher redshifts.

The particle data for a single snapshot is split across multiple HDF5
files. Each snapshot directory contains a set of files
``flamingo_XXXX.Y.hdf5``, where ``XXXX`` is the snapshot number. Each
one of these files contains the particles in part of the simulation
volume. To read all of the particles in the snapshot it is necessary
to read all of the files.

For convenience, each snapshot directory also contains a "virtual"
snapshot file which has a name of the form
``flamingo_XXXX.hdf5``. This file contains HDF5 virtual datasets which
refer to the particle data in all of the "real" snapshot files. This
file can be treated as a single, large snapshot file which contains
all of the particles.

.. note:: If you download the virtual snapshot file it will only be
   readable if you also download the real snapshot files to the same
   directory. The easiest way to ensure this is to use the full
   directory download link for the snapshot you're interested in.
   
Snapshot redshifts
------------------

The FLAMINGO simulations were run with 78 or 79 output snapshot
redshifts, depending on the model. SOAP halo catalogues exist for all
of these redshifts but full particle data is only available for a
subset.

===============  ========  =============  ===============
Snapshot number  Redshift  Particle data  Halo catalogues
===============  ========  =============  ===============
0                15.0      Y              Y
1                ?         N              Y
...              ...       ...            ...
===============  ========  =============  ===============

Snapshot file structure
-----------------------

Header and cosmology
^^^^^^^^^^^^^^^^^^^^

Units
^^^^^

Dataset metadata
^^^^^^^^^^^^^^^^

Spatial indexing
^^^^^^^^^^^^^^^^

Particle properties
-------------------

This section lists all of the properties which are stored for each
type of particle.

Dark matter particles
^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^

Star particles
^^^^^^^^^^^^^^

Black hole particles
^^^^^^^^^^^^^^^^^^^^

Neutrino particles
^^^^^^^^^^^^^^^^^^
