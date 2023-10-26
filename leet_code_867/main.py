class Solution(object):
    def transpose(self, matrix):
        rows = len(matrix)
        columns = len(matrix[0])
        b=[]
        for i in range(columns):
            c=[]
            for j in range(rows):
                c.append(matrix[j][i])
            b.append(c)
        return b