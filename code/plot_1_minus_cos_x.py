#! /usr/bin/env python
# coding: utf-8
"""Plot the function $f(x) = 1 - cos(x)$."""

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

        x, y, yx0, yx1 = self.generate_data(xres)
        self.show_plots(x, y, yx0, yx1)

    @classmethod
    def generate_data(cls, xres):
        """Generate data for function."""
        x = np.arange(-5, 5, xres)
        y = 1 - np.cos(x) # pylint: disable=no-member
        yx0 = x * 0 # Horizontal line for x-axis
        yx1 = x * 0 + 1 # Horizontal line for y=1
        return x, y, yx0, yx1

    def show_plots(self, x, y, yx0, yx1):
        """Show and save plots."""
        plt.plot(x, y)
        plt.hold(True)
        plt.plot(x, yx0, 'k', linewidth=0.5)
        plt.plot(x, yx1, 'k', linewidth=0.5)
        plt.axis('equal')
        plt.xlabel(r'$x$')
        plt.ylabel(r'$f(x)$')
        plt.title(r'$f(x)=1-\cos(x)$')

        if self.saveplots:
            plt.savefig("../images/plot1minusCosX.svg")
            plt.savefig("../images/plot1minusCosX.png", dpi=self.dpi)

        plt.show()
        plt.close()

if __name__ == '__main__':
    CustomPlotter()
