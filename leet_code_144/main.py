# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        r = []
        r.append(root.val)
        r.extend(self.preorderTraversal(root.left))
        r.extend(self.preorderTraversal(root.right))
        return r