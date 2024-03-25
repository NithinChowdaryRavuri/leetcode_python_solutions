class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        s = set([i for i in range(1,n+1)])
        d = defaultdict(int)
        for t in trust:
            if t[0] in s:
                s.remove(t[0])
            d[t[1]] += 1
        return -1 if not s or d[list(s)[0]]!=n-1 else list(s)[0]