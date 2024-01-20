# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return 'x'
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return ' '.join([str(root.val), left, right])

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(nodes):
            val = next(nodes)
            if val=='x':
                return
            root = TreeNode(int(val))
            root.left = dfs(nodes)
            root.right = dfs(nodes)
            return root

        return dfs(iter(data.split()))

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans