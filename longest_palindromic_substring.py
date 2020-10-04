'''
Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            res = max(self.max_substr(s, i, i), self.max_substr(s, i, i + 1), res,
                      key=len)
        return res

    def max_substr(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]


ss = Solution()
s = "babad"
res = ss.longestPalindrome(s)
print('=== Given  string : {}'.format(s))
print('=== result is : {}'.format(res))
