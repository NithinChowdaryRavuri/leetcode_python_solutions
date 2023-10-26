class Solution(object):
    def characterReplacement(self, s, k):
        i, j, d, m = 0, 0, {}, 0
        while j<len(s):
            d[s[j]]=d.get(s[j], 0)+1
            if (j-i+1)-max(d.values())<=k:
                m = max(m, j-i+1)
            else:
                d[s[i]]-=1
                i+=1
            j+=1
        return m