# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(root):
            if root.left==root.right==None:
                return True if root.val==1 else False
            return dfs(root.left) or dfs(root.right) if root.val==2 else dfs(root.left) and dfs(root.right)
        return dfs(root)