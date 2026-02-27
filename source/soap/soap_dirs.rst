Halo catalogue directory layout
===============================

SOAP catalogues
---------------

Each simulation has a ``SOAP-HBT`` directory with one
``halo_properties_XXXX.hdf5`` file for each output time, where ``XXXX`` is
the snapshot number. See :doc:`../snapshots/snapshot_redshifts` for the relation
between snapshot number and redshift.

.. tip:: The easiest way to read the SOAP catalogues is to use swiftsimio
         so that unit metadata is read automatically.
         TODO: write and link to examples!

As an example, see `/FLAMINGO/L1_m9/L1_m9/SOAP-HBT/
</flamingo/viewer.html?path=/FLAMINGO/L1_m9/L1_m9/SOAP-HBT>`__ for
the ``L1_m9`` SOAP catalogues.

HBT-HERONS catalgoues
---------------------

# TODO: Are we serving the HBT files?
# TODO: If so then do we want sorted HBT files?

Each simulation has an ``HBT-HERONS`` directory with one
``XXX`` subdirectory for each output time, where ``XXX`` is
the snapshot number.

Documentation for the HBT-HERONS files can be found at the
`HBT-HERONS webstie
<https://hbt-herons.strw.leidenuniv.nl/>`__

As an example, see `/FLAMINGO/L1_m9/L1_m9/HBT-HERONS/
</flamingo/viewer.html?path=/FLAMINGO/L1_m9/L1_m9/HBT-HERONS>`__ for
the ``L1_m9`` HBT-HERONS catalogues.

