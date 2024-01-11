# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        def dfs(root):
            if not root:
                return
            if low<=root.val<=high:
                self.out += root.val
            if root.val>=high:
                dfs(root.left)
            elif root.val<=low:
                dfs(root.right)
            else:
                dfs(root.left)
                dfs(root.right)
        self.out = 0
        dfs(root)
        return self.out 
        