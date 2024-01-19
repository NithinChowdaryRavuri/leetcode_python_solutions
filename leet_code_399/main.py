class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def dfs(root, target, value = 1):
            if root in seen:
                return -1.0
            if root==target:
                return value
            seen.add(root)
            for neighbor, edge in graph[root]:
                if neighbor not in seen:
                    updated_value= value * edge
                    result = dfs(neighbor, target, updated_value)
                    if result!=-1:
                        return result
            return -1

        graph = defaultdict(list)
        for (src,dest), value in zip(equations, values):
            graph[src].append((dest, value))
            graph[dest].append((src, 1/value))
        out = []
        for start,end in queries:
            if start not in graph or end not in graph:
                out.append(-1)
            else:
                seen = set()
                out.append(dfs(start, end))
        return out