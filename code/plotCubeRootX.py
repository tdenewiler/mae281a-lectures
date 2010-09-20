#! /usr/bin/env python
from scipy import *
from pylab import *

saveplots = 1
xres = 0.001
x = arange(-1,5,xres)
y = x**(1./3.)
plot(x,y)
axis('equal')
xlabel(r'$x$')
ylabel(r'$f(x)$')
title(r'$f(x)=\sqrt{3}{x}$')

if saveplots:
    savefig("../images/plotCubeRootX.svg")
    savefig("../images/plotCubeRootX.png", dpi = 500)

show()
close()
