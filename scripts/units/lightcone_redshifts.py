#!/bin/env python

import hdfstream
import numpy as np

table_header = """\
.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Name
     - Lightcone nr.
     - Gas max :math:`z`
     - DM max :math:`z`
     - stars max :math:`z`
     - BH max :math:`z`
     - Neutrino max :math:`z`"""

row_template = """\
   * - ``{name}``
     - {lightcone_nr}
     - {max_z_gas}
     - {max_z_dm}
     - {max_z_stars}
     - {max_z_bh}
     - {max_z_nu}"""

root = hdfstream.open("flamingo","/")

print(table_header)

for name in root["FLAMINGO/L1_m9"]:

    # Skip metadata files
    if name in ("description.md", "labels.msgpack"):
        continue

    # Skip DMOs for now
    if name.endswith("_DMO"):
        continue

    # Read parameters from one of the files
    attrs = {}
    nr_lightcones = 0
    for lightcone_nr in range(8):
        try:
            # Determine what particle types exist for this lightcone
            index = root[f"FLAMINGO/L1_m9/{name}/particle_lightcones/lightcone{lightcone_nr}_particles/lightcone{lightcone_nr}_0000.0.hdf5"]
            attrs[lightcone_nr] = dict(index["Lightcone"].attrs)
            max_z = {}
            for ptype in ("Gas", "DM", "Stars", "BH", "Neutrino"):
                if ptype in index:
                    max_z[ptype] = float(attrs[lightcone_nr][f"maximum_redshift_{ptype}"][0])
                else:
                    max_z[ptype] = "-"
            print(row_template.format(name=name,
                                      lightcone_nr=lightcone_nr,
                                      max_z_gas=max_z["Gas"],
                                      max_z_dm=max_z["DM"],
                                      max_z_stars=max_z["Stars"],
                                      max_z_bh=max_z["BH"],
                                      max_z_nu=max_z["Neutrino"],))
            nr_lightcones = lightcone_nr+1
        except KeyError:
            continue
