class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x==0 or x==1 or n==1:
            return x

        if n==0:
            return 1

        if x==-1:
            if n%2==0:
                return 1
            else:
                return -1

        if n<0:
            return 1/self.myPow(x, -n)

        xx = self.myPow(x, n//2)

        if n%2 ==0:
            return xx*xx
        return xx*xx*x

ss = Solution()
x = 2.00000
n = 10
res = ss.myPow(x, n)
print('=== Given input x, n : {},  {}'.format(x, n))
print('=== result is : {}'.format(res))
