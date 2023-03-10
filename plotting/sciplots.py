#!/usr/bin/env python

import matplotlib.pyplot as plt

class Chart:
    def __init__(self, title, *args, **kwargs):
        self.title = title
        self.fig = plt.figure(*args, **kwargs)
        self.ax = self.fig.gca()
    
    def show(self):
        self.fig.show()

class AnnotatedLinePlot(Chart):
    def __init__(self, title=None, *args, **kwargs):
        super().__init__(title)

    def add_line(self, x, y, stdev=None):
        self.ax.plot(x, y, marker="o")

class GroupedBarChart(Chart):
    def __init__(self, title, *args, **kwargs):
        pass


if __name__ == "__main__":
    plot = AnnotatedLinePlot(figsize=(9, 6))
    plot.show()