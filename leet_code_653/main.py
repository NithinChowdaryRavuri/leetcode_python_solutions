# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        d = dict()
        queue = deque([root])
        while queue:
            node = queue.popleft()
            target = k - node.val
            if target in d:
                return True
            else:
                d[node.val]=0
            if node.left!=None:
                queue.append(node.left)
            if node.right!=None:
                queue.append(node.right)
        return False
        