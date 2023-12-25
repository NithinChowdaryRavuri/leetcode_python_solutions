class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ''
        mapt = [0]*128
        for w in t:
            mapt[ord(w)]+=1
        start, end, head, d, count = 0, 0, 0, float('inf'), len(t)
        while end < len(s):
            if mapt[ord(s[end])] > 0:
                count -= 1
            mapt[ord(s[end])] -= 1
            end += 1

            while count == 0:
                if d > end - start:
                    d = end - start
                    head = start
                if mapt[ord(s[start])] == 0:
                    count += 1
                mapt[ord(s[start])] += 1
                start += 1
        return s[head:head + d] if d != float('inf') else ''        