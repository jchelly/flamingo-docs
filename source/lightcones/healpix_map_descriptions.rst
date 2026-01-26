HEALPix map descriptions
========================

This page describes the available HEALPix maps: i.e. what quantities
have been computed and their units.

Some quantities relating to gas particles are smoothed onto the map by
converting the particle's SPH smoothing length to an angular size. For
other quantities the full contribution from the particle is added to
a single pixel and no smoothing is done.

Quantities and units
--------------------

A full list of the available quantities is shown in the table below.

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Name
     - Units
     - Smoothed
     - Description
   * - ``BlackHoleMass``
     - :math:`10^{10}\mathrm{M}_\odot`
     - No
     - Total dynamical mass of the black hole particles in each pixel.
   * - ``ComptonY``
     - :math:`-`
     - Yes
     - Thermal SZ effect :ref:`compton-y`.
   * - ``DM``
     - :math:`\mathrm{Mpc}^{-2}`
     - Yes
     - :ref:`dispersion-measure` (see note about bug, below).
   * - ``DarkMatterMass``
     - :math:`10^{10}\mathrm{M}_\odot`
     - No
     - Total mass of the dark matter particles in each pixel.
   * - ``DopplerB``
     - :math:`-`
     - Yes
     - Kinematic SZ effect :ref:`doppler-b` (see note about bug, below).
   * - ``NeutrinoMass``
     - :math:`10^{10}\mathrm{M}_\odot`
     - No
     - Total mass of neutrinos in each pixel. This consists of a constant background density plus perturbations represented by the neutrino particles.
   * - ``SmoothedGasMass``
     - :math:`10^{10}\mathrm{M}_\odot`
     - Yes
     - Total (SPH smoothed) mass of gas in each pixel.
   * - ``StarFormationRate``
     - :math:`10^{10}\mathrm{M}_\odot\mathrm{Mpc}^{-1}\mathrm{km/s}`
     - No
     - Total star formation rate of gas in each pixel.
   * - ``StellarMass``
     - :math:`10^{10}\mathrm{M}_\odot`
     - No
     - Total mass of star particles in each pixel.
   * - ``TotalMass``
     - :math:`10^{10}\mathrm{M}_\odot`
     - No
     - Total mass in each pixel, including gas, dark matter, stars, black holes and neutrinos.
   * - ``UnsmoothedGasMass``
     - :math:`10^{10}\mathrm{M}_\odot`
     - No
     - Total mass of gas in each pixel without smoothing.
   * - ``XrayErositaHighIntrinsicEnergies``
     - :math:`10^{10}\mathrm{M}_\odot\mathrm{Mpc}^{-3}\mathrm{(km/s)}^{3}`
     - Yes
     - Total X-ray flux in the eROSITA 2.3 - 8.0 keV band
   * - ``XrayErositaHighIntrinsicPhotons``
     - :math:`\mathrm{Mpc}^{-3}\mathrm{km/s}`
     - Yes
     - Total X-ray photon flux in the eROSITA 2.3 - 8.0 keV band
   * - ``XrayErositaLowIntrinsicEnergies``
     - :math:`10^{10}\mathrm{M}_\odot\mathrm{Mpc}^{-3}\mathrm{(km/s)}^{3}`
     - Yes
     - Total X-ray flux in the eROSITA 0.2 - 2.3 keV band
   * - ``XrayErositaLowIntrinsicPhotons``
     - :math:`\mathrm{Mpc}^{-3}\mathrm{km/s}`
     - Yes
     - Total X-ray photon flux in the eROSITA 0.2 - 2.3 keV band
   * - ``XrayROSATIntrinsicEnergies``
     - :math:`10^{10}\mathrm{M}_\odot\mathrm{Mpc}^{-3}\mathrm{(km/s)}^{3}`
     - Yes
     - Total X-ray flux in the ROSAT 0.5 - 2.0 keV band
   * - ``XrayROSATIntrinsicPhotons``
     - :math:`\mathrm{Mpc}^{-3}\mathrm{km/s}`
     - Yes
     - Total X-ray photon flux in the ROSAT 0.5 - 2.0 keV  band

.. _compton-y:

Compton :math:`y` parameter
---------------------------

The Compton :math:`y` parameter maps are computed by accumulating the
following dimensionless quantity for each gas particle which crosses
the lightcone:

  :math:`\Delta y = \frac{\sigma_\text{T} k_\text{B}}{m_\text{e}c^2}  \frac{m_\text{g} n_\text{e} T}{\Omega_\text{pixel}^2 d_\text{A}^2 \rho}`

where :math:`m_\text{g}` is the particle's mass,
:math:`\Omega_\text{pixel}` is the solid angle of a \healpix pixel and
:math:`d_\text{A}` is the angular diameter distance to the observer.

.. _doppler-b:

Doppler :math:`b` parameter
---------------------------

.. warning:: Due to a bug, the contribution of each particle to the
             Doppler :math:`b` parameter maps incorrectly included an
             extra factor of :math:`a`. In the data release this has been
             approximately corrected using the expansion factor at the
             shell mid point.

The Doppler :math:`b` parameter maps were intended to be computed by
accumulating the following dimensionless quantity for each gas
particle which crosses the lightcone:

  :math:`\Delta b = \frac{n_\text{e} m_\text{g} \sigma_\text{T} v_\text{r}}{\Omega_\text{pixel}^2 d_\text{A}^2 \rho c}`

where :math:`v_\text{r}` is the particle's radial velocity relative to the
observer.

.. _dispersion-measure:

Dispersion measure
------------------

.. warning:: Due to a bug, the contribution of each particle to the
             dispersion measure maps incorrectly omitted a factor of
             :math:`a`. In the data release this has been
             approximately corrected using the expansion factor at the
             shell mid point.

The dispersion measure maps were intended to be computed by
accumulating the following quantity for each gas particle which
crosses the lightcone:

  :math:`\Delta \text{DM} = \frac{n_\text{e} m_\text{g} a}{\Omega_\text{pixel}^2 d_\text{A}^2 \rho}`

where :math:`a` is the expansion factor at which the particle crossed the lightcone.
