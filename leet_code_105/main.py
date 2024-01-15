# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def builder(preorder, inorder):
            if not inorder or not preorder: return
            root = TreeNode(preorder[0])
            index = inorder.index(root.val)
            root.left = builder(preorder[1:index+1],inorder[:index]) 
            root.right = builder(preorder[index+1:],inorder[index+1:])
            return root
        return builder(preorder, inorder)