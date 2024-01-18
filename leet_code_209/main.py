class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        sum, ans = 0, float('inf')
        left = 0
        for right in range(len(nums)):
            sum+=nums[right]
            while sum>=target:
                ans = min(ans, right-left+1)
                sum-=nums[left]
                left+=1
        return ans if ans!=float('inf') else 0
        