Browsing the available data
===========================

Directory listings
------------------

This web interface can be used to browse the available files. Use the
`FLAMINGO data
<https://dataweb.cosma.dur.ac.uk:8443/flamingo/viewer.html?path=/FLAMINGO>`__
link on the left side of the page to view the FLAMINGO project root
directory. Each directory page contains links to any sub-directories
and files it contains.  You can navigate back to the parent directory
from a sub-directory by clicking on the parent directory name in the
path shown at the top of the page.

For example, `this page <viewer.html?path=FLAMINGO/L1_m9/L1_m9>`__
shows the available files for the fiducial ``L1_m9`` hydro simulation.

Full file downloads
-------------------

Clicking on a file on the directory listing page displays a page
describing the contents of the file and a link which can be used to
download the complete file.

Directory downloads
-------------------

Each directory listing page includes a link to download the directory and
its contents as a tar file. Note that these downloads can be extremely large!
Smaller downloads can be found by navigating to subdirectories. The service
does not attempt to limit download sizes since it's hard to know how much
network bandwidth, disk space and patience any particular user will have.

Paths in the tar files are set such that when unpacked they reproduce the
directory structure shown in the web interface. This is to help prevent
confusion when several simulations contain files with the same name. If
several tar files are downloaded it is recommended to untar them all in the
same directory.

File contents
-------------

Th web interface can display the contents of certain file types.

HDF5
^^^^

Clicking on a HDF5 file on the directory listing page will display
the internal structure of the file, showing groups, datasets and
attributes. The web interface is capable of displaying the contents
of some datasets and attributes, although compound data types and arrays
with more than two dimensions are not supported. This page also shows
how to open the file in python.

For example, you can see the contents of the z=0 SOAP halo catalogue
from the fiducial ``L1_m9`` simulation `here
<viewer.html?path=FLAMINGO/L1_m9/L1_m9/SOAP-HBT/halo_properties_0077.hdf5>`__.

Text
^^^^

Following a link to a text file on the directory listing page will download
and display the file in your browser.

Binary
^^^^^^

Other file types cannot be displayed. In this case just a download link is
provided.
