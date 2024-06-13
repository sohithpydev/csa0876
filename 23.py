def three_sum(nums):
    # Sort the array
    nums.sort()
    triplets = []

    # Iterate through the array with a pointer i
    for i in range(len(nums) - 2):
        # Avoid duplicate triplets by skipping identical elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Set pointers j and k
        j, k = i + 1, len(nums) - 1

        # Find pairs that sum up to -nums[i]
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total == 0:
                triplets.append([nums[i], nums[j], nums[k]])
                # Move pointers j and k to skip identical elements
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1
                j += 1
                k -= 1
            elif total < 0:
                j += 1
            else:
                k -= 1

    return triplets


# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]
