# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, cur=float('-inf')):
            if not root:
                return
            if root.val>=cur:
                self.out+=1
                cur = root.val
            dfs(root.left, cur)
            dfs(root.right, cur)
        self.out = 0
        dfs(root)
        return self.out
        