#!/usr/bin/env python

import matplotlib.pyplot as plt

class GroupedBarChart():
    def __init__(self):
        pass

class AnnotatedLinePlot():
    def __init__(self, *args, **kwargs):
        self.fig = plt.figure(*args, **kwargs)
        self.ax = self.fig.gca()

    def add_line(self, x, y, stdev=None):
        self.ax.plot(x, y, marker="o")

    def show(self):
        self.fig.show()

if __name__ == "__main__":
    plot = AnnotatedLinePlot(figsize=(9, 6))
    plot.show()