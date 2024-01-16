class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        value = 0
        n = len(s)
        index = 0
        while index<n:
            if index+1<n and d[s[index]]<d[s[index+1]]:
                value+=(d[s[index+1]]-d[s[index]])
                index+=2
            else:
                value+=d[s[index]]
                index+=1
        return value
