# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def bfs(root):
            queue = [root]
            level = 0
            while queue:
                temp = []
                for node in queue:
                    if node.left is not None: temp.append(node.left)
                    if node.right is not None: temp.append(node.right)
                if level%2==1:
                    i, j = 0, len(queue)-1
                    while i<j:
                        queue[i].val,queue[j].val = queue[j].val,queue[i].val
                        i += 1
                        j -= 1
                level += 1
                queue = temp
        bfs(root)
        return root