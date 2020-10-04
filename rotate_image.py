class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        return matrix

ss = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print('=== Given matrix  : {}'.format(matrix))

res = ss.rotate(matrix)

print('=== result is : {}'.format(res))
