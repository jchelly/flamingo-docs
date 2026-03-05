Frequently Asked Questions
==========================

This page provides answers to common questions regarding the simulations and the data products.
It will updated to reflect new user inquiries and technical developments.

.. contents::
   :local:
   :backlinks: none

Data
----

.. _compression-filters:

What are the compression filters associated with the datasets?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We apply lossy compression filters to the data in the snapshots and SOAP catalogues to reduce the disk footprint. For floating-point values, this involves reducing precision (effectively rounding) to save space.

A list of the various filters can be found in the `Swift documentation <https://swift.strw.leidenuniv.nl/docs/ParameterFiles/lossy_filters.html>`__. The specific filter name used for any given dataset is stored within the HDF5 attributes of that dataset.

