Property types
--------------

Subhalo quantities (SH)
^^^^^^^^^^^^^^^^^^^^^^^

are computed for each subhalo identified by the halo finder,
irrespective of whether it is a field halo or a satellite (or even
satellite of satellite and so on). They include all particles that they
halo finder has determined are bound to the subhalo. Subhalo properties
are contained within the group ``BoundSubhalo`` in the output file.

Exclusive sphere quantities (ES)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

are similar to subhalo quantities, but they include only the particles
that are bound to the subhalo, and apply an additional radial cut
(aperture). We use eight different aperture radii (10, 30, 50, 100, 300,
500, 1000, 3000 kpc), so that every (sub-)halo has eight of these.
Exclusive sphere properties are contained within a group
``ExclusiveSphere/XXXkpc``, where ``XXX`` is the corresponding aperture
radius.

Inclusive sphere quantities (IS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

use the same physical aperture radii as the exclusive sphere quantities,
but include all particles within the radius, regardless of their
membership status. They are stored within a group
``InclusiveSphere/XXXkpc``.

Exclusive projected quantities (EP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

are similar to exclusive sphere quantities, except that their aperture
filter is applied in projection, and this for independent projections
along the x-, y- and z-axis. Along the projection axis, we do not apply
any radial cut, so that the depth corresponds to all particles bound to
the (sub-)halo. With four projected aperture radii (10, 30, 50, 100
kpc), we then have twelve sets of projected aperture quantities for each
(sub-)halo. Projected aperture quantities are stored in a group named
``ProjectedAperture/XXXkpc/projP``, where ``XXX`` is the corresponding
aperture radius, and ``P`` corresponds to a particular projection
direction (``x``, ``y`` or ``z``).

Spherical overdensity properties (SO)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

are fundamentally different from the three other types in that their
aperture radius is determined from the density profile and is different
for different halos. They always include all particles within a sphere
around the centre of potential, regardless of halo membership. The
radius is either the radius at which the density reaches a certain
target value (50 crit, 100 crit, 200 crit, 500 crit, 1000 crit, 2500
crit, 200 mean, BN98) or a multiple of such a radius (5xR 500 crit).
Details of the spherical overdensity calculation are given at the end of
this document. Spherical overdensities are only computed for centrals,
i.e. field halos. The inclusive sphere quantities are stored in a group
``SO/XXX``, where ``XXX`` can be either ``XXX_mean`` for density
multiples of the mean density, ``XXX_crit`` for density multiples of the
critical density, ``BN98`` for the overdensity definition of Bryan &
Norman (1998), and ``YxR_XXX_ZZZ`` for multiples of some other radius
(e.g. ``5xR_2500_mean``). The latter can only be computed after the
corresponding density multiple SO radius has been computed. This is
achieved by ordering the calculations.

InputHalos
^^^^^^^^^^

Some properties are directly copied from the original halo catalogue
that was passed to SOAP. These are stored in a separate group,
``InputHalos``.

SOAP
^^^^

Some properties are computed by SOAP using the other halo properties
present in the catalogue. These are stored in a separate group,
``SOAP``. This is just done for convenience; these quantities can be
computed from the SOAP output alone.

The table below lists
^^^^^^^^^^^^^^^^^^^^^

all the groups in the output file which containing datasets. Note that
there will be three groups (``x``, ``y`` or ``z``) for each
``ProjectedAperture`` variation. Each halo variation can have a filter
applied to it. If a halo does not satisfy the filter then the variation
will not be calculated for that halo. More information on filters can be
found in the next section.


+------------------------------------+----------------------------------------+------------+-------------+
| Group name (HDF5)                  | Group name (swiftsimio)                | Inclusive? |  Filter     |
+====================================+========================================+============+=============+
| ``BoundSubhalo``                   | ``bound_subhalo``                      | n          |             |
+------------------------------------+----------------------------------------+------------+-------------+
| ``SO/200_crit``                    | ``spherical_overdensity_200_crit``     | y          |             |
+------------------------------------+----------------------------------------+------------+-------------+
| ``SO/50_crit``                     | ``spherical_overdensity_50_crit``      | y          | general     |
+------------------------------------+----------------------------------------+------------+-------------+
| ``SO/100_crit``                    | ``spherical_overdensity_100_crit``     | y          | general     |
+------------------------------------+----------------------------------------+------------+-------------+
| ``SO/200_mean``                    | ``spherical_overdensity_200_mean``     | y          |             |
+------------------------------------+----------------------------------------+------------+-------------+
| ``SO/500_crit``                    | ``spherical_overdensity_500_crit``     | y          |             |
+------------------------------------+----------------------------------------+------------+-------------+
| ``SO/5xR_500_crit``                | ``spherical_overdensity_5xr_500_crit`` | y          | general     |
+------------------------------------+----------------------------------------+------------+-------------+
| ``SO/1000_crit``                   | ``spherical_overdensity_1000_crit``    | y          | general     |
+------------------------------------+----------------------------------------+------------+-------------+
| ``SO/2500_crit``                   | ``spherical_overdensity_2500_crit``    | y          | general     |
+------------------------------------+----------------------------------------+------------+-------------+
| ``SO/BN98``                        | ``spherical_overdensity_bn98``         | y          | general     |
+------------------------------------+----------------------------------------+------------+-------------+
| ``ExclusiveSphere/10kpc``          | ``exclusive_sphere_10kpc``             | n          |             |
+------------------------------------+----------------------------------------+------------+-------------+
| ``ExclusiveSphere/30kpc``          | ``exclusive_sphere_30kpc``             | n          |             |
+------------------------------------+----------------------------------------+------------+-------------+
| ``ExclusiveSphere/50kpc``          | ``exclusive_sphere_50kpc``             | n          |             |
+------------------------------------+----------------------------------------+------------+-------------+
| ``ExclusiveSphere/100kpc``         | ``exclusive_sphere_100kpc``            | n          |             |
+------------------------------------+----------------------------------------+------------+-------------+
| ``ExclusiveSphere/300kpc``         | ``exclusive_sphere_300kpc``            | n          |             |
+------------------------------------+----------------------------------------+------------+-------------+
| ``ExclusiveSphere/500kpc``         | ``exclusive_sphere_500kpc``            | n          | general     |
+------------------------------------+----------------------------------------+------------+-------------+
| ``ExclusiveSphere/1000kpc``        | ``exclusive_sphere_1000kpc``           | n          | general     |
+------------------------------------+----------------------------------------+------------+-------------+
| ``ExclusiveSphere/3000kpc``        | ``exclusive_sphere_3000kpc``           | n          | general     |
+------------------------------------+----------------------------------------+------------+-------------+
| ``InclusiveSphere/10kpc``          | ``inclusive_sphere_10kpc``             | y          |             |
+------------------------------------+----------------------------------------+------------+-------------+
| ``InclusiveSphere/30kpc``          | ``inclusive_sphere_30kpc``             | y          |             |
+------------------------------------+----------------------------------------+------------+-------------+
| ``InclusiveSphere/50kpc``          | ``inclusive_sphere_50kpc``             | y          |             |
+------------------------------------+----------------------------------------+------------+-------------+
| ``InclusiveSphere/100kpc``         | ``inclusive_sphere_100kpc``            | y          |             |
+------------------------------------+----------------------------------------+------------+-------------+
| ``InclusiveSphere/300kpc``         | ``inclusive_sphere_300kpc``            | y          |             |
+------------------------------------+----------------------------------------+------------+-------------+
| ``InclusiveSphere/500kpc``         | ``inclusive_sphere_500kpc``            | y          | general     |
+------------------------------------+----------------------------------------+------------+-------------+
| ``InclusiveSphere/1000kpc``        | ``inclusive_sphere_1000kpc``           | y          | general     |
+------------------------------------+----------------------------------------+------------+-------------+
| ``InclusiveSphere/3000kpc``        | ``inclusive_sphere_3000kpc``           | y          | general     |
+------------------------------------+----------------------------------------+------------+-------------+
| ``ProjectedAperture/10kpc/projP``  | ``projected_aperture_10kpc_projP``     | n          | general     |
+------------------------------------+----------------------------------------+------------+-------------+
| ``ProjectedAperture/30kpc/projP``  | ``projected_aperture_30kpc_projP``     | n          | general     |
+------------------------------------+----------------------------------------+------------+-------------+
| ``ProjectedAperture/50kpc/projP``  | ``projected_aperture_50kpc_projP``     | n          | general     |
+------------------------------------+----------------------------------------+------------+-------------+
| ``ProjectedAperture/100kpc/projP`` | ``projected_aperture_100kpc_projP``    | n          | general     |
+------------------------------------+----------------------------------------+------------+-------------+
| ``SOAP``                           | ``soap``                               | -          |             |
+------------------------------------+----------------------------------------+------------+-------------+
| ``InputHalos``                     | ``input_halos``                        | -          |             |
+------------------------------------+----------------------------------------+------------+-------------+
| ``InputHalos/HBTplus``             | ``input_halos_hbtplus``                | -          |             |
+------------------------------------+----------------------------------------+------------+-------------+
| ``InputHalos/FOF``                 | ``input_halos_fof``                    | -          |             |
+------------------------------------+----------------------------------------+------------+-------------+

