class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates, start_index, remaining, path):
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(start_index, len(candidates)):
                num = candidates[i]
                if i > start_index and num == candidates[i-1]:
                    continue
                if remaining - num < 0:
                    break
                dfs(candidates, i+1, remaining - num, path+[num])
        res = []
        candidates.sort()
        dfs(candidates, 0, target, [])
        return res