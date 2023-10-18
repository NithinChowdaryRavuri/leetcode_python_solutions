class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        nums.sort()
        smallest = 1
        for num in nums:
            if num<1:
                continue
            if num==smallest:
                smallest+=1
        return smallest