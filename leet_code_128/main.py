class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums)==0 :
            return 0
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        result = 1
        temp = 1
        for i in range(len(nums) - 1):
            if nums[i]+1 == nums[i+1]:
                temp += 1
            else:
                temp = 1
            if temp >= result:
                result = temp
        return result