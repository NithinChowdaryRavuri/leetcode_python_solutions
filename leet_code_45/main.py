class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = nums[0]
        res = 0
        furthest = float('-inf')
        while l < len(nums):   
            while l < min(r + 1, len(nums)):
                furthest = max(furthest, l + nums[l])
                l += 1

            r = furthest
            res += 1
            
        return res if len(nums) > 1 else 0