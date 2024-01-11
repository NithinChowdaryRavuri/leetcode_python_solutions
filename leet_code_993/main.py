# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        def dfs(root,x,depth=0,parent=None):
            if not root:
                return
            if root.val==x:
                return depth,parent
            l = dfs(root.left,x,depth+1,root)
            r = dfs(root.right,x,depth+1,root)
            return l if l else r
        
        dx, px = dfs(root,x)
        dy, py = dfs(root,y)

        return dx==dy and px!=py
        