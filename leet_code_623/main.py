# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        if depth==1:
            Root = TreeNode(val, root)
            return Root
        queue = deque([root])
        level = 2
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if level==depth:
                    left = node.left
                    right = node.right
                    node.left = TreeNode(val,left)
                    node.right = TreeNode(val,None, right)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if level==depth: break
            level+=1
        return root