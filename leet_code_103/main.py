# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def bfs(root):
            queue = deque([root])
            left_right = False
            res = []
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
                if left_right:
                    res.append(temp[::-1])
                    left_right = False
                else:
                    res.append(temp)
                    left_right = True
            return res
        if not root:
            return
        return bfs(root)
        