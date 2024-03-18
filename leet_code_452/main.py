class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        res = [points[0]]
        for p in points:
            if p[0] <= res[-1][1]:
                temp = res.pop()
                res.append([max(temp[0], p[0]), min(temp[1], p[1])])
            else:
                res.append(p)
        return len(res)