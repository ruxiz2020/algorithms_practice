class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x + 1
        # [left, right)
        while left < right:
            mid = left + (right - left) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 < x:
                left = mid + 1
            else:
                right = mid
        return left - 1

ss = Solution()
input = 4

print('=== Given input : {}'.format(input))
res = ss.mySqrt(input)
print('=== result is : {}'.format(res))
