# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = deque([root])
        res = []
        while queue:
            n = len(queue)
            temp = []
            for _ in range(n):
                node = queue.popleft()
                if node is None:
                    temp.append(-500)
                    continue
                temp.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            res.append(temp)
        for i in range(1,len(res)):
            temp = res[i]
            n = len(temp)
            if n%2 != 0:
                return False
            if temp[:n//2]!=temp[n-1:(n//2)-1:-1]:
                return False
        return True