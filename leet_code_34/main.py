class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        def binarySearch(nums, target):
            l,r = 0, len(nums)
            while l<r:
                m = (l+r)//2
                if nums[m]<target:
                    l = m+1
                else:
                    r = m
            return l
        start = binarySearch(nums, target)
        end = binarySearch(nums, target+1)
        if start==end:
            return [-1,-1]
        else:
            return [start, end-1]