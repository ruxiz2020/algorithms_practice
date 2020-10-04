class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def isValid(x, y, tmp):
            for i in range(9):
                if board[i][y] == tmp:
                    return False
            for i in range(9):
                if board[x][i] == tmp:
                    return False
            for i in range(3):
                for j in range(3):
                    if board[(x // 3) * 3 + i][(y // 3) * 3 + j] == tmp:
                        return False
            return True

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                tmp = board[i][j]
                board[i][j] = 'D'
                if isValid(i, j, tmp) == False:
                    return False
                else:
                    board[i][j] = tmp
        return True


ss = Solution()
input = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
print('=== Given input matrix : {}'.format(input))
res = ss.isValidSudoku(input)

print('=== result is : {}'.format(res))
