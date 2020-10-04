'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[length] = nums[i]
                length += 1
        return length

ss = Solution()
nums = [3,2,2,3]
val = 3
print('=== Given list : {}'.format(nums))
print('=== Given value : {}'.format(val))
res = ss.removeElement(nums, val)

print('=== result is : {}'.format(res))
