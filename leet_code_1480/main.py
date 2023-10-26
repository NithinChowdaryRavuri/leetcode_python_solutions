class Solution(object):
    def runningSum(self, nums):
        result = []
        result.append(nums[0])
        for i in range(1,len(nums)):
            result.append(nums[i]+result[i-1])
        return result