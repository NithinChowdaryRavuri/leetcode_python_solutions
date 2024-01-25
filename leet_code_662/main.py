# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = deque([(root,1)])
        res = 0
        while queue:
            n = len(queue)
            temp = []
            for _ in range(n):
                node, pos = queue.popleft()
                temp.append(pos)
                if node.left:
                    queue.append((node.left, (2*(pos-1))+1))
                if node.right:
                    queue.append((node.right, (2*(pos-1))+2))
            res = max(res, temp[-1]-temp[0]+1)
        return res
        