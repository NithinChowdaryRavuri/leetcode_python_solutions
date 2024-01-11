# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        def dfs(root):
            if not root:
                return
            if root.left!=None:
                root.left.val = (2*root.val)+1
                self.d.add((2*root.val)+1)
            if root.right!=None:
                root.right.val = (2*root.val)+2
                self.d.add((2*root.val)+2)
            dfs(root.left)
            dfs(root.right)          
        root.val = 0
        self.d = {0}
        dfs(root)
        

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return True if target in self.d else False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)