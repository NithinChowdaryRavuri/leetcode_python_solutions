# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_val = root.val
        res = 1
        level = 1
        queue = deque([root])
        while queue:
            n = len(queue)
            temp = []
            for _ in range(n):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if sum(temp)>max_val:
                max_val = sum(temp)
                res = level
            level+=1
        return res
        