# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root,temp):
            nonlocal res
            if root.left==None and root.right==None:
                if temp==1:
                    res += root.val
            if root.left!=None:
                dfs(root.left,1)
            if root.right!=None:
                dfs(root.right,0)
            

        dfs(root,0)
        return res
        