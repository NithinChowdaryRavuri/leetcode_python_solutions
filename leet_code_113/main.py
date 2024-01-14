# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        def dfs(root, path=[]):
            if not root:
                return
            path+=[root.val]
            if root.left==root.right==None:
                if sum(path)==targetSum:
                    out.append(path[:])        
            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()
            #return 
        out = []
        dfs(root)
        return out