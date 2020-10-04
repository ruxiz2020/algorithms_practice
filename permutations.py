class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, res, [])
        return res

    def dfs(self, nums, res, path):
        if not nums:
            res.append(path)
            return
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i] + nums[i + 1:], res, path + [nums[i]])

ss = Solution()
input = [1,2,3]
print('=== Given input  : {}'.format(input))

res = ss.permute(input)

print('=== result is : {}'.format(res))
