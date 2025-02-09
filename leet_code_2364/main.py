class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        result, diff = 0, {}

        for i in range(len(nums)):
            value = i - nums[i]
            good_pairs = diff.get(value, 0)
            result += i - good_pairs
            diff[value] = good_pairs + 1
        
        return result