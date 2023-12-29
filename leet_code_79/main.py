class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        Rows = len(board)
        Columns = len(board[0])
        path = set()

        def dfs(r, c, index):
            if index == len(word):
                return True
            if r<0 or c<0 or r>=Rows or c>=Columns or board[r][c]!=word[index] or (r,c) in path:
                return False
            path.add((r,c))
            res = dfs(r+1,c,index+1) or dfs(r,c+1,index+1) or dfs(r-1,c,index+1) or dfs(r,c-1,index+1)
            path.remove((r,c))
            return res

        for r in range(Rows):
            for c in range(Columns):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False
        