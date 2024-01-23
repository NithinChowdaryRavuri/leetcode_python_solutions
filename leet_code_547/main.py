class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        def bfs(root):
            queue = deque([root])
            while queue:
                node = queue.popleft()
                for child in graph[node]:
                    if child not in visited:
                        visited.add(child)
                        queue.append(child)
        graph = defaultdict(list)
        rows = len(isConnected)
        cols = len(isConnected[0])
        for i in range(rows):
            for j in range(cols):
                if isConnected[i][j]==1:
                    graph[i+1].append(j+1)
        count, visited = 0, set()
        for i in range(1, rows+1):
            if i not in visited:
                visited.add(i)
                count+=1
                bfs(i)
        return count

                    
        