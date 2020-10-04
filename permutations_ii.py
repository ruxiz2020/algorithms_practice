'''Given a collection of numbers that might contain duplicates, return all possible unique permutations.'''

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length == 0:
            return []
        if length == 1:
            return [nums]
        nums.sort()
        res = []
        previousNum = None
        for i in range(length):
            if nums[i] == previousNum:
                continue
            previousNum = nums[i]
            for j in self.permuteUnique(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + j)
        return res

ss = Solution()
input = [1,1,2]
print('=== Given input  : {}'.format(input))

res = ss.permuteUnique(input)

print('=== result is : {}'.format(res))
