class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(mat)
        cols = len(mat[0])
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==0:
                    queue.append((i,j))
                else:
                    mat[i][j] = float('inf')
        
        while queue:
            r, c = queue.popleft()
            for d in directions:
                new_r = r+d[0]
                new_c = c+d[1]
                if 0<=new_r<rows and 0<=new_c<cols and mat[new_r][new_c]>mat[r][c]+1:
                    mat[new_r][new_c]=mat[r][c]+1    
                    queue.append((new_r, new_c))          
        return mat
        