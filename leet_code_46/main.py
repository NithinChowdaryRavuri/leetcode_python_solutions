class Solution(object):
    def permute(self, nums):
        res = []
        def backtrack(nums, prem):
            if len(prem) == len(nums):
                res.append(prem[:])
                return
            for num in nums:
                if num not in prem:
                    prem.append(num)
                    backtrack(nums, prem)
                    prem.pop()
        backtrack(nums, [])
        return res
        