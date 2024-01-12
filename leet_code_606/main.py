# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def dfs(root,s):
            if not root:
                return
            s.append(str(root.val))
            if root.left or root.right:
                s.append('(')
                dfs(root.left,s)
                s.append(')')
            if root.right:
                s.append('(')
                dfs(root.right,s)
                s.append(')')
        s = []
        dfs(root,s)
        return ''.join(s)
        