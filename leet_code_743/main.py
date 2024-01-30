class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        INF = float('inf')
        graph = defaultdict(list)
        for source, target, weight in times:
            graph[source-1].append((target-1, weight))
        distances = [INF]*n
        distances[k-1] = 0
        min_heap = [(0, k-1)]
        
        while min_heap:
            cur_dist, cur_node = heappop(min_heap)
            for neighbor, weight in graph[cur_node]:
                new_dist = cur_dist+weight
                if distances[neighbor]>new_dist:
                    distances[neighbor]=new_dist
                    heappush(min_heap, (new_dist, neighbor))
        max_delay = max(distances)
        return max_delay if max_delay!=INF else -1