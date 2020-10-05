class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]

ss = Solution()
a = "11"
b = "1"

print('=== Given a, b : {}, {}'.format(a, b))
res = ss.addBinary(a, b)
print('=== result is : {}'.format(res))
