'''
Given a string s, find the length of the longest substring without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 0
        chars = set()
        res = 0
        while left < len(s) and right < len(s):
            if (s[right] in chars) and (s[left] in chars):
                chars.remove(s[left])
                left += 1
            else:
                chars.add(s[right])
                right += 1
                res = max(res, len(chars))
        return res


ss = Solution()
s = "abcabcbb"
res = ss.lengthOfLongestSubstring(s)
print('=== Given string : {}'.format(s))
print('=== result is : {}'.format(res))
