class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        tmp = 0
        res = float("-inf")
        for i in range(len(nums)):
            tmp = nums[i] + (tmp if tmp > 0 else 0)
            res = max(res, tmp)
        return res


ss = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print('=== Given nums : {}'.format(nums))

res = ss.maxSubArray(nums)

print('=== result is : {}'.format(res))
