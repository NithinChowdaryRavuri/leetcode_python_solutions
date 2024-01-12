# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.cur_max = 1 if self.prev!=root.val else self.cur_max+1
            if self.cur_max==self.max_val:
                self.res.append(root.val)
            if self.cur_max > self.max_val:
                self.res = [root.val]
                self.max_val = self.cur_max
            self.prev = root.val
            dfs(root.right)
        self.res=[]
        self.cur_max=0
        self.max_val=0
        self.prev=None
        dfs(root)
        return self.res
        