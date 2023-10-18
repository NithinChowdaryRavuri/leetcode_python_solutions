class Solution(object):
    def searchMatrix(self, matrix, target):
        i = 0
        while i<len(matrix):
            if matrix[i][0]<=target:
                i+=1
            else:
                i-=1
                break
        if i==-1:
            return False
        elif i==len(matrix):
            i-=1
        return target in matrix[i]