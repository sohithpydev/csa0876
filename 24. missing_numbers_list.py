nums = [4,3,2,7,8,2,3,1]
n = len(nums)
all_numbers = set(range(1,n+1))
disappeared_numbers = all_numbers - set(nums)
print(disappeared_numbers)
