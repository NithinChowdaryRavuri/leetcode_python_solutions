# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        out1=[]
        out2=[]
        def dfs(root, out):
            if not root:
                return
            if root.left==root.right==None:
                out.append(root.val)
            dfs(root.left, out)
            dfs(root.right, out)  
        dfs(root1, out1)
        dfs(root2, out2)
        return out1==out2
        