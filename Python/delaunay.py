import numpy
from mayavi import mlab

X2 = numpy.array([0, 0, 1, 1])
Y2 = numpy.array([0.5, 0.45, 1, 0.5])
Z2 = numpy.array([0, 1, 0.5,0])

fig = mlab.figure(1, bgcolor=(1, 1, 1), fgcolor=(0.5, 0.5, 0.5))
# Define the points in 3D space
# including color code based on Z coordinate.
pts = mlab.points3d(X2, Y2, Z2, Y2, colormap='jet')
# Triangulate based on X, Y with Delaunay 2D algorithm.
# Save resulting triangulation.
mesh = mlab.pipeline.delaunay2d(pts)
# Remove the point representation from the plot
pts.remove()
# Draw a surface based on the triangulation
surf = mlab.pipeline.surface(mesh, colormap='jet')

# Simple plot.
mlab.outline(extent=(0,1,0,1,0,1))
mlab.axes(extent=(0,1,0,1,0,1))
mlab.show()
