data = [random.randint(1,100) for i in range (10)]

plt.figure()
plt.hist(data, bins=5)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
