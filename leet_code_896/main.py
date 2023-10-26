class Solution(object):
    def isMonotonic(self, nums):
        if len(nums)==1:
            return True
        inc, dec = True, True
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                inc = False
                break
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                dec = False
                break
        return inc or dec