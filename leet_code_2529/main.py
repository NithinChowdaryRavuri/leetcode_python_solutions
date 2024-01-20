class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
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
            print(l)
            return l
        n = len(nums)
        neg = binarySearch(nums, 0)
        pos = n - binarySearch(nums, 1)
        return max(pos, neg)
        