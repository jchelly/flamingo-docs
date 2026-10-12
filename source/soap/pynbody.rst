Reading SOAP halo catalogues with pynbody
=========================================

The `pynbody <https://pynbody.readthedocs.io/latest/#>`__ python
module can be used to read SOAP halo catalogues. It can efficiently
cut out regions of interest and handles units and cosmology
metadata. There are two ways to access FLAMINGO data with pynbody:

  * Download a complete output and have pynbody read it directly
    using `h5py <https://docs.h5py.org/en/stable/>`__
  * Use pynbody to access data stored on `Cosma
    <https://cosma.readthedocs.io/en/latest/>`__ using the `hdfstream
    <https://hdfstream-python.readthedocs.io/en/latest>`__ service

The latter method might be preferable if you only need a small
fraction of the data, such as a subset of halo properties or halos in
a small region of interest.

To read the particles associated with a halo selected from a SOAP
catalogue, see :doc:`/snapshots/halo_particles`.

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

Opening a halo catalogue
------------------------

The examples below show how to open a local HDF5 which you have
downloaded, and how to open a remote file on the hdfstream server.

.. note:: Opening SOAP outputs with pynbody is currently quite slow
          due to the very large number of datasets.

.. tab-set::

   .. tab-item:: Opening a remote file

      .. code-block:: python

         # Connect to the hdfstream service and open the root directory
         import hdfstream
         root_dir = hdfstream.open("cosma", "/")

         # Open the z=0 halo catalogue from the L1_m10 simulation
         import pynbody
         soap = pynbody.load("FLAMINGO/L1_m10/L1_m10/SOAP-HBT/halo_properties_0077.hdf5", remote_dir=root_dir)

   .. tab-item:: Opening a local file

      .. code-block:: python

         # Here we pass the name of the file we downloaded to pynbody
         import pynbody
         soap = pynbody.load("./FLAMINGO/L1_m10/L1_m10/SOAP-HBT/halo_properties_0077.hdf5", remote_dir=root_dir)

Accessing halo properties
-------------------------

SOAP computes halo properties using several different halo
definitions, which are described in :doc:`soap_halo_variations`. For
each halo definition, various quantities are computed. We can see the
full (and rather long) list of available halo properties with::

  >>> soap.halo.loadable_keys()
  ['ExclusiveSphere/500kpc/KappaCorotGas',
   'ProjectedAperture/30kpc/projy/CentreOfMass',
   'SO/2500_crit/NumberOfGasParticles',
   'ExclusiveSphere/3000kpc/NumberOfGasParticles',
   'InclusiveSphere/1000kpc/DiscToTotalStellarMassFraction',
   ...]

These correspond to HDF5 dataset names in the SOAP files. The
available halo properties are fully documented in
:doc:`soap_property_table`.

In this list we can see the centre of mass of the bound particles,
``BoundSubhalo/CentreOfMass``, and the total bound mass of the subhalo,
``BoundSubhalo/TotalMass``. To read in these quantities::

  pos = soap.halo["BoundSubhalo/CentreOfMass"]
  mass = soap.halo["BoundSubhalo/TotalMass"]

Each property is returned as pynbody `SimArray
<https://pynbody.readthedocs.io/latest/reference/_autosummary/pynbody.array.SimArray.html#pynbody.array.SimArray>`__,
which wraps a numpy ndarray with extra metadata such as unit
information.
