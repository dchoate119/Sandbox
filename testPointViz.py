import numpy as np
from matplotlib import pyplot as plt
from vedo import *
from ipyvtklink.viewer import ViewInteractiveWidget

A = np.random.randn(1_000,3)

plt = Plotter(N=1, axes=1, bg=(1,1,1), interactive = True)
disp = []

disp.append(Points(A, c = 'blue', r = 5))

plt.show(disp, "test")