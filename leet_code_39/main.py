class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dp(candidates, index, target, output):
            if target == 0:
                res.append(output)
                return
            if index == 0:
                return
            if candidates[index-1] > target:
                dp(candidates, index-1, target, output)
            else:
                dp(candidates, index, target-candidates[index-1], output+[candidates[index-1]])
                dp(candidates, index-1, target, output)
        res = []
        dp(candidates, len(candidates), target, [])
        return res
        