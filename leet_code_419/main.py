class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        def bfs(board, i, j):
            queue = deque([(i,j)])
            while queue:
                r,c = queue.popleft()
                board[r][c] = '.'
                if r!=row-1 and board[r+1][c]=='X':
                    queue.append([r+1,c])
                if c!=col-1 and board[r][c+1]=='X':
                    queue.append([r,c+1])
        row = len(board)
        col = len(board[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if board[i][j]=='X':
                    count += 1
                    bfs(board, i, j)
        return count
        