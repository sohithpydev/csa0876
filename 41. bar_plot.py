categories = ['A', 'B', 'C', 'D', 'E']
values = np.random.randint(1, 10, size=len(categories))

plt.bar(categories, values)

plt.title('Barplot Example')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.show()
