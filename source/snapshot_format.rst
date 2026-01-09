Snapshot file format
====================

Here we describe the basic features of FLAMINGO snapshots. For full
details of the SWIFT simulation format, see the `SWIFT documentation
<https://swift.strw.leidenuniv.nl/docs/Snapshots/index.html>`__.

Simulation metadata
-------------------

General information about the snapshot is stored in the form of
attributes attached to HDF5 groups in each snapshot file.

Header
^^^^^^

Snapshots contain a ``Header`` group which contains similar
information to the header in Gadget-2 snapshots. Some of the more
useful attributes are:

+-------------------------+-----------------------------------------------------------------------+
| Attribute name          | Description                                                           |
+=========================+=======================================================================+
| ``Redshift``            | Redshift of this snapshot                                             |
+-------------------------+-----------------------------------------------------------------------+
| ``Scale-factor``        | Expansion factor at this snapshot                                     |
+-------------------------+-----------------------------------------------------------------------+
| ``BoxSize``             | Size of the box in each dimension (FLAMINGO runs are all cubic boxes) |
+-------------------------+-----------------------------------------------------------------------+
| ``NumFilesPerSnapshot`` | Number of files in the snapshot. Always 1 for virtual snapshots.      |
+-------------------------+-----------------------------------------------------------------------+

Cosmology
^^^^^^^^^

The ``Cosmology`` group stores the cosmological parameters used in the
simulation and the redshift of the snapshot output. It includes the
following HDF5 attributes:

+-------------------------+--------------------------------------------------------------------------------------------------------+
| Attribute name          | Description                                                                                            |
+=========================+========================================================================================================+
| ``Redshift``            | Redshift of this snapshot                                                                              |
+-------------------------+--------------------------------------------------------------------------------------------------------+
| ``Scale-factor``        | Expansion factor at this snapshot                                                                      |
+-------------------------+--------------------------------------------------------------------------------------------------------+
| ``Omega_b``             | Baryon density parameter :math:`\Omega_\mathrm{b}` at z=0                                              |
+-------------------------+--------------------------------------------------------------------------------------------------------+
| ``Omega_cdm``           | Cold dark matter density parameter :math:`\Omega_{\mathrm{cdm}}` at z=0                                |
+-------------------------+--------------------------------------------------------------------------------------------------------+
| ``Omega_lambda``        | Dark energy density parameter :math:`\Omega_{\mathrm{\Lambda}}` at z=0                                 |
+-------------------------+--------------------------------------------------------------------------------------------------------+
| ``Omega_m``             | Mass density parameter :math:`\Omega_\mathrm{m} = \Omega_{\mathrm{cdm}} + \Omega_\mathrm{b}` at z=0    |
+-------------------------+--------------------------------------------------------------------------------------------------------+
| ``Omega_nu``            | Neutrino density parameter :math:`\Omega_{\mathrm{\nu}}` at the snapshot redshift                      |
+-------------------------+--------------------------------------------------------------------------------------------------------+
| ``Omega_nu_0``          | Neutrino density parameter :math:`\Omega_{\mathrm{\nu}}` at z=0                                        |
+-------------------------+--------------------------------------------------------------------------------------------------------+
| ``Omega_r``             | Radiation density parameter :math:`\Omega_\mathrm{r}` at z=0                                           |
+-------------------------+--------------------------------------------------------------------------------------------------------+
| ``Omega_k``             | Curvature density parameter :math:`\Omega_\mathrm{k}` at z=0                                           |
+-------------------------+--------------------------------------------------------------------------------------------------------+

.. note:: `swiftsimio
          <https://swiftsimio.readthedocs.io/en/latest/loading_data/index.html>`_
          can create a suitable astropy cosmology object from the
          snapshot metadata. This is the safest way to convert
          redshifts to comoving distances or lookback times, for
          example.

Units
^^^^^

The ``Units`` group describes the system of units used in the
snapshot. It defines basic units of length, mass, time and temperature
in terms of CGS units. Most quantities in the snapshot are expressed
in combinations of these base units. In FLAMINGO, the base units used
are as follows:

+-------------+-------------------------------------------+
| Dimension   | Unit                                      |
+=============+===========================================+
| Length      | :math:`\mathrm{Mpc}`                      |
+-------------+-------------------------------------------+
| Mass        | :math:`10^{10}\mathrm{M}_{\odot}`         |
+-------------+-------------------------------------------+
| Time        | :math:`\mathrm{Mpc} \mathrm{(km/s)}^{-1}` |
+-------------+-------------------------------------------+
| Temperature | :math:`\mathrm{K}`                        |
+-------------+-------------------------------------------+

A few attributes in the snapshot file are expressed in the "internal"
system of units used to run the simulation. This unit system is
described in the ``InternalCodeUnits`` group. In FLAMINGO, the
snapshot and internal unit systems are the same.

The exact units used for each particle property are documented in
:ref:`particle-properties`.

Particle types
--------------

The FLAMINGO simulations contain gas, dark matter, star, black hole
and neutrino particles. There is a HDF5 group for each particle
type. Within these groups particle properties (position, mass,
velocity etc) are stored as HDF5 datasets. The particle type groups
follow Gadget-2's ``PartTypeX`` naming scheme but there are also
symbolic links to the groups with more descriptive names.

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Particle type
     - HDF5 group name
     - Link name
   * - Gas particles
     - ``PartType0``
     - ``GasParticles``
   * - Dark matter particles
     - ``PartType1``
     - ``DMParticles``
   * - Star particles
     - ``PartType4``
     - ``StarsParticles``
   * - Black hole particles
     - ``PartType5``
     - ``BHParticles``
   * - Neutrino particles
     - ``PartType6``
     - ``NeutrinoParticles``

The quantities stored for each particle type are described in :ref:`particle-properties`.

Dataset metadata
----------------

The datasets in the particle type groups have a number of descriptive attributes:

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Attribute name
     - Attribute description
   * - Description
     - A short description of the particle property
