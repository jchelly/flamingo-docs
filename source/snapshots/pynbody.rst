Reading snapshots with pynbody
==============================

The `pynbody <https://pynbody.readthedocs.io/latest/#>`__
python module can be used to read snapshots. It can efficiently cut
out regions of interest from the snapshots and handles units and
cosmology metadata. There are two ways to access FLAMINGO data with
pynbody:

  * Download a complete snapshot and have pynbody read it directly
    using `h5py <https://docs.h5py.org/en/stable/>`__
  * Use pynbody to access snapshots stored on `Cosma
    <https://cosma.readthedocs.io/en/latest/>`__ using the `hdfstream
    <https://hdfstream-python.readthedocs.io/en/latest>`__ service

The latter method might be preferable if you only need a small
fraction of the data in a snapshot, such as only certain particle
types or a small region around an object of interest.

The pynbody documentation includes a section on `working with remote
FLAMINGO data
<https://pynbody.readthedocs.io/latest/tutorials/flamingo_halo_particles.html>`__.

Installation
------------

Pynbody can be installed as follows::

  pip install pynbody

For remote access to snapshots we need at least version 2.8.0 of
pynbody and also the hdfstream module::

  pip install hdfstream

For more general information on how to get started with pynbody, see
the `pynbody documentation
<https://pynbody.readthedocs.io/latest/tutorials/quickstart.html>`__.

Opening a snapshot
------------------

The examples below show how to open a local HDF5 which you have
downloaded, and how to open a remote file on the hdfstream server.

.. tab-set::

   .. tab-item:: Opening a remote file

      .. code-block:: python

         # Connect to the hdfstream service and open the root directory
         import hdfstream
         root_dir = hdfstream.open("cosma", "/")

         # Pass the remote directory object when opening the snapshot with pynbody
         import pynbody
         snap = pynbody.load("FLAMINGO/L1_m10/L1_m10/snapshots/flamingo_0077/flamingo_0077.hdf5", remote_dir=root_dir)

   .. tab-item:: Opening a local file

      .. code-block:: python

         # Open a HDF5 snapshot which we have downloaded
         import pynbody
         snap = pynbody.load("./FLAMINGO/L1_m10/L1_m10/snapshots/flamingo_0077/flamingo_0077.hdf5")

Each snapshot consists of a large number of data files and a single
:ref:`virtual snapshot file <virtual-snapshot>`. The full snapshot can
be opened by giving pynbody the name of the virtual snapshot file or
the base name of the individual snapshot files without the ``.X.hdf5``
suffix.

Snapshot metadata
-----------------

Whether you opened a local or remote snapshot, the ``snap`` object
returned by ``pynbody.load()`` can be used to access simulation
metadata. Basic information about the snapshot is stored in the
``snap.properties`` dict::

  >>> snap.properties
  {'a': np.float64(1.0),
  'h': np.float64(0.681),
  'omegaM0': np.float64(0.30461099999999997),
  'omegaL0': np.float64(0.693922),
  'omegaB0': np.float64(0.0486),
  'omegaC0': np.float64(0.256011),
  'omegaNu0': np.float64(0.0013890794316214667),
  'boxsize': Unit("3.09e+27 a cm"),
  'time': Unit("4.34e+17 s")}

The ``families()`` method can be used to see what particle types exist
in this snapshot::

  >>> snap.families()
  [<Family gas>, <Family dm>, <Family star>, <Family bh>]

To determine the number of particles of each type we can check the
length of each family. To get the number of dark matter particles, for
example::

  >>> len(snap.dm)
  729000000

Each particle type family has a ``loadable_keys()`` method which
returns the names of particle properties which can be loaded::

  >>> snap.dm.loadable_keys()
  ['vel',
   'grp',
   'iord',
   'HaloCatalogueIndex',
   'mass',
   'GroupNr_bound',
   'pos',
   'Rank_bound',
   'phi',
   'eps']

Reading particle data
---------------------

Particle properties, such as position, mass or velocity, are read in
or downloaded when you try to access them. To read the coordinates of
all star particles in the simulation, for example::

  star_pos = snap.star["pos"]

If you opened a remote snapshot, this will trigger a download and a
progress bar will appear. The result is a pynbody `SimArray
<https://pynbody.readthedocs.io/latest/reference/_autosummary/pynbody.array.SimArray.html#pynbody.array.SimArray>`__,
which wraps a numpy ndarray with extra metadata such as unit
information.

In this example, the SimArray records that the particle positions
are in comoving Mpc::

  >>> star_pos
  SimArray([[649.22656783, 524.32466783, 595.55844783],
           [649.48269783, 524.27156783, 595.70102783],
           [649.51910783, 524.65127783, 595.67997783],
           ...,
           [987.07861218, 995.73119218,  88.40002218],
           [987.07806218, 995.72685218,  88.39880218],
           [987.07910218, 995.73126218,  88.39935218]], shape=(42070680, 3), '3.09e+24 cm a')

.. _pynbody_cutouts:

Cutting out a region
--------------------

The particles in Swift snapshots are ordered in a way that allows us
to read regions from a snapshot without reading the entire file. Given
a range of coordinates in x, y, and z, pynbody can compute which
parts of the file to read or download to find the corresponding
particles.

This feature can be used to read in just part of a local snapshot
which you have downloaded, or to download just part of a remote
snapshot on the server. Note that this is likely to return additional
particles outside the requested region because the snapshot volume is
divided into cells and all cells which overlap the region are read in
full.

.. tab-set::

   .. tab-item:: Using a remote file

      .. code-block:: python

         # Connect to the hdfstream service and open the root directory
         import hdfstream
         root_dir = hdfstream.open("cosma", "/")

         # Define a spherical region to read in
         region = pynbody.filt.Sphere("25 Mpc a", [125, 125, 125])

         # Pass the remote directory object and region to read when opening the snapshot with pynbody
         import pynbody
         snap = pynbody.load("FLAMINGO/L1_m10/L1_m10/snapshots/flamingo_0077/flamingo_0077.hdf5",
                             take_region=region, remote_dir=root_dir)

         # Download the coordinates of gas particles in the region
         gas_pos = snap.gas["pos"]

   .. tab-item:: Using a local file

      .. code-block:: python

         # Define a spherical region to read in
         region = pynbody.filt.Sphere("25 Mpc a", [125, 125, 125])

         # Pass the region to read when opening the snapshot with pynbody
         import pynbody
         snap = pynbody.load("FLAMINGO/L1_m10/L1_m10/snapshots/flamingo_0077/flamingo_0077.hdf5",
                             take_region=region)

         # Read the coordinates of gas particles in the region
         gas_pos = snap.gas["pos"]
