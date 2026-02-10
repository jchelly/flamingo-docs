#!/bin/env python

import numpy as np
import hdfstream
import simulation_list as sl

root = hdfstream.open("flamingo", "/FLAMINGO/")



checks = [
    # L1_m8 runs
    {
        "box"            : "L1_m8",
        "names"          : ["L1_m8", "L1_m8_DMO"],
        "nr_snaps"       : 79,
        "expected_snaps" : sl.L1_m8_snapshots
    },
    # L1_m10 runs
    {
       "box"            : "L1_m10",
       "names"          : ["L1_m10", "L1_m10_DMO"],
       "nr_snaps"       : 78,
       "expected_snaps" : sl.L1_m9_snapshots
    },
    # L2p8_m9 runs
    {
        "box"            : "L2p8_m9",
        "names"          : ["L2p8_m9", "L2p8_m9_DMO"],
        "nr_snaps"       : 79,
        "expected_snaps" : sl.L1_m8_snapshots
    },
    # L1_m9 hydro runs
    {
        "box"            : "L1_m9",
        "names"          : sl.L1_m9,
        "nr_snaps"       : 78,
        "expected_snaps" : sl.L1_m9_snapshots
    },
    # L1_m9 DMO runs
    {
        "box"            : "L1_m9",
        "names"          : sl.L1_m9_DMO,
        "nr_snaps"       : 78,
        "expected_snaps" : sl.L1_m9_snapshots
    },
    # L5p6_m10 runs
    {
        "box"            : "L5p6_m10",
        "names"          : ["L5p6_m10_DMO"],
        "nr_snaps"       : 79,
        "expected_snaps" : sl.L1_m8_snapshots
    },
    # L11p2_m11 runs
    {
        "box"            : "L11p2_m11",
        "names"          : ["L11p2_m11_DMO"],
        "nr_snaps"       : 79,
        "expected_snaps" : sl.L1_m8_snapshots
    },
]


for check in checks:

    box = check["box"]
    names = check["names"]
    nr_snaps = check["nr_snaps"]
    all_snaps = np.arange(nr_snaps, dtype=int)
    expected_snaps = np.sort(np.asarray(list(check["expected_snaps"].keys()), dtype=int))

    for name in names:

        dirname = name.replace("σ", "sigma").replace("*","star")
        print(dirname)

        try:
            snapshots_dir = root[f"{box}/{dirname}/snapshots"]
        except KeyError:
            print("  Directory not found")
            continue

        # Check which snapshots we have
        snaps_present = []
        for snap_nr in range(nr_snaps):
            filename = f"flamingo_{snap_nr:04d}/flamingo_{snap_nr:04d}.0.hdf5"
            try:
                snap_file = snapshots_dir[filename]
            except KeyError:
                pass
            else:
                snaps_present.append(snap_nr)

        snaps_found = np.sort(np.asarray(snaps_present))
        if (len(snaps_found) == len(all_snaps)) and np.all(snaps_found==all_snaps):
            print("  All snapshots present")
        elif (len(snaps_found) == len(expected_snaps)) and np.all(snaps_found==expected_snaps):
            print("  Expected subset of snapshots present")
        else:
            missing = 0
            for sn in expected_snaps:
                if sn not in snaps_found:
                    missing += 1
            if missing == 0:
                print("  Have extra snapshots")
            else:
                print("  MISSING SNAPSHOTS")
