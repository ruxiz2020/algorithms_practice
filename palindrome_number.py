'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        tmp = x
        y = 0
        while tmp:
            y = y * 10 + tmp % 10
            tmp = tmp // 10
        return y == x

ss = Solution()
x = 121
res = ss.isPalindrome(x)
print('=== Given input : {}'.format(x))
print('=== result is : {}'.format(res))
