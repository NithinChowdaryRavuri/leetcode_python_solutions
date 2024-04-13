class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isValid(board, row, col):
            for i in range(row):
                if board[i] == col or abs(row - i) == abs(col - board[i]):
                    return False
            return True

        def backtrack(board, row):
            if row == n:
                res.append(list(board))
                return
            for col in range(n):
                if isValid(board, row, col):
                    board[row] = col
                    backtrack(board, row + 1)

        res = []
        backtrack([0] * n, 0)
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in row] for row in res]