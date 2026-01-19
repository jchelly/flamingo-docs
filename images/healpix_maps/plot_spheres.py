# Source - https://stackoverflow.com/a
# Posted by Andras Deak -- Слава Україні, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-16, License - CC BY-SA 4.0

import numpy as np
from mayavi import mlab
from tvtk.api import tvtk # python wrappers for the C++ vtk ecosystem


def rotated_normal(angle_deg):
    theta = np.radians(angle_deg)
    return (np.cos(theta), np.sin(theta), 0)


def auto_sphere():
    # create a figure window (and scene)
    fig = mlab.figure(size=(600, 600))

    for shell_nr, radius, angle in (
            (0, 0.5, 180.0),
            (1, 0.7, 250.0),
            (2, 0.9, 300.0),
            (3, 1.1, 120.0),
            ):

        # load and map the texture
        img = tvtk.PNGReader()
        img.file_name = f'./images/shell_{shell_nr}.png'
        texture = tvtk.Texture(input_connection=img.output_port, interpolate=1)
        # (interpolate for a less raster appearance when zoomed in)

        # use a TexturedSphereSource, a.k.a. getting our hands dirty
        R = 1
        Nrad = 180

        # create the sphere source with a given radius and angular resolution
        sphere = tvtk.TexturedSphereSource(radius=radius, theta_resolution=Nrad,
                                           phi_resolution=Nrad)

        # Clip the sphere
        clipper = tvtk.ClipPolyData(
            input_connection=sphere.output_port,
            clip_function=tvtk.Plane(normal=rotated_normal(angle), origin=(0, 0, 0)),
        )

        # assemble rest of the pipeline, assign texture
        sphere_mapper = tvtk.PolyDataMapper(input_connection=clipper.output_port)
        sphere_actor = tvtk.Actor(mapper=sphere_mapper, texture=texture)
        fig.scene.add_actor(sphere_actor)


if __name__ == "__main__":
    auto_sphere()
    mlab.show()
