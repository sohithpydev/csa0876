# Maximum jump length
def canJump(nums):
    farthest = 0
    for i in range(len(nums)):
        if i > farthest:
            return False
        farthest = max(farthest, i + nums[i])
    return True

# Example usage:
print(canJump([2, 3, 1, 1, 4]))  # Output: True
print(canJump([3, 2, 1, 0, 4]))  # Output: False

# Overlapping intervals
def merge(intervals):
    # Step 1: Sort the intervals by their starting times
    intervals.sort(key=lambda x: x[0])

    merged_intervals = []

    for interval in intervals:
        # If the merged_intervals list is empty or there is no overlap with the last interval
        if not merged_intervals or merged_intervals[-1][1] < interval[0]:
            merged_intervals.append(interval)
        else:
            # There is an overlap, so we merge the current interval with the last interval in merged_intervals
            merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])

    return merged_intervals

# Example usage:
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))  # Output: [[1, 6], [8, 10], [15, 18]]

intervals = [[1, 4], [4, 5]]
print(merge(intervals))  # Output: [[1, 5]]
