class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(index, curr):
            if index == len(nums):
                return curr
            include = dfs(index+1, curr ^ nums[index])
            exclude = dfs(index+1, curr)

            return include + exclude

        return dfs(0,0)