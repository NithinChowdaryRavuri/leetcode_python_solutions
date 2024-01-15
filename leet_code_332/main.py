class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.res = []
        def dfs(root):
            while graph[root]:
                dfs(graph[root].pop())
            self.res.append(root)
            
        graph = defaultdict(list)
        for t in sorted(tickets)[::-1]:
            graph[t[0]].append(t[1])
        dfs('JFK')
        return self.res[::-1]