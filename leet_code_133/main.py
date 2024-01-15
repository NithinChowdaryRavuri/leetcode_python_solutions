"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        def bfs(node):
            if not node: return
            queue = deque([node])
            visited = set()
            d = {}
            while queue:
                root = queue.popleft()
                visited.add(root.val)
                if root.val not in d:
                    d[root.val] = Node(root.val)
                if root.neighbors!=[]:
                    for neighbor in root.neighbors:
                        if neighbor.val not in d:
                            d[neighbor.val] = Node(neighbor.val)
                            queue.append(neighbor)
                        d[root.val].neighbors.append(d[neighbor.val])
            return d[node.val]
        return bfs(node)