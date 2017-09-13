from pylab import imshow, show, gray, colorbar, jet
from numpy import array, empty, ones
from math import *

points = 400
side = 4.0
spacing = 4.0/points
M = empty([points+1,points+1],float)

for ix in range(points+1):
    for iy in range(points+1):
        x = -2.0 + ix * spacing
        y = -2.0 + iy * spacing
        z = 0.0 + 0.0j
        count = 0
        while abs(z) <= 2.0:
            z = z**2 + x + y * 1j
            count = count + 1
            if count >= 400:
                # M[ix,iy] = 0;
                break
        M[ix,iy] = count

imshow(M, origin="lower", extent=[-2,2,-2,2], aspect=1)
# gray()
jet()
colorbar()
show()
