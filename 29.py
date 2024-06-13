def nth_max_min(lst, n):
    if n > len(lst) or n < 1:
        return None, None

    sorted_lst = sorted(lst)

    nth_min = sorted_lst[n - 1]
    nth_max = sorted_lst[-n]

    return nth_max, nth_min


# Example Usage
numbers = [4, 2, 9, 7, 5, 6, 7, 1, 3, 8,0]
print(nth_max_min(numbers,3))
