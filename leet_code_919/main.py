# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        

    def insert(self, val):
        """
        :type val: int
        :rtype: int
        """
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if not node.left:
                node.left = TreeNode(val)
                return node.val
            elif not node.right:
                node.right = TreeNode(val)
                return node.val
            else:
                queue.append(node.left)
                queue.append(node.right)
        

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()