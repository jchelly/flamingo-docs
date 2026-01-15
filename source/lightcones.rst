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

The FLAMINGO simulations include two types of lightcone output:

  * Particle lightcones record every particle which crossed the
    observer's lightcone out to some maximum redshift.
  * HEALPix maps are pixelated all-sky maps containing the accumulated
    properties of particles crossing the lightcone in concentric
    spherical shells around the observer.

The following sections describe the layout and contents of the
lightcone outputs. See also Appendix A of `Schaye et al (2023)
<https://ui.adsabs.harvard.edu/abs/2023MNRAS.tmp.2384S>`__.

.. toctree::
   :maxdepth: 2

   healpix_lightcones
   halo_lightcones
   particle_lightcones

