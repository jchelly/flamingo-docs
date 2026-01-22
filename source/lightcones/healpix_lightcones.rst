HEALPix lightcone maps
======================

The lightcone HEALPix maps are full-sky projected maps of particle
properties (such as mass or x-ray luminosity) in concentric spherical
shells around the observer. When a particle crosses the lightcone we
determine which radial shell it is in and accumulate its contribution
to the appropriate map.

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

The FLAMINGO healpix light-cones are a set of concentric spheres centered on virtual observers. The details of the light-cone construction are stated in Appendix A of `Schaye et al (2023) <https://ui.adsabs.harvard.edu/abs/2023MNRAS.tmp.2384S>`__. The files are stored as `Healpix <https://healpix.sourceforge.io/>`_ files with :math:`N_\mathrm{side} = 16384`, corresponding to a resolution of 0.21 arcmin. All `Healpy <https://healpy.readthedocs.io/en/latest/>`_ routines can be applied to postprocess the data (e.g., smoothing, masking, or applying pixel window functions.)


An example of how to read in the data using lightcone_io is 

.. code-block:: python

   import lightcone_io.healpix_maps as hm

   observer_number = 0
   path = f"/cosma8/data/dp004/flamingo/Runs/L1000N1800/HYDRO_FIDUCIAL/neutrino_corrected_maps/"
   shells = hm.ShellArray(f"{path}", f"lightcone{observer_number}")
   shells[0].map_names

The final line shows all quantaties that are save on the lightcone, which all the light-cones are ``DarkMatterMass``, ``NeutrinoMass``, and ``TotalMass``, whereas the light-cones corresponding to the hydrodynamical simulations also contain the quantaties ``BlackHoleMass``, ``ComptonY``, ` ``DM``, ``DopplerB``, ``SmoothedGasMass``, ``StarFormationRate``, ``StellarMass``, ``UnsmoothedHasMass``, ``XrayErositaHighIntrinsicEnergies``, ``XrayErositaHighIntrinsicPhotons``, ``XrayErositaLowIntrinsicEnergies``, ``XrayErositaLowIntrinsicPhotons``, ``XrayROSATIntrinsicEnergies``, and ``XrayROSATIntrinsicPhotons``. 

The shells are stored such that ``shell 0`` corresponds to the lowest redshift shell. In general, the width of the shells is math:`\Delta z = 0.05`. The comoving distance to the inner and outer parts of the shells can also be read in from the shells directly, as indicated in the example below. The example additionaly shows how to read in the total project mass and conversion between internal units and cgs units.

.. code-block:: python

   for i in range(shells.nr_shells):  
       total_mass = shells[i]["TotalMass"][:]
       inner_radius = shells[i].comoving_inner_radius
       outer_radius = shells[i].comoving_outer_radius
	

Integrated light-cones that have been generated in the analysis for specific papers can be found at

.. toctree::
   :maxdepth: 1

   integrated_lightcones















