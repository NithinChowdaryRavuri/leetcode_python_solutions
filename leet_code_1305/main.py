# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def dfs(root, stack):
            if not root:
                return
            dfs(root.left, stack)
            stack.append(root.val)
            dfs(root.right, stack)
        l = []
        dfs(root1, l)
        dfs(root2, l)
        return sorted(l)      