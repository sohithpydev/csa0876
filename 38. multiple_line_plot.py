import random
import matplotlib.pyplot as plt

x = [random.randint(1,10) for i in range (5)]
y = [random.randint(1,100) for i in range (5)]
z = [random.randint(1,10) for i in range (5)]
plt.figure()
plt.plot(x, y)
plt.title("Basic Line Plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
