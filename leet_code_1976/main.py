class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
    
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v, time in roads:
            adj[u].append((v, time))
            adj[v].append((u, time))
        
        distances = [float('inf')] * n
        ways = [0] * n
        
        # Priority queue: (distance, node)
        heap = []
        heapq.heappush(heap, (0, 0))
        
        distances[0] = 0
        ways[0] = 1
        
        while heap:
            current_dist, u = heapq.heappop(heap)
            
            if u == n - 1:
                break
            
            if current_dist > distances[u]:
                continue
            
            for v, time in adj[u]:
                new_dist = current_dist + time
                
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    ways[v] = ways[u]
                    heapq.heappush(heap, (new_dist, v))
                elif new_dist == distances[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD
        
        return ways[n-1] % MOD