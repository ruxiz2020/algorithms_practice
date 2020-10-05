class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    before = 0
                elif i == 0:
                    before = grid[i][j-1]
                elif j == 0:
                    before = grid[i-1][j]
                else:
                    before = min(grid[i-1][j], grid[i][j-1])
                grid[i][j] = before + grid[i][j]
        return grid[m-1][n-1]

ss = Solution()
input = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

res = ss.minPathSum(input)

print('=== Given input : {}'.format(input))
print('=== result is : {}'.format(res))
