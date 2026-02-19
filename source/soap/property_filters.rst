SOAP property filters
---------------------

For certain properties it only makes sense to compute them if a subhalo 
contains sufficient
particles. HBT-HERONS was run with a configuration that requires each
subhalo to have at least 20 particles. However, even for those
particle numbers, a lot of the properties computed by SOAP will be zero
(e.g. the gas mass within a 10 kpc aperture), or have values that are
outliers compared to the full halo population because of undersampling.
We can save a lot of disk space by filtering these out by applying
appropriate cuts. Filtering means setting the value of the property to
zero, and HDF5 file compression then very effectively reduces the data
storage required to store these properties, while the size of the arrays
that the end user sees remains unchanged. We also save on
computing time by not computing properties that are filtered out.

Since different properties can have very different requirements,
filtering is done in categories, where each category corresponds to a
set of quantities that are filtered using the same criterion.

**Basic quantities (basic)** are never filtered out, and hence are calculated for all objects in the
input subhalo catalogue.

**General quantities (general)** use a filter based on the total number of particles bound to the
subhalo.

**Gas quantities (gas)** use a filter based on the number of gas particles bound to the subhalo.

**DM quantities (dm)** use a filter based on the number of DM particles bound to the subhalo.

**Stellar quantities (star)** use a filter based on the number of star particles bound to the subhalo.

**Baryon quantities (baryon)** use a filter based on the number of gas and star particles bound to the subhalo.

Note that there are no quantities that use a BH or neutrino particle
number filter.

The particle number thresholds are set in the parameter file. The
different categories are summarised in the table below.

+---------+-----------------------------------------------------------------------+
| Name    | Criterion                                                             |
+=========+=======================================================================+
| basic   | all subhalos                                                          |
+---------+-----------------------------------------------------------------------+
| general | :math:`N_{\rm{}gas}+N_{\rm{}dm}+N_{\rm{}star}+N_{\rm{}BH} \geq{} 100` |
+---------+-----------------------------------------------------------------------+
| gas     | :math:`N_{\rm{}gas} \geq{} 100`                                       |
+---------+-----------------------------------------------------------------------+
| dm      | :math:`N_{\rm{}dm} \geq{} 100`                                        |
+---------+-----------------------------------------------------------------------+
| star    | :math:`N_{\rm{}star} \geq{} 100`                                      |
+---------+-----------------------------------------------------------------------+
| baryon  | :math:`N_{\rm{}gas}+N_{\rm{}star} \geq{} 100`                         |
+---------+-----------------------------------------------------------------------+

