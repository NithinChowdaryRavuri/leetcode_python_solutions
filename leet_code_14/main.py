class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = lambda x: len(x))
        res = list(strs[0])
        for word in strs:
            temp=0
            if not res:
                break
            for i, c in enumerate(word):
                if i>=len(res) or res[i]!=c:
                    temp = i
                    break
                temp = i+1
            res = res[:temp]
        return ''.join(res)       