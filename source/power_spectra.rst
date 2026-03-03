Power spectra
=============

Each simulation directory contains a HDF5 file named
``power_spectrum.hdf5``. This contains the total matter power spectrum
at 123 different redshifts. See `this page
<https://flamingo.strw.leidenuniv.nl/power_spectra.html>`__ for full
documentation.

The power spectrum files can be accessed remotely using the
:doc:`hdfstream </service_docs/python_module>` module or downloaded
and read directly with `h5py <https://www.h5py.org/>`__. The examples
below show how to do this.

.. note:: The power spectrum files are small enough that they're easy
          to download so there's no real need for remote access to
          their contents. The example here is presented to illustrate
          how to use the hdfstream module to read datasets without
          downloading the complete file.

.. tab-set::

   .. tab-item:: Reading a remote file

      .. code-block:: python

         import hdfstream
         import matplotlib.pyplot as plt
         import numpy as np

         fig, ax = plt.subplots(1)
         with hdfstream.open('cosma', 'FLAMINGO/L1_m9/L1_m9/power_spectrum.hdf5') as file:
             for z in [2, 0]:
                 k = file[f'z={z:.2f}/k'][:]
                 p = file[f'z={z:.2f}/P(k)'][:]
                 ax.plot(k, p, label=f'L1_m9 (z={z})')
             shot_noise = file['z=0.00'].attrs['Shot noise (Mpc**3)']
             ax.axhline(shot_noise, c='k', ls='--', label='Shot noise')
         ax.set_xlabel('Wavenumber $k$ [$\mathrm{Mpc}^{-1}$]')
         ax.set_ylabel('$P(k)$ [$\mathrm{Mpc}^{3}$]')
         ax.set_xscale('log')
         ax.set_yscale('log')
         ax.legend()
         plt.show()

   .. tab-item:: Reading a local file

      .. code-block:: python

         import h5py
         import matplotlib.pyplot as plt
         import numpy as np

         fig, ax = plt.subplots(1)
         with h5py.File('./FLAMINGO/L1_m9/L1_m9/power_spectrum.hdf5') as file:
             for z in [2, 0]:
                 k = file[f'z={z:.2f}/k'][:]
                 p = file[f'z={z:.2f}/P(k)'][:]
                 ax.plot(k, p, label=f'L1_m9 (z={z})')
             shot_noise = file['z=0.00'].attrs['Shot noise (Mpc**3)']
             ax.axhline(shot_noise, c='k', ls='--', label='Shot noise')
         ax.set_xlabel('Wavenumber $k$ [$\mathrm{Mpc}^{-1}$]')
         ax.set_ylabel('$P(k)$ [$\mathrm{Mpc}^{3}$]')
         ax.set_xscale('log')
         ax.set_yscale('log')
         ax.legend()
         plt.show()
