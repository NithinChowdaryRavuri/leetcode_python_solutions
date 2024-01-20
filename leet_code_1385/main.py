class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        def binarySearch(arr, val):
            l,r = 0, len(arr)
            while l<r:
                m = (l+r)//2
                if arr[m]<val:
                    l = m+1
                else:
                    r = m
            return l
        arr2.sort()
        out = 0
        for num in arr1:
            left = binarySearch(arr2, num-d)
            right = binarySearch(arr2, num+d)
            if left==right:
                if left<len(arr2) and arr2[left] not in [num-d, num+d]:
                    out+=1
                elif left==len(arr2):
                    out+=1
        return out
        