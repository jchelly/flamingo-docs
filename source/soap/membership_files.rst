Group membership files
----------------------

Before SOAP can be run we generate a set of files which contain halo
membership information for each particle in the SWIFT snapshot. The
datasets in these files are stored in the same order and with the same
partitioning between files as the datasets in the snapshots. This allows
SOAP to read halo membership information for sub-regions of the
simulation volume without reading the full halo-finder output. These
files may also be useful for visualising the input halo catalogue.

The group membership files are HDF5 files with one group for each
particle type, named PartType0, PartType1, ... as in the snapshots. Each
group contains the following datasets:

#. ``GroupNr_bound``: for each particle in the corresponding snapshot
   file this contains the array index of the subhalo which the particle
   is bound to. If a particle is not bound to any subhalo it will have
   ``GroupNr_bound``\ =-1.

#. ``Rank_bound``: the ranking by total energy of this particle within
   the subhalo it belongs to, or -1 if the particle is not bound to any
   subhalo. The particle with the most negative total energy has
   ``Rank_bound``\ =0.

#. ``GroupNr_all``: (VELOCIraptor only) for each particle in the
   corresponding snapshot file this contains the array index of the VR
   group which the particle belongs to, regardless of whether it is
   bound or unbound. Particles in no group have ``GroupNr_all``\ =-1.

#. ``FOFGroupIDs``: the 3D FOF group the particle is part of. This field
   is only present if a FOF snapshot is listed in the parameter file.
   This field is present in the snapshots themselves, but for FLAMINGO
   hydro simulations the FOF was regenerated. If this field is present
   it will overwrite the value from the snapshots when SOAP is run.

The GroupNr values stored here are zero based array indexes into the
full subhalo catalogue, and not the subhalos IDs. For example the first
group in the VELOCIraptor catalogue has GroupNr=0 and ID=1.

The script ‘make_virtual_snapshot.py‘ will combine snapshot and group
membership files into a single virtual snapshot file. This virtual file
can be read by swiftsimio and gadgetviewer to provide halo membership
information alongside other particle properties. Using the virtual file
along with the spatial masking functionality within swiftsimio means it
is possible to quickly load all the particles bound to a given subhalo.

.. |image| image:: images/image7.png
.. |image1| image:: images/image4.png
