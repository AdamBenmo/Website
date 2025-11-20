nums = [6, 0, 3, 5, 7, 4, 2]

# Outer loop to pick each number
for i in range(len(nums)):
    # Inner loop to compare it with every other number
    for j in range(i + 1, len(nums)):
        # Compare the current number with the next number
        if nums[i] > nums[j]:
            # Swap if the current number is bigger
            nums[i], nums[j] = nums[j], nums[i]

print(nums)