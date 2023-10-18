class Solution(object):
    def generateMatrix(self, n):
        min_row, max_row, min_col, max_col = 0, n-1, 0, n-1
        matrix = [[0 for i in range(n)] for j in range(n)]
        r = 1
        while r<n**2:
            for i in range(min_col,max_col+1):
                matrix[min_row][i] = r
                r+=1
            min_row+=1
            for i in range(min_row,max_row+1):
                matrix[i][max_col] = r
                r+=1
            max_col-=1
            for i in range(max_col,min_col-1,-1):
                matrix[max_row][i]=r
                r+=1
            max_row-=1
            for i in range(max_row,min_row-1,-1):
                matrix[i][min_col] = r
                r+=1
            min_col+=1
        if n%2!=0:
            matrix[n//2][n//2]=r
        return matrix