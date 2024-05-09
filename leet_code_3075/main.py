class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        res, i = 0, 0
        while i < k:
            val = happiness.pop()
            if val <= i:
                val = 0
            else:
                val -= i
            res += val
            i += 1
        return res

        