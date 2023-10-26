class Solution(object):
    def isToeplitzMatrix(self, matrix):
        rows = len(matrix)
        l = matrix[0]
        l.pop()
        for i in range(1,rows):
            l = [matrix[i][0]] + l
            if l==matrix[i]:
                l.pop()
            else:
                return False
        return True