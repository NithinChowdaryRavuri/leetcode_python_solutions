class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(root,path=[0]):
            if path[-1] == n-1:
                out.append(path)
                return
            for child in g[root]:
                dfs(child,path+[child])
            return
        n = len(graph)
        out = []
        g = {node:[] for node in range(n)}
        for i,edge in enumerate(graph):
            g[i].extend(edge)
        dfs(0)
        return out