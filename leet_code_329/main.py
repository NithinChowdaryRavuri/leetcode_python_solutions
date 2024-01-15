class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def dfs(i, j, memo):
            if memo[i][j]!=-1:
                return memo[i][j]
            directions = [(-1,0), (0,-1), (1,0), (0,1)]
            max_depth = 1
            for r,c in directions:
                new_i = i+r
                new_j = j+c
                if 0<=new_i<row and 0<=new_j<col and matrix[new_i][new_j]>matrix[i][j]:
                    depth = 1+dfs(new_i, new_j, memo)
                    max_depth = max(max_depth, depth)
            memo[i][j] = max_depth
            return max_depth
        row = len(matrix)
        col = len(matrix[0])
        memo = [[-1]*col for _ in range(row)]
        res = 0
        for i in range(row):
            for j in range(col):
                res = max(res, dfs(i,j, memo))
        return res