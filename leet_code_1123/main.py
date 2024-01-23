# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(root):
            if not root: return None, 0
            left, ld = dfs(root.left)
            right, rd = dfs(root.right)
            if ld==rd:
                return root, ld+1
            elif ld>rd:
                return left, ld+1
            else:
                return right, rd+1
        result, _ = dfs(root)
        return result
        
        