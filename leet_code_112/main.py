# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def dfs(root,cur_sum=0):
            if not root:
                return False
            if root.left==root.right==None:
                cur_sum += root.val
                if cur_sum==targetSum:
                    return True
            return dfs(root.left, cur_sum+root.val) or dfs(root.right, cur_sum+root.val)
        return dfs(root)
        