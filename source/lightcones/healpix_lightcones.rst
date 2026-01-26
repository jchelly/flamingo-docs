HEALPix maps
============

The FLAMINGO simulation lightcone outputs include full-sky projected
maps of particle properties (such as mass or x-ray luminosity) in
concentric spherical shells around the observer. When a particle
crosses the observer's lightcone we determine which radial shell it is
in and accumulate its contribution to the appropriate maps.

These maps use the `HEALPix <https://healpix.sourceforge.io/>`__
pixelisation scheme to divide the sky into pixels of equal area. The
maps are provided at two resolutions. The highest resolution maps have
an angular resolution of about 13 arcseconds (:math:`N_{side}=16384`).
Since these large maps can be difficult to work with, we also provide
down-sampled maps with an angular resolution of about 50 arcseconds
(:math:`N_{side}=4096`).

.. grid:: 2

    .. grid-item-card:: Projected mass in shells
       :columns: 5

       .. image:: images/sphere.png

       Projected gas mass in 10 concentric spherical shells around an
       observer in the ``L1_m8`` simulation. The observer is at the centre
       of the sphere. The outer sphere has a comoving radius of
       approximately 2Gpc.

    .. grid-item-card:: Compton Y parameter at z < 0.05
       :columns: 7

       .. image:: images/comptony_z0.05.png

       Mollweide projected full sky map of the thermal
       Sunyaev-Zel'dovich effect as quantified by the Compton y
       parameter for the redshift interval 0 < z < 0.05.

HEALPix maps of a range of physical quantities are available. For more
information see the documentation links below and appendix A of
`Schaye et al (2023)
<https://ui.adsabs.harvard.edu/abs/2023MNRAS.tmp.2384S>`__.

.. toctree::
   :maxdepth: 2

   Directory layout <healpix_layout>
   File format <healpix_format>
   Shell redshifts <healpix_shell_redshifts>
   Map descriptions <healpix_map_descriptions>
   integrated_lightcones















