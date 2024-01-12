# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(root, path=''):
            if not root:
                return
            if root.left==root.right==None:
                path+=str(root.val)
                out.append(path)
            dfs(root.left, path+str(root.val)+'->')
            dfs(root.right, path+str(root.val)+'->')
            
        out = []
        dfs(root)
        return out