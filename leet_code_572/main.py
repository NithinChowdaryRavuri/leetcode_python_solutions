# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def dfs(root):
            if not root:
                return "#"
            return '!'+str(root.val)+dfs(root.left)+dfs(root.right)
        return dfs(subRoot) in dfs(root)
        