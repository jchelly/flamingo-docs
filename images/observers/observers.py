#!/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Cube side length
L = 2.8

# Cube vertices (0/1 combinations scaled by L)
vertices = np.array([[0,0,0],
                     [0,0,L],
                     [0,L,0],
                     [0,L,L],
                     [L,0,0],
                     [L,0,L],
                     [L,L,0],
                     [L,L,L]])

# Cube centre
centre = np.array([L/2, L/2, L/2])

# Observers halfway to each vertex
observers = (centre + vertices) / 2

# ---- Plot ----
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

# Draw cube edges
for v in vertices:
    # draw line from centre to vertex
    ax.plot([centre[0], v[0]],
            [centre[1], v[1]],
            [centre[2], v[2]],
            color='gray', linestyle='--', linewidth=0.8)

# Scatter cube vertices
#ax.scatter(vertices[:,0], vertices[:,1], vertices[:,2],
#           s=40, c='black', label="Vertices")

# Centre point
ax.scatter(centre[0], centre[1], centre[2],
           s=80, c='red', label="Centre")

# Observers
ax.scatter(observers[:,0], observers[:,1], observers[:,2],
           s=100, c='blue', marker='o', label="Observers")

# Cube bounding box
ax.set_xlim(0, L)
ax.set_ylim(0, L)
ax.set_zlim(0, L)

ax.set_xlabel('x [Gpc]')
ax.set_ylabel('y [Gpc]')
ax.set_zlabel('z [Gpc]')
ax.set_title("Observer positions in L2p8 boxes")

ax.legend()
ax.view_init(elev=20, azim=15)
plt.show()
