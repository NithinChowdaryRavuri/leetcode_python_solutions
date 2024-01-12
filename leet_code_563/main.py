# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.out = 0
        def dfs(root):
            if not root:
                return 0  
            if root.left==root.right==None:
                return root.val
            left = dfs(root.left)
            right = dfs(root.right)
            self.out += abs(left-right)
            return left+right+root.val
        dfs(root)
        return self.out
