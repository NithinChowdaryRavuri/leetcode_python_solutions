class Solution(object):
    def searchInsert(self, nums, target):
        l,r = 0, len(nums)
        while l<r:
            m = (l+r)//2
            if nums[m]<target:
                l = m+1
            else:
                r = m
        return l