class Solution(object):
    def wordPattern(self, pattern, s):
        s = s.split()
        check = {}
        if len(s)!=len(pattern):
            return False
        for i in range(len(s)):
            if s[i] not in check.keys() and pattern[i] not in check.values():
                check[s[i]] = pattern[i]
            else:
                if s[i] in check.keys():
                    if check[s[i]] != pattern[i]:
                        return False
                else:
                    return False
        else:
            return True