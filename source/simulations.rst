Simulations
===========

This page lists the available FLAMINGO simulations and provides a link
to the data for each one. For additional information see also the
`list of simulations
<https://flamingo.strw.leidenuniv.nl/simulations.html>`__ on the
`FLAMINGO project web site <https://flamingo.strw.leidenuniv.nl>`__ at
Leiden Observatory.

Naming conventions
------------------

Box size
^^^^^^^^

Where the name of a simulation starts with ``LX_mY``, the value of ``X``
indicates the box size in comoving Gpc. All simulations without this
prefix were run in a 1Gpc box.

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Label
     - Box side length (comoving Gpc)
   * - ``L1``
     - 1.0
   * - ``L2p8``
     - 2.8
   * - ``L5p6``
     - 5.6
   * - ``L11p2``
     - 11.2

Mass resolution
^^^^^^^^^^^^^^^

Where the name of a simulation starts with ``LX_mY``, the value of the
integer ``Y`` indicates the mass resolution of the simulation. It is
approximately equal to :math:`\log_{10}(m_{\mathrm{gas}})`, where
:math:`m_{\mathrm{gas}}` is the gas particle mass. All simulations
with no resolution specifier in their name were run at ``m9``
resolution.

.. note:: The exact particle masses vary slightly with the cosmology
          used in each simulation (see `this table
          <https://flamingo.strw.leidenuniv.nl/simulations.html>`__),
          and CDM particles in dark matter only runs have larger
          masses to account for the baryons. The values below are for
          hydro runs using the fiducial FLAMINGO cosmology.

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Label
     - Gas particle mass (:math:`\mathrm{M_{\odot}}`)
     - CDM particle mass (:math:`\mathrm{M_{\odot}}`)
   * - ``m8``
     - :math:`1.34 \times 10^8`
     - :math:`7.06 \times 10^8`
   * - ``m9``
     - :math:`1.07 \times 10^9`
     - :math:`5.65 \times 10^9`
   * - ``m10``
     - :math:`8.56 \times 10^9`
     - :math:`4.52 \times 10^{10}`

Model variations
^^^^^^^^^^^^^^^^

Simulations with names which do not start with the ``LX_mY`` prefix
are model variations run in 1Gpc boxes at the fiducial ``m9``
resolution.

Dark matter only models
^^^^^^^^^^^^^^^^^^^^^^^

Dark matter only models are indicated with a ``_DMO`` suffix. For
example, the dark matter only 1Gpc box at ``m9`` resolution is
``L1_m9_DMO``.

Directory layout
----------------

The simulations are divided into subdirectories based on their box
size and mass resolution. For example, the directory `/FLAMINGO/L1_m9
</flamingo/viewer.html?path=/FLAMINGO/L1_m9>`__ contains all
simulations run in a 1Gpc box at ``m9`` resolution. Within each
simulation directory there are subdirectories for the available data
products: :doc:`snapshots <snapshots/index>`, :doc:`halo catalogues
<soap/index>` and :doc:`lightcone outputs <lightcones/index>`.

.. mermaid::

   flowchart LR
     flamingo["`**Project root**
     FLAMINGO/`"]

     flamingo --> L1_m8["`**High res. 1Gpc**
     L1_m8/`"]
     L1_m8-->L1_m8_fiducial["`**Fiducial model**
     L1_m8/`"]
     L1_m8-->L1_m8_dmo["`**DMO model**
     L1_m8_DMO/`"]

     flamingo --> L1_m9["`**Fiducial res. 1Gpc**
     L1_m9/`"]
     L1_m9-->L1_m9_fiducial["`**Fiducial model**
     L1_m9/`"]
     L1_m9-->L1_m9_dmo["`**DMO model**
     L1_m9_DMO/`"]

     L1_m9-->L1_m9_variations["`**Model variations**
     fgas+2sigma/
     fgas-2sigma/
     ...`"]

     flamingo --> others["`**Other boxes**
     L1_m10/
     L2p8_m9/
     ...`"]


Hydrodynamical simulations
--------------------------

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Name
     - Description
   * - `L1_m9 </flamingo/viewer.html?path=/FLAMINGO/L1_m9/L1_m9>`__
     - Fiducial model
