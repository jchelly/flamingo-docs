Integrated lightcones
=====================

This page describes the integrated healpix lightcones that have been produced in the analyses of the simulations.

Weak lensing convergence maps
-----------------------------

The maps are constructed using the backward ray-tracing methodology
described in `Broxterman et al (2024)
<https://ui.adsabs.harvard.edu/abs/2024MNRAS.529.2309B%2F/abstract>`__. At
each of the FLAMINGO mass shells, the rays are deflected according to
the gravitational potential. The files correspond to integrated weak
lensing convergence maps that assume an non-tomographic Euclid-like
n(z) and are saved as ring-ordered Healpix maps at
:math:`N_\mathrm{side} = 8192`. No smoothing or noise has been applied
to these files. The files can be read as


.. code-block:: python

    import h5py
    file_path = '/cosma8/data/dp004/dc-brox1/FLAMINGO_datarelease/WL_convergence_Euclid_like_nz_Broxterman24_L1_m9_lc0.hdf5'
    data_file = h5py.File(f"/{file_path}",'r')
    kappa_map = data_file["Convergence"][:]
    data_file.close()


