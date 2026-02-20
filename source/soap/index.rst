Halo catalogues
=================

At each snapshot output by the simulation, bound objects are identified by grouping
particles based on their spatial and dynamical properties. There are multiple
methods for doing this, but within the
FLAMINGO simulations structure is identified
using the HBT-HERONS subhalo finder
`(Forouhar Moreno et al. 2025). <https://ui.adsabs.harvard.edu/abs/2025MNRAS.543.1339F>`__

Once the centres of subhalos and the particles bound to each one have
been identified, they are passed to the SOAP code
`(McGibbon et al. 2025). <https://ui.adsabs.harvard.edu/abs/2025JOSS...10.8252M>`__.
This outputs catalogues containing a large number of properties for different
halo/galaxy definitions, as described within the following pages.

.. toctree::
   :maxdepth: 1

   directory_layout
   particle_selection
   property_filters
   property_table
   membership_files

TODO: Remove membership files from the list above?

.. note:: Within the cosmological simulation community people refer to both
          "halos" and "subhalos", occasionally in an inconsistent manner.
          Within FLAMINGO a halo corresponds to an overdensity of particles, originally found using the 3D FoF algorithm. Each halo contains one or more
          subhalos, which are a self-bound collection of particles identified by
          HBT-HERONS. Subhalos can be either centrals (each halo has a single central subhalo,
          and the halo centre is defined as the most bound particle position of its central 
          subhalo), or satellites.

