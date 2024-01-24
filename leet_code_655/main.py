# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def dfs(grid, root, l, r, level):
            if not root: return
            m = (l+r)//2
            grid[level][m]=str(root.val)
            dfs(grid, root.left, l, m, level+1)
            dfs(grid, root.right, m, r, level+1)
        queue = deque([root])
        depth = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth+=1
        print(depth)
        grid = [[""]*((2**depth)-1) for _ in range(depth)]
        dfs(grid,root, 0, (2**depth)-1, 0)
        return grid
        