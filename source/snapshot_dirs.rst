Snapshot directory layout
=========================

The snapshots for each simulation are stored in directories with names
of the form ``snapshots/flamingo_XXXX``, where ``XXXX`` is the snapshot
number. Lower snapshot numbers correspond to higher redshifts.

The particle data for a single snapshot is split across multiple HDF5
files. Each snapshot directory contains a set of files
``flamingo_XXXX.Y.hdf5``, where ``XXXX`` is the snapshot number and
``Y`` numbers the files that make up each snapshot. Each one of these
files contains the particles in part of the simulation volume. To read
all of the particles in the snapshot it is necessary to read all of
the files.

Virtual snapshot files
----------------------

For convenience, each snapshot directory also contains a "virtual"
snapshot file which has a name of the form
``flamingo_XXXX.hdf5``. This file contains HDF5 virtual datasets which
refer to the particle data in the "real" snapshot files. This file can
be treated as a single, large snapshot file which contains all of the
particles.

If you download the virtual snapshot file it will only be readable if
you also download the real snapshot files to the same directory. The
easiest way to ensure this is to use the full directory download link
for the snapshot you're interested in.

.. warning:: If HDF5 can't find the data for a virtual dataset it
   silently returns incorrect "fill" values! So if you download a
   virtual snapshot and get strange results it may be that HDF5 isn't
   finding the real data files.

If you use the hdfstream module to read from a virtual snapshot the
server automatically reads the underlying datasets in the real
snapshot files.

