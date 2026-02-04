Directory layout
================

The simulations are divided into subdirectories based on their box
size and mass resolution. For example, the directory `/FLAMINGO/L1_m9
</flamingo/viewer.html?path=/FLAMINGO/L1_m9>`__ contains all
simulations run in a 1Gpc box at ``m9`` resolution. Within each
simulation directory there are subdirectories for the available data
products: :doc:`snapshots </snapshots/index>`, :doc:`halo catalogues
</soap/index>` and :doc:`lightcone outputs </lightcones/index>`.

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

