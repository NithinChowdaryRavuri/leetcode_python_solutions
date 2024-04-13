class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        group = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] in group:
                group[groupSizes[i]].append(i)
            else:
                group[groupSizes[i]] = [i]
        result = []
        for key in group:
            for i in range(0, len(group[key]), key):
                result.append(group[key][i:i+key])
        return result