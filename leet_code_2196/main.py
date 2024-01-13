# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        def builder(node):
            if node==-1:
                return
            if node not in graph:
                return TreeNode(node)
            root = TreeNode(node)
            values = graph[node]
            root.left = builder(values[0])
            root.right = builder(values[1])
            return root
        graph = dict()
        set1 = set()
        set2 = set()
        for d in descriptions:
            set1.add(d[0])
            set2.add(d[1])
            graph[d[0]] = graph.get(d[0], [-1,-1])
            if d[2]==1:
                graph[d[0]][0] = d[1]
            else:
                graph[d[0]][1] = d[1]
        start = list(set1-set2)[0]
        return builder(start)

        