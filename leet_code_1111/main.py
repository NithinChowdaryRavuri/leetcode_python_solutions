class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        assigned_depth = [0] * len(seq)
        depth_level = 0
        for index, char in enumerate(seq):
            if char == "(":
                assigned_depth[index] = depth_level & 1
                depth_level += 1
            else:
                depth_level -= 1
                assigned_depth[index] = depth_level & 1      
        return assigned_depth