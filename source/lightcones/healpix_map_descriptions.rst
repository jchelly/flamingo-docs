HEALPix map descriptions
========================

This page describes the HEALPix maps computed in :doc:`spherical
shells <healpix_shell_redshifts>`, including a list of the available
quantities and their units.

Some quantities relating to gas particles are smoothed onto the map by
converting the particle's SPH smoothing length to an angular size. See
:ref:`smoothed-maps` for details. For other quantities the full
contribution from the particle is added to a single pixel and no
smoothing is done.

.. note:: See :doc:`integrated_lightcones` for HEALPix maps of
          additional, redshift-integrated quantities which were
          computed in post-processing.

Quantities and units
--------------------

THe HEALPix maps include the following quantities:

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
     - Thermal SZ effect :ref:`compton-y`. Excludes :ref:`recently heated gas <agn_exclusion>`.
   * - ``DM``
     - :math:`\mathrm{Mpc}^{-2}`
     - Yes
     - :ref:`dispersion-measure` (see note about bug, below). Excludes :ref:`recently heated gas <agn_exclusion>`.
   * - ``DarkMatterMass``
     - :math:`10^{10}\mathrm{M}_\odot`
     - No
     - Total mass of the dark matter particles in each pixel.
   * - ``DopplerB``
     - :math:`-`
     - Yes
     - Kinematic SZ effect :ref:`doppler-b` (see note about bug, below). Excludes :ref:`recently heated gas <agn_exclusion>`.
   * - ``NeutrinoMass``
     - :math:`10^{10}\mathrm{M}_\odot`
     - No
     - Total mass of neutrinos in each pixel.
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

X-ray maps
----------

There are also maps of X-ray luminosity in various bands. All X-ray
maps are smoothed. There are two types of X-ray maps:

Original X-ray maps output by Swift
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These maps are available for all observers and to high redshift, but
were computed incorrectly :ref:`assuming the z=0 UV background at all
redshifts <issues_xray_uvb>`. They have a ``_FrozenUVB`` suffix in the
``lightconeX_shell_*.hdf5`` map files.

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Name
     - Units
     - Description
   * - ``XrayErositaHighIntrinsicEnergies``
     - :math:`10^{10}\mathrm{M}_\odot\mathrm{Mpc}^{-3}\mathrm{(km/s)}^{3}`
     - Total X-ray flux in the eROSITA 2.3 - 8.0 keV band. :ref:`Assumes z=0 UV background <issues_xray_uvb>`. Excludes :ref:`recently heated gas <agn_exclusion>`.
   * - ``XrayErositaHighIntrinsicPhotons``
     - :math:`\mathrm{Mpc}^{-3}\mathrm{km/s}`
     - Total X-ray photon flux in the eROSITA 2.3 - 8.0 keV band. :ref:`Assumes z=0 UV background <issues_xray_uvb>`. Excludes :ref:`recently heated gas <agn_exclusion>`.
   * - ``XrayErositaLowIntrinsicEnergies``
     - :math:`10^{10}\mathrm{M}_\odot\mathrm{Mpc}^{-3}\mathrm{(km/s)}^{3}`
     - Total X-ray flux in the eROSITA 0.2 - 2.3 keV band. :ref:`Assumes z=0 UV background <issues_xray_uvb>`. Excludes :ref:`recently heated gas <agn_exclusion>`.
   * - ``XrayErositaLowIntrinsicPhotons``
     - :math:`\mathrm{Mpc}^{-3}\mathrm{km/s}`
     - Total X-ray photon flux in the eROSITA 0.2 - 2.3 keV band. :ref:`Assumes z=0 UV background <issues_xray_uvb>`. Excludes :ref:`recently heated gas <agn_exclusion>`.
   * - ``XrayROSATIntrinsicEnergies``
     - :math:`10^{10}\mathrm{M}_\odot\mathrm{Mpc}^{-3}\mathrm{(km/s)}^{3}`
     - Total X-ray flux in the ROSAT 0.5 - 2.0 keV band. :ref:`Assumes z=0 UV background <issues_xray_uvb>`. Excludes :ref:`recently heated gas <agn_exclusion>`.
   * - ``XrayROSATIntrinsicPhotons``
     - :math:`\mathrm{Mpc}^{-3}\mathrm{km/s}`
     - Total X-ray photon flux in the ROSAT 0.5 - 2.0 keV  band. :ref:`Assumes z=0 UV background <issues_xray_uvb>`. Excludes :ref:`recently heated gas <agn_exclusion>`.

Recomputed X-ray maps
^^^^^^^^^^^^^^^^^^^^^

Where lightcone gas particle data are available, we have recomputed
the X-ray maps assuming the correct UV background. These maps are
available for observer 0 in a subset of the ``L1_m9`` variations, and
only for the first ten redshift shells (redshift :math:`z <
0.5`). They have a ``_Recomp`` suffix in the
``lightconeX_shell_*.hdf5`` map files.

Recomputed maps are available for the following simulations:

  * ``L1_m9``
  * ``fgas+2sigma``
  * ``fgas-2sigma``
  * ``fgas-4sigma``
  * ``fgas-8sigma``
  * ``Mstar-1sigma``
  * ``Mstar-1sigma_fgas-4sigma``
  * ``Jet``
  * ``Jet_fgas-4sigma``
  * ``PlanckDCDM12``
  * ``LS8_fgas-8sigma``
  * ``NoCooling``

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Name
     - Units
     - Description
   * - ``XrayErositaHighIntrinsicEnergies``
     - :math:`10^{10}\mathrm{M}_\odot\mathrm{Mpc}^{-3}\mathrm{(km/s)}^{3}`
     - Total X-ray flux in the eROSITA 2.3 - 8.0 keV band. Excludes :ref:`recently heated gas <agn_exclusion>`.
   * - ``XrayErositaHighConvolvedEnergies``
     - :math:`10^{10}\mathrm{M}_\odot\mathrm{Mpc}^{-1}\mathrm{(km/s)}^{3}`
     - Total X-ray flux in the eROSITA 2.3 - 8.0 keV band :ref:`convolved with eROSITA ARF <convolved-Xray>`. Excludes :ref:`recently heated gas <agn_exclusion>`.
   * - ``XrayErositaHighIntrinsicPhotons``
     - :math:`\mathrm{Mpc}^{-3}\mathrm{km/s}`
     - Total X-ray photon flux in the eROSITA 2.3 - 8.0 keV band. Excludes :ref:`recently heated gas <agn_exclusion>`.
   * - ``XrayErositaHighConvolvedPhotons``
     - :math:`\mathrm{Mpc}^{-1}\mathrm{km/s}`
     - Total X-ray photon flux in the eROSITA 2.3 - 8.0 keV band :ref:`convolved with eROSITA ARF <convolved-Xray>`. Excludes :ref:`recently heated gas <agn_exclusion>`.
   * - ``XrayErositaLowIntrinsicEnergies``
     - :math:`10^{10}\mathrm{M}_\odot\mathrm{Mpc}^{-3}\mathrm{(km/s)}^{3}`
     - Total X-ray flux in the eROSITA 0.2 - 2.3 keV band. Excludes :ref:`recently heated gas <agn_exclusion>`.
   * - ``XrayErositaLowConvolvedEnergies``
     - :math:`10^{10}\mathrm{M}_\odot\mathrm{Mpc}^{-1}\mathrm{(km/s)}^{3}`
     - Total X-ray flux in the eROSITA 0.2 - 2.3 keV band :ref:`convolved with eROSITA ARF <convolved-Xray>`. Excludes :ref:`recently heated gas <agn_exclusion>`.
   * - ``XrayErositaLowIntrinsicPhotons``
     - :math:`\mathrm{Mpc}^{-3}\mathrm{km/s}`
     - Total X-ray photon flux in the eROSITA 0.2 - 2.3 keV band. Excludes :ref:`recently heated gas <agn_exclusion>`.
   * - ``XrayErositaLowConvolvedPhotons``
     - :math:`\mathrm{Mpc}^{-1}\mathrm{km/s}`
     - Total X-ray photon flux in the eROSITA 0.2 - 2.3 keV band :ref:`convolved with eROSITA ARF <convolved-Xray>`. Excludes :ref:`recently heated gas <agn_exclusion>`.
   * - ``XrayROSATIntrinsicEnergies``
     - :math:`10^{10}\mathrm{M}_\odot\mathrm{Mpc}^{-3}\mathrm{(km/s)}^{3}`
     - Total X-ray flux in the ROSAT 0.5 - 2.0 keV band. Excludes :ref:`recently heated gas <agn_exclusion>`.
   * - ``XrayROSATConvolvedEnergies``
     - :math:`10^{10}\mathrm{M}_\odot\mathrm{Mpc}^{-1}\mathrm{(km/s)}^{3}`
     - Total X-ray flux in the ROSAT 0.5 - 2.0 keV  band :ref:`convolved with the ROSAT response function <convolved-Xray>`. Excludes :ref:`recently heated gas <agn_exclusion>`.
   * - ``XrayROSATIntrinsicPhotons``
     - :math:`\mathrm{Mpc}^{-3}\mathrm{km/s}`
     - Total X-ray photon flux in the ROSAT 0.5 - 2.0 keV  band. Excludes :ref:`recently heated gas <agn_exclusion>`.
   * - ``XrayROSATConvolvedPhotons``
     - :math:`\mathrm{Mpc}^{-1}\mathrm{km/s}`
     - Total X-ray photon flux in the ROSAT 0.5 - 2.0 keV band :ref:`convolved with the ROSAT response function <convolved-Xray>`. Excludes :ref:`recently heated gas <agn_exclusion>`.



.. _agn_exclusion:

Exclusion of recently heated gas particles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Several of the maps described above, including the X-ray maps, Compton
:math:`y` parameter, Doppler :math:`b` parameter, and dispersion
measure were computed using only gas particles which have not been
recently heated by AGN. Gas particles are excluded from these maps if
they have been AGN heated within the last :math:`15 \mathrm{Myr}` and
their temperature is between :math:`10^{-1} \Delta T_{\mathrm{AGN}}`
and :math:`10^{0.3} \Delta T_{\mathrm{AGN}}`, where :math:`\Delta
T_{\mathrm{AGN}}` is the AGN feedback heating temperature.

.. _compton-y:

Compton :math:`y` parameter
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Compton :math:`y` parameter maps are computed by accumulating the
following dimensionless quantity for each gas particle which crosses
the lightcone:

  :math:`\Delta y = \frac{\sigma_\text{T} k_\text{B}}{m_\text{e}c^2}  \frac{m_\text{g} n_\text{e} T}{\Omega_\text{pixel}^2 d_\text{A}^2 \rho}`

where :math:`m_\text{g}` is the particle's mass,
:math:`\Omega_\text{pixel}` is the solid angle of a \healpix pixel and
:math:`d_\text{A}` is the angular diameter distance to the
observer.  Excludes :ref:`gas recently heated by AGN <agn_exclusion>`.

.. _doppler-b:

Doppler :math:`b` parameter
^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
observer. Excludes :ref:`gas recently heated by AGN <agn_exclusion>`.

.. _dispersion-measure:

Dispersion measure
^^^^^^^^^^^^^^^^^^

.. warning:: Due to a bug, the contribution of each particle to the
             dispersion measure maps incorrectly omitted a factor of
             :math:`a`. In the data release this has been
             approximately corrected using the expansion factor at the
             shell mid point.

The dispersion measure maps were intended to be computed by
accumulating the following quantity for each gas particle which
crosses the lightcone:

  :math:`\Delta \text{DM} = \frac{n_\text{e} m_\text{g} a}{\Omega_\text{pixel}^2 d_\text{A}^2 \rho}`

where :math:`a` is the expansion factor at which the particle crossed
the lightcone.  Excludes :ref:`gas recently heated by AGN
<agn_exclusion>`.

.. _convolved-Xray:

Convolved X-ray Maps
^^^^^^^^^^^^^^^^^^^^

The convolved X-ray maps (e.g. ``XrayErositaLowConvolvedPhotons``) are
constructed in the same way as the ``Intrinsic`` X-ray maps, except
that the emitted photon energy is convolved with the effective area of
the detector belonging to the telescope of the corresponding energy
band (e.g. section 3.1 of `McDonald et al (2026)
<https://ui.adsabs.harvard.edu/abs/2026arXiv260202484M/abstract>`__ .)
Convolved maps in the ROSAT (0.5-2.0 keV) band adopt the effective
area information from the publicly available `ROSAT on-axis response
function
<https://heasarc.gsfc.nasa.gov/docs/rosat/ruh/handbook/node122.html\#tabeffarea>`__
. The maps in the eROSITA-high (2.3 - 8.0 keV band) and eROSITA-low
(0.2 - 2.3 keV) utilise the `survey-averaged eROSITA auxiliary
response files
<https://erosita.mpe.mpg.de/dr1/eSASS4DR1/eSASS4DR1_arfrmf/>`__,
specifically those for telescope model (TM) 8, which excludes TM5 and
TM7 as they suffer from light leakage (`Predehl et al (2021)
<https://arxiv.org/abs/2010.03477>`__.)


.. _smoothed-maps:

Smoothed maps
-------------

Gas particles in the FLAMINGO simulations have an associated SPH
smoothing length, so quantities derived from the gas can be smoothed
onto the HEALPix maps. When a gas particle crosses the lightcone its
angular smoothing length is computed as:

.. math::

   \theta_\text{h} = \arctan(h/r)

where :math:`h` is the particle's smoothing length and :math:`r` is
the distance from the observer at which the particle crossed the
lightcone. A gas particle with an angular smoothing length
:math:`\theta_\text{h}` will update all pixels within an angular
radius

.. math::

   \theta_\text{s}=\gamma\theta_\text{h}

where :math:`\gamma` is the number of smoothing lengths at which the
SPH kernel falls to zero. If :math:`\theta_\text{s}` is smaller than
the maximum angular radius of any HEALPix pixel then no smoothing is
done and the full contribution of the particle to the map is added to
a single pixel. Otherwise, we distribute the particle's contribution
over multiple pixels weighted by a 2D projected smoothing kernel.

The projected kernel is computed using equation 30 of `Price (2007)
<https://ui.adsabs.harvard.edu/abs/2007PASA...24..159P/abstract>`__:

.. math::

  F(q_{xy}) = \int_{-\sqrt{R^2-q^{2}_{xy}}}^{\sqrt{R^2-q^{2}_{xy}}} W(q) \mathrm{d}q_{z}

Here, :math:`q^2 = q^2_{xy} + q^2_{z}`, :math:`R = h\gamma` is the
radius where the SPH kernel reaches zero, and :math:`W(q)` is the
Wendland C2 kernel used in FLAMINGO's SPH implementation. The
contribution to the map from a particle is distributed between all
pixels with centres within an angular radius :math:`\theta_s` of the
particle, weighted by the projected kernel and normalized such that
the total contribution to the map is the same as in the un-smoothed case.
