# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        out = [0]
        def check(path):
            count = 0
            for values in path.values():
                if values%2==1:
                    count+=1
            if count<=1:
                out[0]+=1
        def dfs(root, path):
            if not root: return
            path[root.val]+=1
            left = dfs(root.left, path)
            right = dfs(root.right, path)
            if left==right==None:
                check(path)
            path[root.val]-=1
            return root
        path = defaultdict(int)
        dfs(root, path)
        return out[0]