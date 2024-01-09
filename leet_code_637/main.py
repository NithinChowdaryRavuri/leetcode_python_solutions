# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue = deque([root])
        res=[]
        while queue:
            n = len(queue)
            temp,count = 0,0
            for _ in range(n):
                node = queue.popleft()
                temp += node.val
                count += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(float(temp)/count)
        return res