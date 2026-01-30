Integrated lightcones
=====================

This page describes the integrated healpix lightcones that have been produced in the analyses of the simulations.
In the construction of these maps, the FLAMINGO shells have been rotated whenever the lightcone diameter exceeds the
box size. The same rotation has been applied to the different observables, meaning the different integrated maps can 
be directly compared and cross correlated. The rotations that have been applied to the 1 cGpc (L1) or 2.8 cGpc (L2p8) variations are

.. code-block:: python

    import healpy as hp
    import lightcone_io.healpix_maps as hm
    import numpy as np
    import astropy.units as u

    angles_L1=np.array([[0., 0. ,3.26757547, 3.26757547, 3.26757547, 1.51289711, 1.51289711, 3.13885639, 3.13885639, 3.13885639, 2.17061318, 2.17061318, 2.17061318, 2.17061318, 4.59420579, 4.59420579, 4.59420579, 1.14273623, 1.14273623, 1.14273623, 1.14273623, 2.02717201, 2.02717201, 2.02717201, 2.02717201, 2.77675054, 2.77675054, 2.77675054, 2.77675054, 2.77675054, 0.83245259, 0.83245259, 0.83245259, 0.83245259, 0.83245259, 0.83245259, 4.95779263, 4.95779263, 4.95779263, 4.95779263, 4.95779263, 4.95779263, 4.95779263, 2.52359739, 2.52359739, 2.52359739, 2.52359739, 2.52359739, 2.52359739, 2.52359739, 2.52359739, 2.69301628, 2.69301628, 2.69301628, 2.69301628, 2.69301628, 2.69301628, 2.69301628, 2.69301628, 2.69301628], [0., 0., 1.41518902, 1.41518902,  1.41518902, 0.80580058, 0.80580058, 0.71830831, 0.71830831, 0.71830831, 1.77536892, 1.77536892, 1.77536892, 1.77536892, 0.62434822, 0.62434822, 0.62434822, 2.14076603, 2.14076603, 2.14076603, 2.14076603, 0.49840908, 0.49840908, 0.49840908, 0.49840908, 2.0136344, 2.0136344, 2.0136344 , 2.0136344, 2.0136344,  2.25356928, 2.25356928, 2.25356928 , 2.25356928 , 2.25356928,  2.25356928, 1.85187078, 1.85187078, 1.85187078, 1.85187078, 1.85187078, 1.85187078 , 1.85187078, 1.36014098, 1.36014098, 1.36014098, 1.36014098, 1.36014098, 1.36014098, 1.36014098, 1.36014098, 2.35895331, 2.35895331, 2.35895331, 2.35895331, 2.35895331, 2.35895331, 2.35895331, 2.35895331, 2.35895331]])

    angles_L2p8=np.array(([[0., 0., 0., 0., 0., 0., 0.,  2.11833333, 2.11833333, 2.11833333, 2.11833333, 2.11833333, 2.11833333, 2.11833333, 2.11833333, 2.11833333, 1.29070838, 1.29070838, 1.29070838, 1.29070838, 1.29070838, 1.29070838, 1.29070838, 1.29070838, 1.29070838, 1.29070838, 1.29070838, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 3.79736641, 3.79736641, 3.79736641, 3.79736641,  3.79736641, 3.79736641, 3.79736641, 3.79736641, 3.79736641, 3.79736641, 3.79736641, 3.79736641, 3.79736641, 3.79736641, 3.79736641, 3.79736641, 3.79736641, 3.79736641, 1.32878635, 1.32878635, 1.32878635, 1.32878635, 1.32878635, 1.32878635], [0., 0., 0., 0., 0., 0., 0., 0.96440001, 0.96440001, 0.96440001, 0.96440001, 0.96440001, 0.96440001, 0.96440001, 0.96440001, 0.96440001, 1.74841793, 1.74841793, 1.74841793, 1.74841793, 1.74841793, 1.74841793, 1.74841793, 1.74841793, 1.74841793, 1.74841793, 1.74841793, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 1.45462313, 1.45462313, 1.45462313, 1.45462313, 1.45462313, 1.45462313, 1.45462313, 1.45462313, 1.45462313, 1.45462313,  1.45462313, 1.45462313, 1.45462313, 1.45462313, 1.45462313, 1.45462313, 1.45462313, 1.45462313, 2.48706614, 2.48706614, 2.48706614, 2.48706614, 2.48706614, 2.48706614]]))

    path = f"/cosma8/data/dp004/flamingo/Runs/L1000N1800/L1_m9/neutrino_corrected_maps_downsampled_4096/" 
    shells = hm.ShellArray(f"{path}", "lightcone0")

    def rotate_map(hmap, rot_theta, rot_phi):
        longitude = rot_phi*180/np.pi * u.deg
        latitude = rot_theta*180/np.pi * u.deg
        rot_custom = hp.Rotator(rot=[longitude.to_value(u.deg), latitude.to_value(u.deg)], inv=True)
        hmap = rot_custom.rotate_map_alms(hmap)
        return hmap

    for i in range(shells.nr_shells):
        total_mass_shell = shells[i]["TotalMass"][:]
        rotated_total_mass_shell = rotate_map(total_mass_shell,angles_L1[0,i],angles_L1[1,i])

Weak lensing convergence maps
-----------------------------

The maps are constructed using the backward ray-tracing methodology
described in `Broxterman et al (2024)
<https://ui.adsabs.harvard.edu/abs/2024MNRAS.529.2309B%2F/abstract>`__, of which a 
later version of the code can be found `here
<https://github.com/JegerBroxterman/Lensing_raytrace_FLAMINGO>`__. At
each of the FLAMINGO mass shells, the rays are deflected according to
the gravitational potential. The files correspond to integrated weak
lensing convergence maps (:math:`\kappa`) that assume an non-tomographic Euclid-like
source redshift distribution and are saved as ring-ordered Healpix maps at
:math:`N_\mathrm{side} = 8192`. No smoothing or noise has been applied
to these files. The files can be read as


.. code-block:: python

    import h5py
    file_path = '/cosma8/data/dp004/dc-brox1/FLAMINGO_datarelease/WL_convergence_Euclid_like_nz_Broxterman24_L1_m9_lc0.hdf5'
    data_file = h5py.File(f"/{file_path}",'r')
    kappa_map = data_file["Convergence"][:]
    data_file.close()

where the part ``L1_m9_lc0`` changes between the variations and lightcones (lc), for example,
``L2p8_m9_DMO_lc4`` for observer four in the 2800 cGpc dark-matter-only box.

