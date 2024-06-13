def three_sum_closest(nums, target):
    nums.sort()
    closest_sum = float('inf')

    for i in range(len(nums) - 2):
        # Set pointers j and k
        j, k = i + 1, len(nums) - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]
            # Check if the current sum is closer to the target
            if abs(total - target) < abs(closest_sum - target):
                closest_sum = total

            # Adjust pointers based on the comparison with the target
            if total < target:
                j += 1
            elif total > target:
                k -= 1
            else:
                return closest_sum

    return closest_sum


# Example usage:
nums = [-1, 2, 1, -4]
target = 1
print(three_sum_closest(nums, target))  # Output: 2
