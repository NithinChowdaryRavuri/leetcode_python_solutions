class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i,j):
            if i<0 or i==rows or j<0 or j==cols or grid[i][j]!=1:
                return
            grid[i][j]=0
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if (i==0 or i==rows-1 or j==0 or j==cols-1) and grid[i][j]==1:
                    dfs(i, j)
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    count+=1
        return count
        