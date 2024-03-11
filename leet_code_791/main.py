class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        d = defaultdict(int)
        for c in s:
            d[c]+=1
        res = list()
        for c in order:
            res+=[c]*d[c]
            del d[c]
        for x, y in d.items():
            res+=[x]*y
        return ''.join(res)
        