class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls, colors = defaultdict(int), defaultdict(int)
        result = []

        for query in queries:
            if query[0] in balls:
                colors[balls[query[0]]] -= 1
                if colors[balls[query[0]]] == 0: 
                    del colors[balls[query[0]]]
            balls[query[0]] = query[1]
            colors[query[1]] += 1
            result.append(len(colors))
        
        return result
        