from pylab import plot,show
from numpy import loadtxt,size,linspace, arange, array
from math import *

data = loadtxt("millikan.txt",float)
x = data[:,0]
y = data[:,1]
N = size(x)
Ex = sum(x)/N
Ey = sum(y)/N
Exx = sum(x**2)/N
Exy = sum(x*y)/N
m = (Exy - Ex * Ey)/(Exx - Ex**2)
c = (Exx * Ey - Ex * Exy)/(Exx - Ex**2)
print "Ex = ", Ex, "Ey = ", Ey
print "Exx = ", Exx, "Exy = ", Exy
print "m=",m,", c=",c
#xp = linspace(0.5e15,1.3e15,1e14)
xp = arange(5e14, 13e14, 1e14)
xp = array(xp)
yp = array(m * xp + c)

h = m * (1.602 * 10**(-19))
print "h = ", h

# plot(x,y,"k.")
# plot(xp,yp,"k-")
# show()

# the exact Planck's constant is 6.626176 x 10-34
# m= 4.08822735852e-15 , c= -1.73123580398
# computed h = 6.54934022835e-34
