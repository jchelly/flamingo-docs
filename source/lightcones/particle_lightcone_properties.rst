Particle properties in the particle lightcones
==============================================

This page documents all of the properties which are stored for each
type of particle in the FLAMINGO lightcone particle outputs.

In the Units column in the tables below we use :math:`a` to indicate
the expansion factor. Comoving megaparsecs are expressed as
:math:`a\mathrm{Mpc}`. In the Shape column, N indicates the number of
particles in the dataset.

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Name
     - Type
     - Shape
     - Units
     - Description
   * - ``Coordinates``
     - float64
     - N,3
     - :math:`a\mathrm{Mpc}`
     - Co-moving positions of the particles
