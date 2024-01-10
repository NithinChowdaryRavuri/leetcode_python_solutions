# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        arr = []

        def preorder(root):
            if not root:
                return

            arr.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)

        arr = sorted(arr)
        res = float('inf')

        for i in range(1, len(arr)):
            res = min(res, abs(arr[i]) - abs(arr[i-1]))
        return res