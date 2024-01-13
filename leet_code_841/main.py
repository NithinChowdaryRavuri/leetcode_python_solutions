class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        def bfs(root):
            queue = deque([root])
            while queue:
                node = queue.popleft()
                visited.add(node)
                for key in graph[node]:
                    if key not in visited:
                        queue.append(key)
        n = len(rooms)
        visited = set()
        graph = {node:[] for node in range(n)}
        for i, keys in enumerate(rooms):
            graph[i].extend(keys)
        bfs(0)
        return n==len(visited)