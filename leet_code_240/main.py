class Solution(object):
    def searchMatrix(self, m, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i,j = 0, len(m[0])-1
        while i>=0 and i<len(m) and j>=0 and j<len(m[0]):
            if m[i][j]==target:
                return True
            elif m[i][j]>target:
                j-=1
            else:
                i+=1
        return False