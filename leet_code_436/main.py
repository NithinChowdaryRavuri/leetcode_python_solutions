class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        def binarySearch(arr, val):
            l,r = 0, len(arr)
            while l<r:
                m = (l+r)//2
                if arr[m]<val:
                    l = m+1
                else:
                    r = m
            return l
        start = defaultdict(int)
        res = []
        for i, inter in enumerate(intervals):
            start[inter[0]] = i
        keys = start.keys()
        for inter in intervals:
            if inter[1] in start:
                res.append(start[inter[1]])
            elif binarySearch(keys, inter[1])<len(keys):
                res.append(start[keys[binarySearch(keys, inter[1])]])
            else:
                res.append(-1)
        return res