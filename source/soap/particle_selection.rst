SOAP halo variations
====================

SOAP calculates properties for several definitions of a halo. These various types
give users the freedom to select the most appropriate definition for their scientific
use case.

.. _bound_subhalo_description:

Bound subhalo
-------------

Bound subhalo properties are computed for each subhalo identified by the subhalo finder,
irrespective of whether it is a central or satellite subhalo (or even
a satellite of satellite, and so on). They include all particles that the
subhalo finder has determined to be bound to the subhalo. Subhalo properties
are contained within the group ``bound_subhalo`` in the output file.

.. _exclusive_sphere_description:

Exclusive sphere
----------------

Exclusive sphere properties are similar to bound subhalo quantities, but
they include only the particles
that are bound to the subhalo and also satisfy an additional radial cut
(aperture). We use eight different aperture radii (10, 30, 50, 100, 300,
500, 1000, 3000 physical kpc), so that every subhalo has eight of these.
Exclusive sphere properties are contained within a group
``exclusive_sphere_XXXkpc``, where ``XXX`` is the corresponding aperture
radius.

.. _inclusive_sphere_description:

Inclusive sphere
----------------

Inclusive sphere properties use the same physical aperture radii as 
the exclusive sphere quantities,
but include all particles within the radius, regardless of their
membership status. They are stored within a group
``inclusive_sphere_XXXkpc``, where ``XXX`` is the corresponding aperture
radius.

.. _projected_aperture_description:

Exclusive projected aperture
----------------------------

The projected apertures are similar to exclusive sphere quantities, 
except that their aperture
filter is applied in 3 independent projections
along the x-, y- and z-axis. Along the projection axis, we do not apply
any radial cut, so that the depth corresponds to all particles bound to
the subhalo. With four projected aperture radii (10, 30, 50, 100
kpc), we then have twelve sets of projected aperture quantities for each
subhalo. Projected aperture quantities are stored in a group named
``projected_aperture_XXXkpc_projP``, where ``XXX`` is the corresponding
aperture radius, and ``P`` corresponds to a particular projection
direction (``x``, ``y`` or ``z``).

.. _spherical_overdensity_description:

Spherical overdensity
---------------------

Spherical overdensities are fundamentally different from the other
halo variations in that their
aperture radius is determined from the density profile and so has a different value
for each halo. They always include all particles within a sphere
centred on the most bound particle, regardless of particle subhalo membership. The
radius is either the radius at which the density reaches a certain
target value (50 crit, 100 crit, 200 crit, 500 crit, 1000 crit, 2500
crit, 200 mean,
`Bryan & Norman (1998) <https://ui.adsabs.harvard.edu/abs/1998ApJ...495...80B>`__)
or a multiple of such a radius (5xR 500 crit).
See `Spherical overdensity calculations`_ for details about how the radii are
calculated.
Spherical overdensities are only computed for centrals,
i.e. field halos. The inclusive sphere quantities are stored in a group
``spherical_overdensity_XXX``, where ``XXX`` are the target density values
listed above.

Input Halos
-----------

Some properties are copied directly from the original subhalo catalogue
that was passed to SOAP. These are stored in a three separate groups.
``input_halos`` contains the fundamental properties required for SOAP
to run. ``input_halos_fof`` contains the FoF properties of the host of
each central subhalo. ``input_halos_hbtplus`` contains properties copied directly
from the HBT-HERONS catalogues.

SOAP
----

Some properties are computed by SOAP using the other halo properties
present in the catalogue. These are stored in a separate group,
``SOAP``. This is just done for convenience; these quantities can be
computed from the SOAP output alone.

Summary table
-------------

The table below lists all the groups in the output file that contain datasets.
Note that there will be three groups (``x``, ``y`` or ``z``) for each
projected aperture variation. Each halo variation can have a filter
applied to it. If a halo does not satisfy the filter then the variation
will not be calculated for that halo. More information on filters can be
found :doc:`in the next section <property_filters>`.


+----------------------------------------+------------+-------------+
| Group name                             | Inclusive? |  Filter     |
+========================================+============+=============+
| ``bound_subhalo``                      | n          | basic       |
+----------------------------------------+------------+-------------+
| ``spherical_overdensity_200_crit``     | y          | basic       |
+----------------------------------------+------------+-------------+
| ``spherical_overdensity_50_crit``      | y          | general     |
+----------------------------------------+------------+-------------+
| ``spherical_overdensity_100_crit``     | y          | general     |
+----------------------------------------+------------+-------------+
| ``spherical_overdensity_200_mean``     | y          | basic       |
+----------------------------------------+------------+-------------+
| ``spherical_overdensity_500_crit``     | y          | basic       |
+----------------------------------------+------------+-------------+
| ``spherical_overdensity_5xr_500_crit`` | y          | general     |
+----------------------------------------+------------+-------------+
| ``spherical_overdensity_1000_crit``    | y          | general     |
+----------------------------------------+------------+-------------+
| ``spherical_overdensity_2500_crit``    | y          | general     |
+----------------------------------------+------------+-------------+
| ``spherical_overdensity_bn98``         | y          | general     |
+----------------------------------------+------------+-------------+
| ``exclusive_sphere_10kpc``             | n          | basic       |
+----------------------------------------+------------+-------------+
| ``exclusive_sphere_30kpc``             | n          | basic       |
+----------------------------------------+------------+-------------+
| ``exclusive_sphere_50kpc``             | n          | basic       |
+----------------------------------------+------------+-------------+
| ``exclusive_sphere_100kpc``            | n          | basic       |
+----------------------------------------+------------+-------------+
| ``exclusive_sphere_300kpc``            | n          | basic       |
+----------------------------------------+------------+-------------+
| ``exclusive_sphere_500kpc``            | n          | general     |
+----------------------------------------+------------+-------------+
| ``exclusive_sphere_1000kpc``           | n          | general     |
+----------------------------------------+------------+-------------+
| ``exclusive_sphere_3000kpc``           | n          | general     |
+----------------------------------------+------------+-------------+
| ``inclusive_sphere_10kpc``             | y          | basic       |
+----------------------------------------+------------+-------------+
| ``inclusive_sphere_30kpc``             | y          | basic       |
+----------------------------------------+------------+-------------+
| ``inclusive_sphere_50kpc``             | y          | basic       |
+----------------------------------------+------------+-------------+
| ``inclusive_sphere_100kpc``            | y          | basic       |
+----------------------------------------+------------+-------------+
| ``inclusive_sphere_300kpc``            | y          | basic       |
+----------------------------------------+------------+-------------+
| ``inclusive_sphere_500kpc``            | y          | general     |
+----------------------------------------+------------+-------------+
| ``inclusive_sphere_1000kpc``           | y          | general     |
+----------------------------------------+------------+-------------+
| ``inclusive_sphere_3000kpc``           | y          | general     |
+----------------------------------------+------------+-------------+
| ``projected_aperture_10kpc_projP``     | n          | general     |
+----------------------------------------+------------+-------------+
| ``projected_aperture_30kpc_projP``     | n          | general     |
+----------------------------------------+------------+-------------+
| ``projected_aperture_50kpc_projP``     | n          | general     |
+----------------------------------------+------------+-------------+
| ``projected_aperture_100kpc_projP``    | n          | general     |
+----------------------------------------+------------+-------------+
| ``soap``                               | \-         | basic       |
+----------------------------------------+------------+-------------+
| ``input_halos``                        | \-         | basic       |
+----------------------------------------+------------+-------------+
| ``input_halos_hbtplus``                | \-         | basic       |
+----------------------------------------+------------+-------------+
| ``input_halos_fof``                    | \-         | basic       |
+----------------------------------------+------------+-------------+


Spherical overdensity calculations
----------------------------------

The radius at which the density reaches a certain threshold value is
found by linear interpolation of the cumulative mass profile obtained
after sorting the particles by radius. The approach we use is different
from that taken by VR, where both the mass and the radius are obtained
from independent interpolations on the mass and density profiles (the
latter uses the logarithm of the density in the interpolation). The VR
approach is inconsistent, in the sense that the condition

.. math::

   \begin{equation}
       \frac{4\pi{}}{3} R_{\rm{}SO}-3 \rho{}_{\rm{}target} = M_{\rm{}SO},\label{eq:MSO_condition}
   \end{equation}

is not guaranteed to be true, and will be especially violated for large
radial bins (the bins are generated from the particle radii by sorting
the particles, so we have no control over their width). We instead opt
to guarantee this condition by only finding :math:`R_{\rm{}SO}` or
:math:`M_{\rm{}SO}` by interpolation and using eq.
(`[eq:MSO_condition] <#eq:MSO_condition>`__) to derive the other
quantity.

.. container:: float
   :name: fig:MSO_vs_RSO

   |image| |image1|

While the interpolation of the logarithmic density profile to find
:math:`R_{\rm{}SO}` is more straightforward, we found that it can lead
to significant deviations between the value of :math:`M_{\rm{}SO}` and
the cumulative mass in neighbouring bins that can be more than one
particle mass, as illustrated in Fig. `1 <#fig:MSO_vs_RSO>`__. The
reason for this is that the cumulative mass profile at fixed density
increases very steeply with radius, so that a small difference in
:math:`R_{\rm{}SO}` leads to a relatively large difference in
:math:`M_{\rm{}SO}`. Conversely, fixing :math:`M_{\rm{}SO}` will lead to
an :math:`R_{\rm{}SO}` that only deviates a little bit from the
:math:`R_{\rm{}SO}` found by interpolating the density profile. However,
doing so requires us to find the intersection of the cumulative mass
profile at fixed density (green line in Fig. `1 <#fig:MSO_vs_RSO>`__)
with the actual cumulative mass profile, which means solving the
following equation:

.. math::

   \begin{equation}
       \frac{4\pi{}}{3} \rho{}_{\rm{}target} R_{\rm{}SO}-3 = M_{\rm{}low} + \left( \frac{M_{\rm{}high}-M_{\rm{}low}}{R_{\rm{}high} - R_{\rm{}low}} \right) \left(R_{\rm{}SO} - R_{\rm{}low}\right),
       \label{eq:RSO}
   \end{equation}

where :math:`R/M_{\rm{}low/high}` are the bounds of the intersecting bin
(which we find in the density profile). This third degree polynomial
equation has no unique solution, although in practice only one of the
three possible complex solutions is real. We find this solution by using
a root finding algorithm within the intersecting bin (we use Brent’s
method for this).

For clarity, this is the full set of rules for determining the SO radius
in SOAP:

#. Sort particles according to radius and construct the cumulative mass
   profile.

#. Discard any particles at zero radius, since we cannot compute a
   density for those. The mass of these particles is used as an
   :math:`r=0` offset for the cumulative mass profile. Since the halo centre
   is the position of the most bound particle, there should
   always be at least one such particle.

#. Construct the density profile by dividing the cumulative mass at
   every radius by the volume of the sphere with that radius.

#. Find intersection points between the density profile and the target
   density, i.e. the radii :math:`R_{1,2}` and masses :math:`M_{1,2}`
   where the density profile goes from above to below the threshold:

   *. If there are none, analytically compute
      :math:`R_{\rm{}SO}=\sqrt{3M_1/(4\pi{}R_1\rho_{\rm{}target})}`,
      where :math:`R_1` and :math:`M_1` are the first non zero radius
      and the corresponding cumulative mass. This is a special case of
      Eq. (`[eq:RSO] <#eq:RSO>`__). Unless there are multiple particles
      at the exact centre of potential position, this radius estimate
      will then be based on just two particles.

   *. In all other cases, we use :math:`R_{1,2}` and :math:`M_{1,2}` as
      input for Eq. (`[eq:RSO] <#eq:RSO>`__) and solve for
      :math:`R_{\rm{}SO}`. The only exception is the special case where
      :math:`R_1 = R_2`. If that happens, we simply move further down
      the line until we find a suitable interval.

#. From :math:`R_{\rm{}SO}`, we determine :math:`M_{\rm{}SO}` using Eq.
   (`[eq:MSO_condition] <#eq:MSO_condition>`__).

Neutrinos (if present in the model) are included in the inclusive sphere calculation
(and only here, since neutrino
particles cannot be bound to a subhalo) by adding both their weighted
masses (which can be negative), as well as the contribution from the
background neutrino density. The latter is achieved by explicitly adding
the cumulative mass profile at constant neutrino density to the total
cumulative mass profile before computing the density profile. This is
the only place where neutrinos explicitly enter the algorithm, except
for the neutrino masses computed for the spherical overdensity properties.


.. |image| image:: images/image7.png
.. |image1| image:: images/image4.png
