class Solution(object):
    def pivotIndex(self, nums):
        lsum=0
        rsum=0
        for i in range(len(nums)):
            lsum=sum(nums[0:i])
            rsum=sum(nums[i+1:])
            if lsum==rsum:
                return i
        return -1