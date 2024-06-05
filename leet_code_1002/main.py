class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = False
        for word in words:
            curr = defaultdict(int)
            for char in word:
                curr[char] += 1
            if not res:
                res = curr
            else:
                for key in res.keys():
                    res[key] = min(res[key], curr[key])
        ans = []
        for key in res.keys():
            ans += [key]*res[key]
        return ans