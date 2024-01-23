# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def replaceValueInTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        levelmap = defaultdict(int)
        def dfs(root, level=0):
            if not root: return
            levelmap[level]+=root.val
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        dfs(root)
        def dfs(root, level, sibling):
            if not root: return
            root.val = levelmap[level]-root.val-sibling
            left = root.left.val if root.left else 0
            right = root.right.val if root.right else 0
            if root.left:
                dfs(root.left, level+1, right)
            if root.right:
                dfs(root.right, level+1, left)
            return root
        return dfs(root, 0, 0)

        