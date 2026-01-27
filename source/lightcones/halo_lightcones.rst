Halo lightcones
===============

For comparison with observations it is useful to create a "lightcone"
halo catalogue where each halo is seen at the time it crossed the
observer's past lightcone. Ideally this would be done by running a
halo finder on the :doc:`lightcone particle
output</lightcones/particle_lightcones>`, but this was not implemented
in FLAMINGO.

Approximate lightcone halo catalogues can be constructed by running a
halo finder on all of the simulation snapshots and then interpolating
halo positions between snapshots to determine when any periodic copy
of a halo crosses the past lightcone of the observer. The FLAMINGO
simulation snapshots are too widely spaced for accurate interpolation,
but we can use black hole particles from the lightcone particle
outputs as tracers of halo positions.

We divide the redshift range :math:`0 < z < 15` into spherical shells
corresponding to the simulation snapshots. The mid point of each shell
lies at the snapshot redshift and its inner and outer edges lie half
way to the next and previous snapshot redshifts respectively. These
shells are illustrated below.

.. card::
   :img-top: images/lightcone_shells.png

   Redshift shells used in the construction of the lightcone halo
   catalogue for ``L1_m9``. Only low redshifts are shown for clarity.

The halo catalogue for a particular shell is constructed by matching
between two datasets:

  * The HBT-HERONS halo catalogue for the shell's corresponding snapshot
  * The black hole particles in the shell's redshift range in the particle lightcone

For each halo in the snapshot halo catalogue we pick a black hole
particle to serve as a tracer of that halo. Wherever that black hole
particle appears in the particle lightcone within the shell's redshift
range we place a copy of the halo. We repeat this for every shell to
build up a lightcone halo catalogue that extends to :math:`z=15`.

.. warning:: This method only works for halos which contain at least
             one black hole particle. All halos below the black hole
             seeding mass are likely to be missing from the lightcone
             catalogue. Some halos above the seeding mass, such as
             satellite subhalos, may lose their central black hole in
             some cases and also not appear in the halo lightcone.

For more information on the lightcone halo catalogues, see the links below:
	     
.. toctree::
   :maxdepth: 2

   Directory layout <halo_lightcone_layout>
   File format <halo_lightcone_format>
