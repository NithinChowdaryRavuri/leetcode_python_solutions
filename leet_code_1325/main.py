# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        def dfs(root):
            if not root:
                return
            left = dfs(root.left)
            right = dfs(root.right)
            if left==None:
                root.left = None
            if right==None:
                root.right = None
            if left==right==None:
                if root.val==target:
                    return None
            return root 
        return dfs(root)