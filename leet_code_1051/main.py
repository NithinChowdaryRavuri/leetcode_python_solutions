class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = heights[:]
        ans.sort()
        count = 0
        for i in range(len(heights)):
            if heights[i] != ans[i]: count+=1
        return count
        