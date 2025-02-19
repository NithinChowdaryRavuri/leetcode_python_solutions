class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def dfs(path):
            if len(path) == n:
                self.count += 1
                if self.count == k: 
                    self.result = ''.join(path)
                return
            
            for char in "abc":
                if not path or char != path[-1]:
                    path.append(char)
                    dfs(path)
                    if self.result != "":
                        return self.result
                    path.pop()
        self.count = 0
        self.result = ""
        dfs([])
        return self.result