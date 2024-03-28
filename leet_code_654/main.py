# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def TreeBuilder(nums):
            if not nums: return
            root = TreeNode(max(nums))
            root.left = TreeBuilder(nums[:nums.index(max(nums))])
            root.right = TreeBuilder(nums[nums.index(max(nums))+1:])
            return root
        return TreeBuilder(nums)