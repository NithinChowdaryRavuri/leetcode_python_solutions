class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(x, y, prevHeight, visited):
            if x<0 or x==m or y<0 or y==n:
                return
            if (x,y) in visited:
                return
            height = heights[x][y]
            if height<prevHeight:
                return
            visited.add((x,y))
            dfs(x+1, y, height, visited)
            dfs(x, y+1, height, visited)
            dfs(x-1, y, height, visited)
            dfs(x, y-1, height, visited)

        m = len(heights)
        n = len(heights[0])
        p, a = set(), set()
        for i in range(m):
            dfs(i,0,0,p)
            dfs(i,n-1,0,a)
        for i in range(n):
            dfs(0,i,0,p)
            dfs(m-1,i,0,a)
        return list(p & a)
        
        