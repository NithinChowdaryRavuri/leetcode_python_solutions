# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans=0
        def solve(root):
            if not root:
                return 0
            l = solve(root.left)
            r = solve(root.right)
            self.ans = max(self.ans,l+r)
            return max(l,r)+1
        solve(root)
        return self.ans