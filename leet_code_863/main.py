# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        graph = defaultdict(list)
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                queue.append(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                queue.append(node.right)
        depth = 0
        queue = deque([target.val])
        visited = set()
        while queue:
            n = len(queue)
            res = []
            for _ in range(n):
                node = queue.popleft()
                if node in visited:
                    continue
                visited.add(node)
                if depth==k:
                    res.append(node)
                queue.extend(graph[node])
            if depth==k:
                return res
            depth+=1
        return []   