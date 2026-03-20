HBT-HERONS merger trees
=======================

Full merger trees are provided in the form of HBT outputs.

link to website

The HBT-HERONS source code is available at `on github
<https://github.com/SWIFTSIM/HBT-HERONS>`__ and the exact git revision which
was used to generate a subhalo catalogue can be found by inspecting the
``git_hash`` attribute of the ``HEADER`` group in the HDF5 output file.

can be linked to soap catalogues using the Track id field, as shown in the example below
property list

.. list-table::
   :header-rows: 1

   * - Name
     - Description
     - Units
   * - ``Nbound``
     - The total number of particles bound to the subhalo.
     - :math:`-`
   * - ``Mbound``
     - The total mass of particles bound to the subhalo.
     - :math:`10^{10} \mathrm{M}_\odot`
   * - ``NboundType``
     - The total number of particles bound to the subhalo, classifed according to their particle type.
     - :math:`-`
   * - ``MboundType``
     - The total mass of particles bound to the subhalo, classifed according to their particle type.
     - :math:`10^{10} \mathrm{M}_\odot`
   * - ``VmaxPhysical``
     - The maximum value of the circularised rotation curve of the subhalo. The centre of the aperture used to compute this quantity corresponds to ``ComovingMostBoundPosition``
     - :math:`\mathrm{km/s}`
   * - ``BoundM200Crit``
     - Mass of a region with a spherical overdensity of 200 times the critical density of the universe. Only bound mass is included and only for centrals. The centre of the aperture used to compute this quantity corresponds to ``ComovingMostBoundPosition``
     - :math:`10^{10} \mathrm{M}_\odot`
   * - ``RmaxComoving``
     - The radius at which the circularised rotation curve of the subhalo reaches its maximum value (``VmaxPhysical``). The centre of the aperture used to compute this quantity corresponds to ``ComovingMostBoundPosition``
     - :math:`a\mathrm{Mpc}`
   * - ``RHalfComoving``
     - The smallest radius that encloses 50% of the total bound mass. The centre of the aperture used to compute this quantity corresponds to ``ComovingMostBoundPosition``
     - :math:`a\mathrm{Mpc}`
   * - ``REncloseComoving``
     - The smallest radius that encloses 100% of the total bound mass. Useful when interested in doing spatial masking. The centre of the aperture used to compute this quantity corresponds to ``ComovingMostBoundPosition``
     - :math:`a\mathrm{Mpc}`
   * - ``BoundR200CritComoving``
     - The radius of a sphere enclosing a mean density that is 200 times the critical density of the Universe. Only bound mass is included and it is only computed for centrals. The centre of the aperture used to compute this quantity corresponds to ``ComovingMostBoundPosition``
     - :math:`a\mathrm{Mpc}`
   * - ``ComovingAveragePosition``
     - Mass-weighted average position of all bound particles.
     - :math:`a\mathrm{Mpc}`
   * - ``PhysicalAverageVelocity``
     - Mass-weighted average velocity of all bound particles.
     - :math:`\mathrm{km/s}`
   * - ``ComovingMostBoundPosition``
     - Position of the most bound particle.
     - :math:`a\mathrm{Mpc}`
   * - ``PhysicalMostBoundVelocity``
     - Velocity of the most bound particle.
     - :math:`\mathrm{km/s}`
   * - ``InertialTensor``
     - Flattened representation of the inertia tensor of the subhalo.
     - :math:`a^2\mathrm{Mpc}^2`
   * - ``InertialTensorWeighted``
     - Flattened representation of the inertia tensor of the subhalo, weighted by particle mass and 3D distance to ``ComovingMostBoundPosition``
     - :math:`-`
   * - ``SpecificSelfPotentialEnergy``
     - Mass-weighted average potential energy of bound particles.
     - :math:`\mathrm{km^2/s^2}`
   * - ``SpecificSelfKineticEnergy``
     - Mass-weighted average kinetic energy of bound particles in the centre of mass reference frame of the subhalo.
     - :math:`\mathrm{km^2/s^2}`
   * - ``SpecificAngularMomentum``
     - Mass-weighted average angular momentum of bound particles in the centre of mass reference frame of the subhalo.
     - :math:`\mathrm{km/s}`
   * - ``TracerIndex``
     - Bound ranking of the most bound tracer particle.
     - :math:`-`
   * - ``MostBoundParticleId``
     - ID of the most bound particle.
     - :math:`-`
   * - ``SnapshotIndexOfBirth``
     - The output when the subhalo was first identified.
     - :math:`-`
   * - ``SnapshotIndexOfSink``
     - If the subhalo has [sunk](../outputs/merger_trees.md/#subhalo-sinking), the output when that happened. If it has not sunk, it equals -1.
     - :math:`-`
   * - ``SnapshotIndexOfDeath``
     - If the subhalo has sunk or disrupted, the output when that happened. If neither has happened, it equals -1.
     - :math:`-`
   * - ``SnapshotIndexOfLastIsolation``
     - If the subhalo has ever been a satellite, the output before it ever became a satellite for the first time. If it has always been a central subhalo, it equals -1.
     - :math:`-`
   * - ``SnapshotIndexOfLastMaxVmax``
     - The output when the subhalo reached its maximum value of VmaxPhysical.
     - :math:`-`
   * - ``SnapshotIndexOfLastMaxMass``
     - The output when the subhalo reached its maximum value of M
     - :math:`-`
   * - ``LastMaxMass``
     - The maximum mass that the subhalo has reached so far.
     - :math:`10^{10} \mathrm{M}_\odot`
   * - ``LastMaxVmaxPhysical``
     - The maximum VmaxPhysical that the subhalo has reached so far.
     - :math:`\mathrm{km/s}`
   * - ``TrackId``
     - Unique identifier for the subhalo, which persists across time.
     - :math:`-`
   * - ``SinkTrackId``
     - If the subhalo has sunk, the ``TrackId`` of the subhalo that accreted it. If it has not happened, it equals -1.
     - :math:`-`
   * - ``DescendantTrackId``
     - If the subhalo has sunk or disrupted, the ``TrackId`` of the subhalo that accreted its most bound particles. If neither has happened, it equals -1.
     - :math:`-`
   * - ``NestedParentTrackId``
     - The ``TrackId`` of the parent subhalo. Central subhaloes have -1.
     - :math:`-`
   * - ``HostHaloId``
     - The Friends of Friends group that this subhalo is a part of.
     - :math:`-`
   * - ``Rank``
     - The mass ranking of the subhalo compared to all of the subhaloes that have the same ``HostHaloId``
     - :math:`-`
   * - ``Depth``
     - The number of hierarchical connections that the subhalo is away from the central, e.g. 0 for centrals, 1 for satellites, 2 for satellites of satellites.
     - :math:`-`

.. warning:: Since the HBT-HERONS definition of spherical overdensity is based on the 
             enclosed mass of bound particles only, it does not follow the common convention in the 
             literature, which includes the mass contribution of all particles. The values
             in the SOAP catalogues should be used instead.

These are sorted HBT catalogues

TODO: Update and test once HBT files are served

Matching example
----------------

.. code-block:: python


    # Simulations to match between
    sim1 = "L1000N1800/DMO_FIDUCIAL"
    sim2 = "L1000N1800/HYDRO_FIDUCIAL"
    snap_nr = 77

    # Load SOAP catalogues
    base_dir = "/cosma8/data/dp004/flamingo/Runs/"
    soap1 = sw.load(f"{base_dir}/{sim1}/SOAP-HBT/halo_properties_{snap_nr:04}.hdf5")
    soap2 = sw.load(f"{base_dir}/{sim2}/SOAP-HBT/halo_properties_{snap_nr:04}.hdf5")

    # Load matching file
    match_dir = "/cosma8/data/dp004/dc-mcgi1/FLAMINGO/matching"
    match_filename = f"{match_dir}/match_{sim1.replace('/', '_')}_{sim2.replace('/', '_')}_{snap_nr:04}.hdf5"

    with h5py.File(match_filename, "r") as file:
        match_index = file["MatchIndex1to2"][:]
        consistent = file["Consistent1to2"][:] == 1

    # Load the mass of the matched halos
    mass_1 = soap1.spherical_overdensity_200_crit.total_mass[consistent]
    mass_2 = soap2.spherical_overdensity_200_crit.total_mass[match_index[consistent]]

    # Plot
    fig, ax = plt.subplots(figsize=(7, 6))
    bins = np.logspace(8, 15, 100)

    h = ax.hist2d(
        mass_1.to_physical_value('Msun'),
        mass_2.to_physical_value('Msun'),
        bins=bins,
        norm="log",
    )
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(f"M200c in {sim1} [$M_\\odot$]")
    ax.set_ylabel(f"M200c in {sim2} [$M_\\odot$]")
    
    cbar = fig.colorbar(h[3], ax=ax)
    cbar.set_label('N_halo')
    
    plt.savefig(f"compare_mbound_{sim1.replace('/', '_')}.png", dpi=200)
    plt.close()

    import h5py
    import matplotlib.pyplot as plt
    import numpy as np
    import swiftsimio as sw

    # Connect to the hdfstream service and open the root directory
    root_dir = hdfstream.open("cosma", "/")

    # Load the z=0 SOAP catalogue from the L1_m9 simulation
    final_snap_nr = 77
    soap = sw.load(root_dir[f"FLAMINGO/L1_m9/L1_m9/SOAP-HBT/halo_properties_{final_snap_nr:04}.hdf5"])

    # Pick the most massive satellite which has lost at least 70% of its mass
    mask = soap.input_halos.is_central.value == 0
    last_max_mass_msun = soap.input_halos_hbtplus.last_max_mass.to_physical_value('Msun')
    bound_mass_msun = soap.bound_subhalo.total_mass.to_physical_value('Msun')
    mask &= (bound_mass_msun / last_max_mass_msun) < 0.3
    i = np.argmax(np.where(mask, bound_mass_msun, 0))

    # Get the TrackId of the object we have selected
    track_id = soap.input_halos_hbtplus.track_id[i].value

    # Get the first snapshot this object appeared
    birth_snap_nr = soap.input_halos_hbtplus.snapshot_index_of_birth[i].value

    # Create an array to hold the evolution
    n_exist = final_snap_nr - birth_snap_nr + 1
    mass_evolution_msun = np.zeros((n_exist, 6))
    scale_factor = np.zeros(n_exist)

    # Loop through the catalogues and extract the mass for this object
    hbt_basename = f"FLAMINGO/L1_m9/L1_m9/sorted_hbt/OrderedSubSnap_{{snap_nr:03}}.hdf5"
    for i in range(n_exist):
        hbt_filename = hbt_basename.format(snap_nr=birth_snap_nr+i)
        with hdfstream.open('cosma', hbt_filename) as file:
            # Mass is stored in units of 10^10 Msun
            mass_evolution_msun[i] = file["Subhalos/MboundType"][track_id] * 10 ** 10
            scale_factor[i] = file['Cosmology']['ScaleFactor'][0]

    # Plot the results
    fig, ax = plt.subplots(1)
    ax.plot(scale_factor, mass_evolution_msun[:, 1], label='Dark matter', color='k')
    ax.plot(scale_factor, mass_evolution_msun[:, 0], label='Gas', color='tab:green')
    ax.plot(scale_factor, mass_evolution_msun[:, 4], label='Stars', color='tab:orange')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('Scale factor')
    ax.set_ylabel('Bound mass [Msun]')
    ax.legend()
    plt.savefig('hbt_example.png')
    plt.close()

