class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def bfs(i,j):
            queue = deque([(i,j)])
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            visited = set([(i,j)])
            closed = True
            while queue:
                r,c = queue.popleft()
                if r==0 or r==rows-1 or c==0 or c==cols-1:
                    closed = False
                grid[r][c]=2
                for d in directions:
                    new_r = r+d[0]
                    new_c = c+d[1]
                    if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited and grid[new_r][new_c]==0:
                        visited.add((new_r, new_c))
                        queue.append((new_r, new_c))
            return closed
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    if bfs(i,j):
                        count+=1
        return count
        