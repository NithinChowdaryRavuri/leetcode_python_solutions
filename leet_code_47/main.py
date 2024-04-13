class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, counter):
            if len(path) == len(nums):
                res.append(path)
                return
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    backtrack(path + [num], counter)
                    counter[num] += 1
        res = []
        counter = Counter(nums)
        backtrack([], counter)
        return res