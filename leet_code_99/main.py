# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root: return
            dfs(root.left)
            stack.append(root)
            if len(stack)>1 and stack[-1].val<stack[-2].val:
                a.append(len(stack)-2)
            dfs(root.right)
            
        a = []
        stack = []
        dfs(root)
        stack[a[0]].val, stack[a[-1]+1].val = stack[a[-1]+1].val, stack[a[0]].val
        
        
        
        