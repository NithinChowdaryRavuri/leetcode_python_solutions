class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
        if intervals[0][0] > newInterval[1]:
            return [newInterval]+intervals
        if intervals[-1][1] < newInterval[0]:
            return intervals+[newInterval]
        ni = newInterval
        res, val, used = [], False, False
        for i in intervals:
            if i[1] < ni[0]:
                res.append(i)
            elif i[0] > ni[1]:
                if used:
                    res.append(i)
                else:
                    used = True
                    res.append(ni)
                    res.append(i)
            else:
                used = True
                if not val:
                    temp = [min(i[0], ni[0]), max(i[1], ni[1])]
                    res.append(temp)
                    val = True
                else:
                    temp = res.pop()
                    temp = [min(temp[0], i[0]), max(temp[1], i[1])]
                    res.append(temp)
        return res