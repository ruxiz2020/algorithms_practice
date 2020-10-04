class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        M, N = len(haystack), len(needle)
        for i in range(M - N + 1):
            if haystack[i : i + N] == needle:
                return i
        return -1

ss = Solution()
haystack = "hello"
needle = "ll"
print('=== Given str : {}'.format(haystack))
print('=== Given str : {}'.format(needle))
res = ss.strStr(haystack, needle)

print('=== result is : {}'.format(res))
