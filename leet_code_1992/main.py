class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        def bfs(i,j):
            queue = deque([(i,j)])
            temp = list()
            visited = set()
            while queue:
                r,c = queue.popleft()
                land[r][c]=0
                temp = [r,c]
                if c+1<cols and land[r][c+1]==1 and (r, c+1) not in visited:
                    visited.add((r, c+1))
                    queue.append((r, c+1))
                if r+1<rows and land[r+1][c]==1 and (r+1, c) not in visited:
                    visited.add((r+1, c))
                    queue.append((r+1, c))
            return temp


        rows = len(land)
        cols = len(land[0])
        res = []
        for i in range(rows):
            for j in range(cols):
                if land[i][j]==1:
                   res.append([i,j]+bfs(i,j))
        return res
