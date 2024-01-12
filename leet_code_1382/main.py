# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def builder(arr):
            l,r = 0, len(arr)-1
            if l>r: return
            mid = (l+r)//2
            root = TreeNode(arr[mid])
            root.left = builder(arr[:mid])
            root.right = builder(arr[mid+1:])
            return root
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.arr.append(root.val)
            dfs(root.right)
        self.arr = []
        dfs(root)
        return builder(self.arr)
        