class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        p, n, ans = 0, 0, 0

        for num in nums:
            p = max(p, 0) + num
            n = min(n, 0) + num

            ans = max(ans, p, abs(n))
        
        return ans