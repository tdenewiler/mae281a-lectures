#! /usr/bin/env python
from scipy import *
from pylab import *

saveplots = 1
xres = 0.001
x = arange(-1,5,xres)
y = sqrt(x)
plot(x,y)
axis('equal')
xlabel(r'$x$')
ylabel(r'$f(x)$')
title(r'$f(x)=\sqrt{x}$')

if saveplots:
    savefig("../images/plotSqrtX.svg")
    savefig("../images/plotSqrtX.png", dpi = 500)

show()
close()
