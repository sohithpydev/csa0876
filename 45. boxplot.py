import numpy as np
import matplotlib.pyplot as plt

x = np.arange(5)
y = np.random.rand(5)
yerr = np.random.rand(5) / 10

plt.errorbar(x, y, yerr=yerr, fmt='o')
plt.show()
