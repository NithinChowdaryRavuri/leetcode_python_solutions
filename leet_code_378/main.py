class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def count(matrix, target):
            i, j, count = 0, n-1, 0
            while 0<=i<n and 0<=j<n:
                if matrix[i][j]<=target:
                    i+=1
                    count+=j+1
                else:
                    j-=1
            return count
        n = len(matrix)
        l, r = matrix[0][0], matrix[n-1][n-1]
        while l<r:
            m = (l+r)//2
            c = count(matrix, m)
            if c<k:
                l = m+1
            else:
                r = m
        return l