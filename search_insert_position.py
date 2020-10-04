class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0;
        right = len(nums) - 1

        while left <= right:
            mid = ( left + right ) / 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left

ss = Solution()
nums = [1,3,5,6]
target = 5
print('=== Given list : {}'.format(nums))
print('=== Given target : {}'.format(target))
res = ss.searchInsert(nums, target)

print('=== result is : {}'.format(res))
