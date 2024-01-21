class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def bfs(i, j):
            queue = deque([(i,j)])
            area = 0
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            while queue:
                r,c = queue.popleft()
                if 0<=r<rows and 0<=c<cols and grid[r][c]==1:
                    grid[r][c]=0
                    area+=1
                    for d in directions:
                        new_r = r+d[0]
                        new_c = c+d[1]
                        queue.append((new_r, new_c))
            return area

        rows = len(grid)
        cols = len(grid[0])
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    res = max(res, bfs(i,j))
        return res        