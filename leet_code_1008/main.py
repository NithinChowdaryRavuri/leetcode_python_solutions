# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        def TreeBuilder(nums):
            if not nums: return
            root = TreeNode(nums[0])
            left = [n for n in nums if n < nums[0]]
            right = [n for n in nums if n > nums[0]]
            root.left = TreeBuilder(left)
            root.right = TreeBuilder(right)
            return root
        return TreeBuilder(preorder)