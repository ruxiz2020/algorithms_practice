def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    h = {}
    for i, num in enumerate(nums):
        n = target - num
        if n not in h:
            h[num] = i
        else:
            return [h[n], i]



arr = [3,8,6,2,5,9]

print(twoSum(arr, 7))

print(twoSum(arr, 19))
