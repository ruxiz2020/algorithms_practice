class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        total = m + n - 2
        v = n - 1
        def permutation(m, n):
            son = 1
            for i in range(m, m - n, -1):
                son *= i
            mom = 1
            for i in range(n, 0, -1):
                mom *= i
            return son / mom
        return permutation(total, min(v, total -v))


ss = Solution()
m = 3
n = 2

res = ss.uniquePaths(m, n)
print('=== Given m : {}'.format(m))
print('=== Given n : {}'.format(n))
print('=== result is : {}'.format(res))
