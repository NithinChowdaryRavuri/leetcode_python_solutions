class Solution(object):
    def isValid(self, s):
        l = []
        d = {")":"(", "}":"{", "]":"["}
        for char in s:
            if char in "({[":
                l.append(char)
            else:
                if len(l)==0:
                    return False
                if d[char] != l.pop():
                    return False
        return len(l)==0