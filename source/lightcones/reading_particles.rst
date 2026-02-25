Reading lightcone particle data
===============================

The `lightcone_io <https://lightconeio.readthedocs.io/en/stable/>`__
python module can be used to read FLAMINGO lightcone particle outputs,
either by reading downloaded HDF5 files directly or by accessing maps
stored on `Cosma <https://cosma.readthedocs.io/en/latest/>`__ using
the `hdfstream <https://hdfstream-python.readthedocs.io/en/latest>`__
service. The latter method might be better if you're only interested
in certain quantities or regions on the sky.

Installation
------------

The ``lightcone_io`` module can be installed as follows::

  pip install lightcone_io

For remote access to snapshots we also need the hdfstream module::

  pip install hdfstream

Opening the particle data for a lightcone observer
--------------------------------------------------

The examples below show how to open the lightcone particle data output
for observer 0 in the fiducial ``L1_m9`` simulation.

.. tab-set::

   .. tab-item:: Opening remote files

      .. code-block:: python

         # Connect to the hdfstream service and open the root directory
         import hdfstream
         root = hdfstream.open("cosma", "/", user="my_username") # TODO: update when we remove access restrictions

         # Location of one of the lightcone particle files relative to the remote directory
         filename = "FLAMINGO/L1_m9/L1_m9/particle_lightcones/lightcone0_particles/lightcone0_0000.0.hdf5"

         # Open the lightcone particle output
         import lightcone_io as lc
         lightcone = lc.ParticleLightcone(filename, remote_dir=root)

   .. tab-item:: Opening local files

      .. code-block:: python

         # Location of one of the lightcone particle files we downloaded
         filename = "./FLAMINGO/L1_m9/L1_m9/particle_lightcones/lightcone0_particles/lightcone0_0000.0.hdf5"

         # Open the lightcone particle output
         import lightcone_io as lc
         lightcone = lc.ParticleLightcone(filename)

Reading particle information
----------------------------

The commands above return a ``ParticleLightcone`` object which acts
like a dictionary where the particle types are the keys. E.g. to see
which particle types are available::

  print(list(lightcone))

You can use the properties attribute to see what quantities are
available for each particle type. E.g.::

  print(lightcone["Gas"].properties)

The particles in the files are sorted into redshift shells. Within a
shell they are sorted by HEALPix pixel index. If we specify the
redshift range we're interested in and a position on the sky, the
``lightcone_io`` module can locate and read (or download) the
corresponding particles::

  # Quantities we wish to read in
  property_names = ("Coordinates", "ParticleIDs")

  # Line of sight vector specifying the centre of the patch of sky to read in.
  # Here we're looking along the simulation x axis. Set vector=None and
  # radius=None to read the full sky.
  vector = (1., 0., 0.)

  # Angular radius of the patch to read in (10 degrees, here)
  import numpy as np
  radius = np.radians(10.)

  # Redshift range to read in, or None to read all redshifts.
  redshift_range = (0., 1.0)

  # Read or download the dark matter particles
  data = lightcone["DM"].read(property_names, vector, radius, redshift_range)

The result is a dict of `unyt
<https://unyt.readthedocs.io/en/stable/>`__ arrays with the requested
data. In this example we have particle positions and IDs::

  particle_positions = data["Coordinates"]
  particle_ids       = data["ParticleIDs"]
