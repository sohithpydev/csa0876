import numpy as np
import matplotlib.pyplot as plt

# Create some random data
data = [np.random.rand(10) for _ in range(5)]

# Create the boxplot
plt.boxplot(data)
plt.show()
