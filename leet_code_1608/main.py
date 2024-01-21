class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binarySearch(nums, val):
            l, r = 0, len(nums)
            while l<r:
                m = (l+r)//2
                if nums[m]<val:
                    l = m+1
                else:
                    r = m
            return l
        n = len(nums)
        nums.sort()
        max = nums[-1]
        for i in range(1, max+1):
            if n-binarySearch(nums,i)==i:
                return i
        return -1