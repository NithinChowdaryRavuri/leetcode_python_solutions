class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        def binarySearch(nums, target):
            l,r = 0, len(nums)
            while l<r:
                m=(l+r)//2
                if nums[m]<target:
                    l=m+1
                else:
                    r=m
            return l
        size = len(mat[0])
        l = list()
        for i,row in enumerate(mat):
            l.append([i,size-binarySearch(row[::-1],1)])
        l.sort(key=lambda x:x[1])
        return [l[i][0] for i in range(k)]


        