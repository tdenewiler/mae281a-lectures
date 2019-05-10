#! /usr/bin/env python
# coding: utf-8
"""Plot the function $f(x) = sqrt{3}{x}$."""

from __future__ import division
import numpy as np
import matplotlib # pylint: disable=import-error
matplotlib.use('Qt4Agg') # For use over SSH.
import matplotlib.pyplot as plt # pylint: disable=import-error,wrong-import-position

class CustomPlotter():
    """Plot custom function."""

    def __init__(self):
        """Plot function."""
        self.saveplots = True
        self.dpi = 100
        xres = 0.001

        x, y = self.generate_data(xres)
        self.show_plots(x, y)

    @classmethod
    def generate_data(cls, xres):
        """Generate data for function."""
        x = np.arange(-1, 5, xres)
        y = x**(1/3)

        return x, y

    def show_plots(self, x, y):
        """Show and save plots."""
        plt.plot(x, y)
        plt.axis('equal')
        plt.xlabel(r'$x$')
        plt.ylabel(r'$f(x)$')
        plt.title(r'$f(x)=\sqrt{3}{x}$')

        if self.saveplots:
            plt.savefig("../images/plotCubeRootX.svg")
            plt.savefig("../images/plotCubeRootX.png", dpi=self.dpi)

        plt.show()
        plt.close()

if __name__ == '__main__':
    CustomPlotter()
