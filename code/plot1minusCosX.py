#! /usr/bin/env python
from scipy import *
from pylab import *

saveplots = 1
xres = 0.001
x = arange(-5,5,xres)
y = 1-cos(x)
yx0 = x*0 # Horizontal line for x-axis
yx1 = x*0+1 # Horizontal line for y=1
plot(x,y)
hold(True)
plot(x,yx0,'k',linewidth=0.5)
plot(x,yx1,'k',linewidth=0.5)
axis('equal')
xlabel(r'$x$')
ylabel(r'$f(x)$')
title(r'$f(x)=1-\cos(x)$')

if saveplots:
    savefig("../images/plot1minusCosX.svg")
    savefig("../images/plot1minusCosX.png", dpi = 500)

show()
close()
