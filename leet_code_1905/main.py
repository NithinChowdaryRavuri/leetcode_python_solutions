class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        def bfs(i, j):
            queue = deque([(i, j)])
            visited = set([(i, j)])
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            res = True

            while queue:
                r, c = queue.popleft()
                grid2[r][c]=2
                for d in directions:
                    new_r, new_c = r + d[0], c + d[1]
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid2[new_r][new_c] == 1 and (new_r, new_c) not in visited:
                        if grid1[new_r][new_c] == 0:
                            res = False
                        visited.add((new_r, new_c))
                        queue.append((new_r, new_c))
            return res

        rows = len(grid1)
        cols = len(grid1[0])
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] ==grid1[i][j]== 1:
                    if bfs(i, j):
                        count += 1

        return count
        