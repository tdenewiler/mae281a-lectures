#! /usr/bin/env python
# coding: utf-8
"""
Plot the function $f(x) = sqrt{x}$.
"""

import matplotlib
matplotlib.use('Qt4Agg') # For use over SSH.
import matplotlib.pyplot as plt
import numpy as np

class CustomPlotter(object):
    """
    Plot custom function.
    """
    def __init__(self):
        self.saveplots = True
        self.dpi = 100
        xres = 0.001

        x, y = self.generate_data(xres)
        self.show_plots(x, y)

    @classmethod
    def generate_data(cls, xres):
        """
        Generate data for function.
        """
        xres = 0.001
        x = np.arange(-1, 5, xres)
        y = np.sqrt(x) # pylint: disable=no-member

        return x, y

    def show_plots(self, x, y):
        """
        Show and save plots.
        """
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
