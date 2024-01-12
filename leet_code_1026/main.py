# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, low=None, high=None):
            if not root:
                return
            if low==high==None:
                low=root.val
                high=root.val
            elif root.val<low:
                low = root.val
            elif root.val>high:
                high = root.val
            self.val = max(self.val, abs(high-low))
            dfs(root.left, low, high)
            dfs(root.right, low, high)

        self.val = float('-inf')
        dfs(root)
        return self.val  