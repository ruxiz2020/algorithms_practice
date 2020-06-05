def twoSum(nums, target):

    l = len(nums)
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, l):
            if nums[i] + nums[j] == target:
                return[i, j]


arr = [3, 8, 6, 2, 5, 9]

print(twoSum(arr, 7))

print(twoSum(arr, 19))
