Property categories
-------------------

Halo properties only make sense if the subhalo contains sufficient
particles. Halo finders are often run with a configuration that requires
at least 20 particles for a satellite subhalo. However, even for those
particle numbers, a lot of the properties computed by SOAP will be zero
(e.g. the gas mass within a 10 kpc aperture), or have values that are
outliers compared to the full halo population because of undersampling.
We can save a lot of disk space by filtering these out by applying
appropriate cuts. Filtering means setting the value of the property to
``NaN``; HDF5 file compression then very effectively reduces the data
storage required to store these properties, while the size of the arrays
that the end user sees remains unchanged. Evidently, we can also save on
computing time by not computing properties that are filtered out.

Since different properties can have very different requirements,
filtering is done in categories, where each category corresponds to a
set of quantities that are filtered using the same criterion. Inclusive,
exclusive or projected quantities with different aperture radii (or
overdensity criteria) can be used to create profiles. In order for these
profiles to make sense, we have to apply a consistent cut across all the
different aperture radii (or overdensity criteria) for the same subhalo
property type. Or in other words: the quantities for an inclusive sphere
with a 10 kpc aperture radius will use the same filter mask as the
quantities of the inclusive sphere with a 3000 kpc aperture radius, even
though the latter by construction has many more particles.

Basic quantities (basic)
^^^^^^^^^^^^^^^^^^^^^^^^

are never filtered out, and hence are calculated for all objects in the
input halo catalogue.

General quantities (general)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

use a filter based on the total number of particles bound to the
subhalo.

Gas quantities (gas)
^^^^^^^^^^^^^^^^^^^^

use a filter based on the number of gas particles bound to the subhalo.

DM quantities (dm)
^^^^^^^^^^^^^^^^^^

use a filter based on the number of DM particles bound to the subhalo.

Stellar quantities (star)
^^^^^^^^^^^^^^^^^^^^^^^^^

use a filter based on the number of star particles bound to the subhalo.

Baryon quantities (baryon)
^^^^^^^^^^^^^^^^^^^^^^^^^^

use a filter based on the number of gas and star particles bound to the
subhalo.

Note that there are no quantities that use a BH or neutrino particle
number filter.

The particle number thresholds are set in the parameter file. The
different categories are summarised in the table below.

+---------+-----------------------------------------------------------------------+
| Name    | criterion                                                             |
+=========+=======================================================================+
| basic   | (all halos)                                                           |
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

