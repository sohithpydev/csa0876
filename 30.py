result = []
def sum_squares(numbers):
    for i in numbers:
        result.append(i**2)
    return result, sum(result)
numbers = [1,2,3]
print(sum_squares(numbers))
