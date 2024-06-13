def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

nested_list = [1, [2, [3, 4], 5], 6, [[7, 8], 9]]
flattened_list = list(flatten(nested_list))
print(flattened_list)

'''def flatten(nested_list):
    flat_list = []

    def flatten_helper(lst):
        for item in lst:
            if isinstance(item, list):
                flatten_helper(item)
            else:
                flat_list.append(item)

    flatten_helper(nested_list)
    return flat_list

nested_list = [1, [2, [3, 4], 5], 6, [[7, 8], 9]]
flattened_list = flatten(nested_list)
print(flattened_list)'''