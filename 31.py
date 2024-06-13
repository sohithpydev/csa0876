counts = {}

def count_elements(lst):
    for element in lst:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    return counts

lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
element_counts = count_elements(lst)
print(element_counts)
