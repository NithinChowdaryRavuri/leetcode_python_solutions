class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def dfs(path):
            if len(path) == len(nums):
                if ''.join(path) not in nums:
                    self.result = ''.join(path)
                return
            for char in ["0", "1"]:
                path.append(char)
                dfs(path)
                if self.result != "": return
                path.pop()
        self.result = ""
        dfs([])
        return self.result