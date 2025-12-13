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
shows the available data for the fiducial ``L1_m9`` hydro simulation.

.. image:: L1_m9_directory.png
   :class: screenshot
   :alt: screenshot of a directory listing

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

Full file downloads
-------------------

Clicking on a file on the directory listing page displays the contents
of the file and a link which can be used to download it.

.. image:: L1_m9_soap.png
   :class: screenshot
   :alt: screenshot showing the contents of a SOAP halo catalogue

The web interface can display the contents of HDF5 and text files. If
a file cannot be displayed, only a download link is provided.
