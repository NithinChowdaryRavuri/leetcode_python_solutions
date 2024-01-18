class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l, r, res = 0, len(citations)-1, 0
        while l<=r:
            m = (l+r)//2
            if citations[m]>=len(citations)-m:
                res = len(citations)-m
                r = m-1
            else:
                l = m+1
        return res