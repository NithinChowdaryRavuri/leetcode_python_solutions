class Solution(object):
    def checkInclusion(self, s1, s2):
        d, t = {}, {}
        for _ in s1:
            if _ in d:
                d[_] += 1
            else:
                d[_] = 1
        i, j = 0, 0
        while j < len(s2):
            if s2[j] in t:
                t[s2[j]]+=1
            else:
                t[s2[j]]=1
            if j-i+1<len(s1):
                j+=1
            else:
                if t==d:
                    return True
                else:
                    t[s2[i]]-=1
                    if t[s2[i]]==0:
                        del t[s2[i]]
                    i+=1
                    j+=1
        return False