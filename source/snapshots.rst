Snapshots
=========

Each FLAMINGO simulation models the evolution of a cubic volume of the
Universe from just after the big bang to the present day. The state of
the simulation is output at intervals as a series of "snapshots",
which record the distribution of particles in the simulated volume at
an instant in time.

Snapshots contain multiple particle types which model different matter
components: the dark matter only simulations contain particles
representing the distribution of dark matter and neutrinos. The hydro
simulations also include particles representing gas, stars and black
holes. Many physical properties, such as position, mass and velocity,
are stored for each particle.

.. card-carousel:: 2

    .. card:: L1_m8 gas temperature at z=0

        .. image:: _static/images/L1_m8_snapshots/L1_m8_gas_temp_z0.jpg

    .. card:: L1_m8 DM velocity dispersion at z=0

        .. image:: _static/images/L1_m8_snapshots/L1_m8_dm_veldisp_z0.jpg

    .. card:: L1_m8 stellar mass at z=0

        .. image:: _static/images/L1_m8_snapshots/L1_m8_stellar_mass_z0.jpg

The following sections describe the layout and contents of the snapshots.

.. toctree::
   :maxdepth: 2

   Directory layout <snapshot_dirs>
   File format <snapshot_format>
   Output redshifts <snapshot_redshifts>
   Particle properties <snapshot_particle_properties>

For more information about the SWIFT simulation snapshot format used
here, see the `SWIFT documentation
<https://swift.strw.leidenuniv.nl/docs/Snapshots/index.html>`__.
