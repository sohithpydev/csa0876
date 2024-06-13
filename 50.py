def odd_numbers(*args):
    stack = []
    for i in args:
        if i % 2 != 0:
            stack.append(i)
    return stack
print(odd_numbers(2,3,5,6,7,8,9))