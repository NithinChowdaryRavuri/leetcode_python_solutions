class Solution(object):
    def majorityElement(self, nums):
        nums = sorted(nums)
        return nums[int(len(nums)/2)]