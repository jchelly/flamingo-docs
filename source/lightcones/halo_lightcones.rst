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
way to the next and previous snapshot redshifts respectively.


.. toctree::
   :maxdepth: 2

   Directory layout <halo_lightcone_layout>
   File format <halo_lightcone_format>
