Lightcone outputs
=================

When we observe the real Universe, the light from distant objects
takes time to reach us. This means we see these objects as they were
when the light was emitted. More distant objects are seen as they were
at earlier times.

The FLAMINGO simulations attempt to replicate this effect for easier
comparison with observations. We place several virtual observers in
the simulated volume of space at the present day, and as the
simulation evolves we identify particles which cross each observer's
lightcone. A particle crosses the lightcone when it passes exactly the
distance at which light emitted from it would arrive at the observer
today. These particles are stored in the lightcone outputs.

The lightcone outputs extend to redshifts where the comoving distance
is greater than the simulation box size. The periodic simulation box is
replicated as necessary it to fill the lightcone volume.

Particle lightcones
-------------------

:doc:`particle_lightcones` record every particle which crossed the observer's
lightcone out to some maximum redshift. At high redshift the volume
and number of particles in the lightcone becomes extremely large, so
for each particle type there is an upper redshift limit beyond which
particles are not output.

HEALPix maps
------------

The :doc:`healpix_lightcones` are full-sky projected maps of particle
properties (such as mass or x-ray luminosity) in concentric spherical
shells around the observer. When a particle crosses the lightcone we
determine which radial shell it is in and accumulate its contribution
to the appropriate map.

.. figure:: _static/images/lightcones/sphere.png
   :class: with-border

   Projected gas mass in 10 concentric spherical shells around an
   observer in the ``L1_m8`` simulation. The observer is at the centre
   of the sphere. The outer sphere has a comoving radius of
   approximately 2Gpc.

Lightcone documentation
-----------------------

The following sections describe the layout and contents of the
lightcone outputs. See also Appendix A of `Schaye et al (2023)
<https://ui.adsabs.harvard.edu/abs/2023MNRAS.tmp.2384S>`__.

.. toctree::
   :maxdepth: 2

   healpix_lightcones
   halo_lightcones
   particle_lightcones

