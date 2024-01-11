class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        def bfs(root):
            queue = deque([root])
            visited = set([root])
            while queue:
                node = queue.popleft()
                if node == destination:
                    return True
                for child in graph[node]:
                    if child not in visited:
                        visited.add(child)
                        queue.append(child)
            return False

        graph = {node:[] for node in range(n)}
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        return bfs(source)
        