class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        prev, index = 0, 0
        res = []
        for i in range(1,n+1):
            if index == len(target): break
            if i == target[index]:
                res.append("Push")
                index += 1
            elif i < target[index]:
                res.append("Push")
                res.append("Pop")
        return res