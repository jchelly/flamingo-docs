#!/bin/env python
#
# Make rst tables of particle properties
#

import h5py


def rst_grid_table(headers, rows):
    """
    Function to generate an rst grid table

    headers - headers stored as a list of strings
    rows - rows stored as a list of lists of strings
    """
    # Add a bit of extra width to each column to allow some edits
    col_widths = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]

    # Add soem extra space for editting the description (e.g. adding :math:)
    col_widths[-1] += 20

    def format_row(row):
        return "| " + " | ".join(f"{str(cell):<{w}}" for cell, w in zip(row, col_widths)) + " |"

    def separator(char="-"):
        return f"+{char}" + f"{char}+{char}".join(char * w for w in col_widths) + f"{char}+"

    # Build the table
    lines = [separator("-"), format_row(headers), separator("=")]
    for row in rows:
        lines.append(format_row(row))
        lines.append(separator())
    return "\n".join(lines)

# Table column names
columns = ("Name", "Type", "Dimensions", "Description")

# Open a snapshot file
filename = "/cosma8/data/dp004/flamingo/Runs/L1000N1800/HYDRO_FIDUCIAL/snapshots/flamingo_0077/flamingo_0077.0.hdf5"
snap = h5py.File(filename, "r")

# Loop over particle types
for ptype in (0, 1, 4, 5, 6):

    # Open the group for this type
    group = snap[f"PartType{ptype}"]

    # List of table rows
    rows = []

    # Generate table rows
    for name in group:
        dset = group[name]
        rows.append([
            name,
            str(dset.dtype),
            ",".join(["N",]+[str(s) for s in dset.shape[1:]]),
            dset.attrs["Description"].decode()
        ])

    print(rst_grid_table(columns, rows))
