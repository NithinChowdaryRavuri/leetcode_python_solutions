# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(root, p, q):
            if not root: return False
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            if left and right:
                self.res = root
                return True
            if root.val==p.val or root.val==q.val:
                if left or right:
                    self.res = root
                return True
            return left or right
        self.res = None
        dfs(root, p, q)
        return self.res