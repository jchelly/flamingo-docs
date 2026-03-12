Power spectra
=============

Each simulation directory contains a set of ASCII text files representing various power spectra and cross-spectra. These are available at 123 different redshifts, indexed from ``0000`` to ``0122``. The files follow the naming convention ``power_<type>_<index>.txt``. The following types of auto-spectra and cross-spectra are available:

* **Auto-spectra**:
    * ``matter``: Total matter
    * ``cdm``: Cold Dark Matter (CDM)
    * ``gas``: Gas
    * ``starBH``: Stars and Black Holes
    * ``pressure``: Electron pressure

* **Cross-spectra**:
    * ``cdm-gas``: CDM and gas
    * ``cdm-neutrino``: CDM and neutrinos
    * ``cdm-starBH``: CDM and stars/Black Holes
    * ``gas-matter``: Gas and total matter
    * ``gas-neutrino``: Gas and neutrinos
    * ``gas-starBH``: Gas and stars/Black Holes
    * ``matter-pressure``: Total matter and electron pressure
    * ``starBH-neutrino``: Stars/Black Holes and neutrinos
    * ``neutrino0-neutrino1``: Cross-correlation between the two neutrino particle realisations (used for shot-noise suppression)

The power spectra do contain some small artifacts (such as the small peak in the middle of the z=2 line if you run the example below for the L1_m9 outputs) which are due to combining foldings, and are not real.

TODO: Add link to some files

The files are stored as plain text with a descriptive header. The data is organized into three space-separated columns:

  * ``Column (0) - Redshift (z)``: The redshift of the output.
  * ``Column (1) - Wavenumber (k)``: The wavenumber in units of :math:`\mathrm{Mpc}^{-1}` (note that there is **no** factor of *h*).
  * ``Column (2) - Power (P(k))``: The shot-noise subtracted power in units of :math:`\mathrm{Mpc}^{3}`.

The example below shows how to load two files and plot the results.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt

   fig, ax = plt.subplots(1)

   # Loading the matter power spectrum at z=2 and z=0
   for filename in ['power_matter_0082.txt', 'power_matter_0122.txt']:

       # Load the data (skipping the header automatically)
       data = np.loadtxt(filename)

       # Extract columns
       z = data[0, 0]   # Redshift is the same for all rows in a single file
       k = data[:, 1]   # Fourier scale k [Mpc^-1]
       pk = data[:, 2]  # Power P(k) [Mpc^3]

       # Plot the power spectrum
       ax.plot(k, pk, label=f'z = {z:.2f}')

   ax.set_xlabel(r'$k$ [$\mathrm{Mpc}^{-1}$]')
   ax.set_ylabel(r'$P(k)$ [$\mathrm{Mpc}^{3}$]')
   ax.loglog()
   ax.legend()

   plt.show()

Baryonic response emulator
--------------------------

A Gaussian process emulator to model the effect of baryons on the matter power spectrum for all the simulations varying feedback in the FLAMINGO suite has been developed as part of `Schaller et al. (2025)
<https://ui.adsabs.harvard.edu/abs/2025MNRAS.539.1337S/abstract>`__. It is available via PyPI index ( ``pip install FlamingoBaryonResponseEmulator`` ) or `from github
<https://github.com/FLAMINGOSIM/FlamingoBaryonResponseEmulator>`__, where examples are also available.

The emulator can be used to predict the deviation of the matter power spectrum for the hydrodynamical simulation from the corresponding dark matter only simulation due to baryon and galaxy formation physics. The response as a function of wavenumber k is returned by the emulator as a function of redshift and three parameters characterizing the galaxy and cluster properties in the simulations. These are (i) the offset in the gas fraction in clusters from the Xray-based data used for the calibration of the simulations, (ii) the offset in the galaxy masses from the stellar mass function data used for the calibration, and (iii) the fraction of the AGN feedback taking place in the form of collimated jets as opposed to thermally-driven winds. The emulator is accurate to better than 1% for redshifts lower than 2 and for comoving scales up to k=10h/Mpc. Evaluation of the response for a given model is fast (1ms on 1 CPU core). 
