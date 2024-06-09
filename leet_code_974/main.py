class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        prefix = 0
        remainder = {0:1}
        for num in nums:
            prefix += num
            mod = prefix % k
            if mod < 0:
                mod += k
            if mod in remainder:
                ans += remainder[mod]
                remainder[mod] +=1
            else:
                remainder[mod] = 1
        return ans