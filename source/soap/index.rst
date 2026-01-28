Halo catalogues
=================

When we observe the real Universe, the light from distant objects
takes time to reach us. This means we see these objects as they were
when the light was emitted. More distant objects are seen as they were
at earlier times.

The FLAMINGO simulations attempt to replicate this effect for easier
comparison with observations. We place several virtual observers in
the simulated volume of space at the present day, and as the
simulation evolves we identify and store particles which cross each
observer's lightcone. A particle crosses the lightcone when it passes
exactly the distance at which light emitted from it would arrive at
the observer today.

The FLAMINGO lightcone outputs include particle data, HEALPix maps, and
halo catalogues. These are described in the following sections:

.. toctree::
   :maxdepth: 2

   particle_selection
   property_filters
   property_table
   membership_files


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
       \frac{4\pi{}}{3} R_{\rm{}SO}^3 \rho{}_{\rm{}target} = M_{\rm{}SO},\label{eq:MSO_condition}
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
       \frac{4\pi{}}{3} \rho{}_{\rm{}target} R_{\rm{}SO}^3 = M_{\rm{}low} + \left( \frac{M_{\rm{}high}-M_{\rm{}low}}{R_{\rm{}high} - R_{\rm{}low}} \right) \left(R_{\rm{}SO} - R_{\rm{}low}\right),
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
   :math:`r=0` offset for the cumulative mass profile. Since the centre
   of potential is the position of the most bound particle, there should
   always be at least one such particle.

#. Construct the density profile by dividing the cumulative mass at
   every radius by the volume of the sphere with that radius.

#. Find intersection points between the density profile and the target
   density, i.e. the radii :math:`R_{1,2}` and masses :math:`M_{1,2}`
   where the density profile goes from above to below the threshold:

   #. If there are none, analytically compute
      :math:`R_{\rm{}SO}=\sqrt{3M_1/(4\pi{}R_1\rho_{\rm{}target})}`,
      where :math:`R_1` and :math:`M_1` are the first non zero radius
      and the corresponding cumulative mass. This is a special case of
      Eq. (`[eq:RSO] <#eq:RSO>`__). Unless there are multiple particles
      at the exact centre of potential position, this radius estimate
      will then be based on just two particles.

   #. In all other cases, we use :math:`R_{1,2}` and :math:`M_{1,2}` as
      input for Eq. (`[eq:RSO] <#eq:RSO>`__) and solve for
      :math:`R_{\rm{}SO}`. The only exception is the special case where
      :math:`R_1 = R_2`. If that happens, we simply move further down
      the line until we find a suitable interval.

#. From :math:`R_{\rm{}SO}`, we determine :math:`M_{\rm{}SO}` using Eq.
   (`[eq:MSO_condition] <#eq:MSO_condition>`__).

Neutrinos – if present in the model – are included
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

in the inclusive sphere calculation (and only here, since neutrino
particles cannot be bound to a halo) by adding both their weighted
masses (which can be negative), as well as the contribution from the
background neutrino density. The latter is achieved by explicitly adding
the cumulative mass profile at constant neutrino density to the total
cumulative mass profile before computing the density profile. This is
the only place where neutrinos explicitly enter the algorithm, except
for the neutrino masses computed for the SOs. Neutrinos are not included
in the calculation of the centre of mass and centre of mass velocity.


