class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def bfs(i,j):
            queue = deque([(i,j)])
            visited = set()
            visited.add((i,j))
            time = 0
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            while queue:
                n = len(queue)
                for _ in range(n):
                    r,c = queue.popleft()
                    if grid[r][c]==2:
                        return time
                    for d in directions:
                        nr = r+d[0]
                        nc = c+d[1]
                        if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]!=0 and (nr,nc) not in visited:
                            visited.add((nr,nc))
                            queue.append((nr,nc))
                time+=1
            return -1                 

        res = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    val = bfs(i,j)
                    if val==-1: return -1
                    else: res = max(res, val)
        return res