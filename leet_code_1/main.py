class Solution(object):
    def twoSum(self, nums, target):
        result = {}
        for i in range(len(nums)):
            temp = target-nums[i]
            if temp in result:
                return [i, result[temp]]
            result[nums[i]] = i