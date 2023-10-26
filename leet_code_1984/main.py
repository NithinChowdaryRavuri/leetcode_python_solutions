class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i, j, ans = 0, k - 1, float("inf")
        while j < len(nums):
            temp = nums[j] - nums[i]
            if temp < ans:
                ans = temp
            i += 1
            j += 1
        return ans

