'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        keys = {}
        for i in range(len(nums)):
            if target - nums[i] in keys:
                return [keys[target - nums[i]], i]
            if nums[i] not in keys:
                keys[nums[i]] = i

ss = Solution()
arr = [3,8,6,2,5,9]
tgt = 7
res = ss.twoSum(arr, tgt)
print('=== Given array : {}'.format(arr))
print('=== and target : {}'.format(tgt))
print('=== result is : {}'.format(res))
