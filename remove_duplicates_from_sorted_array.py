class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        cur = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[cur]:
                cur += 1
                nums[cur] = nums[i]
        return cur+1, nums

ss = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]


res = ss.removeDuplicates(nums)
print('=== Given list : {}'.format(nums))
print('=== result is : {}'.format(res))
