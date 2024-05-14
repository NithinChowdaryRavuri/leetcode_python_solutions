class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
                return 0
            current = grid[i][j]
            grid[i][j] = 0
            local = current
            local = max(local, current+dfs(i+1, j), 
                        current+dfs(i-1, j), 
                        current+dfs(i, j+1), 
                        current+dfs(i, j-1))
            grid[i][j] = current
            return local
        res, m, n = 0, len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    res = max(res, dfs(i,j))
        return res