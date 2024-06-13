def remove_duplicates(duplicates):
    result = []
    for i in duplicates:
        if i not in result:
            result.append(i)
    return result
duplicates = [4,6,1,1,2,3,3]
print(remove_duplicates(duplicates))
duplicates.sort(reverse=True)
print(remove_duplicates(duplicates))
duplicates.sort(reverse=False)
print(remove_duplicates(duplicates))

