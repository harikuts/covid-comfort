from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
import random
import math

import wx

"""
Starter code from
https://stackoverflow.com/questions/10737459/embedding-a-matplotlib-figure-inside-a-wxpython-panel
"""

def generate_random_positions(num, max_dist):
    positions = []
    distances = []
    for i in range(num):
        while True:
            x, y = random.randint(1, max_dist)
            if (x, y) not in positions:
                positions.append((x, y))
                distances.append(math.sqrt(x**2 + y**2))
                break
    return positions, distances

class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()

    def draw(self):
        self.positions, self.distances = generate_random_positions(random.randint(1, 10). 20)
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)


if __name__ == "__main__":
    app = wx.PySimpleApp()
    fr = wx.Frame(None, title='test')
    panel = CanvasPanel(fr)
    panel.draw()
    fr.Show()
    app.MainLoop()
