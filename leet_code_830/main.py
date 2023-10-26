class Solution(object):
    def largeGroupPositions(self, s):
        result = []
        current = s[0]
        count = 1
        for i in range(1,len(s)):
            if s[i] == current:
                count+=1
            else:
                if count >2:
                    result.append([i-count, i-1])
                current= s[i]
                count = 1
        if count > 2:
            result.append([len(s) - count, len(s) - 1])
        return result