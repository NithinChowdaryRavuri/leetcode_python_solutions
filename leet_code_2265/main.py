# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return [0,0]
            left = dfs(root.left)
            right = dfs(root.right)
            if int((root.val+left[0]+right[0])/(left[1]+right[1]+1))==root.val:
                self.out+=1
            return [root.val+left[0]+right[0],left[1]+right[1]+1]
            
        self.out = 0
        dfs(root)
        return self.out
        