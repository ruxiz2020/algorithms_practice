class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.lower_bound(nums, target)
        right = self.higher_bound(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]

    def lower_bound(self, nums, target):
        # find in range [left, right)
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def higher_bound(self, nums, target):
        # find in range [left, right)
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

ss = Solution()
nums = [5,7,7,8,8,10]
target = 8
print('=== Given list : {}'.format(nums))
print('=== Given target : {}'.format(target))
res = ss.searchRange(nums, target)

print('=== result is : {}'.format(res))
