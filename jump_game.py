class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        step = nums[0]
        for i in range(1, len(nums)):
            if step > 0:
                step -= 1
                step = max(step, nums[i])
            else:
                return False
        return True

ss = Solution()
nums = [2,3,1,1,4]
print('=== Given nums : {}'.format(nums))

res = ss.canJump(nums)

print('=== result is : {}'.format(res))
