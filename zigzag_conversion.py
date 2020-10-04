class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        ans = ""
        interval = 2 * (numRows - 1)
        for i in range(0, len(s), interval):
            ans += s[i]
        for row in range(1, numRows - 1):
            inter = 2 * row
            i = row
            while i < len(s):
                ans += s[i]
                inter = interval - inter
                i += inter
        print(ans)
        for i in range(numRows - 1, len(s), interval):
            ans += s[i]
        return ans

ss = Solution()
s = "PAYPALISHIRING"
numRows = 3
res = ss.convert(s, numRows)
print('=== Given string : {}'.format(s))
print('=== Given number of row : {}'.format(numRows))
print('=== result is : {}'.format(res))
