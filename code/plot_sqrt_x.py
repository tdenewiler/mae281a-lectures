#! /usr/bin/env python
# coding: utf-8
"""Plot the function $f(x) = sqrt{x}$."""

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
        xres = 0.001
        x = np.arange(-1, 5, xres)
        y = np.sqrt(x) # pylint: disable=no-member

        return x, y

    def show_plots(self, x, y):
        """Show and save plots."""
        plt.plot(x, y)
        plt.axis('equal')
        plt.xlabel(r'$x$')
        plt.ylabel(r'$f(x)$')
        plt.title(r'$f(x)=\sqrt{x}$')

        if self.saveplots:
            plt.savefig("../images/plotSqrtX.svg")
            plt.savefig("../images/plotSqrtX.png", dpi=self.dpi)

        plt.show()
        plt.close()

if __name__ == '__main__':
    CustomPlotter()
