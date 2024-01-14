class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def dfs(r,c):
            if r<0 or c<0 or r==row or c==col or board[r][c]!='O': 
                return
            board[r][c]='T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j]=='O' and (i in [0, row-1] or j in [0,col-1]):
                    dfs(i,j)
        
        for i in range(row):
            for j in range(col):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='T':
                    board[i][j]='O'