class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if arr[0]<arr[1]>arr[2]:
            return 1
        l,r = 0,len(arr)-1
        while l<=r:
            m = (l+r)//2 
            if arr[m-1]<arr[m]>arr[m+1]:
                return m
            if arr[m-1]<arr[m]<arr[m+1]:
                l = m+1
            if arr[m-1]>arr[m]>arr[m+1]:
                r = m-1