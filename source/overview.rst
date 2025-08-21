Service overview
----------------

This service provides web based remote access to collections of data
stored in HDF5 format on the COSMA system in Durham. Access is
possible at several levels of granularity:

  * Recursive download of a full directory (e.g. a complete simulation snapshot) in tar format
  * Download of individual files in HDF5 format
  * Access to HDF5 groups, datasets and attributes within a file via
    streaming in `messagepack <https://msgpack.org/index.html>`__
    format

A `python client module <viewer?page=python_module>`__ which
implements a similar interface to h5py is provided. This can be used
to `download dataset slices as numpy arrays <viewer?page=python_examples>`__,
for example.

The web interface can be used to browse the available files and their
contents. It also provides links for file and directory downloads and
the ability to preview the contents of HDF5 files.

Currently no authentication is required, although there is a (fairly
high) rate limit on requests.
