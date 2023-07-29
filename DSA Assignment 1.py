def search_insert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # If the target is not found, return the index where it would be inserted
    return left

# Test the function with the example input
nums = [1, 3, 5, 6]
target = 5
output = search_insert(nums, target)
print(output)  # Output: 2
