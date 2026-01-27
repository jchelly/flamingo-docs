Snapshot directory layout
=========================

The layout of the snapshot files for each simulation is shown in the
diagram below. Each simulation has a ``snapshots`` directory with one
``flamingo_XXXX`` subdirectory for each output time, where ``XXXX`` is
the snapshot number. See :doc:`snapshot_redshifts` for the relation
between snapshot number and redshift.

.. tip:: The easiest way to access particle data is to use swiftsimio
         to read the :ref:`virtual-snapshot` so that you don't need to
         concatenate data from multiple files and unit metadata is
         read automatically. TODO: write and link to examples!

.. mermaid::

   flowchart LR
     snapshots["snapshots/"]

     snapshots --> s0000["`**Snapshot 0**
     flamingo_0000/`"]
     snapshots --> s0001["`**Snapshot 1**
     flamingo_0001/`"]

     s0000 --> s0000_virtual["`**Virtual snapshot**
     flamingo_0000.hdf5`"]
     s0000 --> s0000_chunks["`**Snapshot chunks**
     flamingo_0000.0.hdf5
     flamingo_0000.1.hdf5
     flamingo_0000.2.hdf5
     ...`"]

     s0001 --> s0001_f0["..."]

As an example, see `/FLAMINGO/L1_m9/L1_m9/snapshots/
</flamingo/viewer.html?path=/FLAMINGO/L1_m9/L1_m9/snapshots>`__ for
the ``L1_m9`` snapshot data.

.. _virtual-snapshot:

Virtual snapshot file
---------------------

Each snapshot directory contains a "virtual" snapshot file which has a
name of the form ``flamingo_XXXX.hdf5``. This file contains HDF5
virtual datasets which refer to particle data distributed over a
number of additional HDF5 files in the same directory. This file can
be treated as a single, large snapshot file which contains all of the
particles.

Snapshot data files
-------------------

The virtual snapshot file does not contain any particle data
itself. The particles in each snapshot are split across multiple HDF5
files with names of the form ``flamingo_XXXX.Y.hdf5``, where ``XXXX``
is the snapshot number and ``Y`` numbers the files that make up the
snapshot. Each one of these files contains the particles in part of
the simulation volume. To read all of the particles in the snapshot it
is necessary to read from all of the files.

If you download the virtual snapshot file it will only be readable if
you also download the snapshot data files to the same directory. The
easiest way to ensure this is to use the full directory download link
for the snapshot you're interested in. See
:doc:`/service_docs/web_interface` for details.

.. warning:: If HDF5 can't find the data for a virtual dataset it
   silently returns incorrect "fill" values! So if you download a
   virtual snapshot and get strange results it may be that HDF5 isn't
   finding the real data files.

If you use the hdfstream module to read from a virtual snapshot the
server automatically reads the underlying datasets in the real
snapshot files.
