# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.arr = []
        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            self.arr.append(root.val)
            inOrder(root.right)
            
        inOrder(root)
        node = TreeNode(self.arr[0])
        temp = node
        for i in range(1,len(self.arr)):
            temp.right = TreeNode(self.arr[i])
            temp = temp.right
        return node