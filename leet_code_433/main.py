class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        d = ["A", "C", "G", "T"]
        queue = deque([startGene])
        level = 0
        visited = set()
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                visited.add(node)
                if node==endGene:
                    return level
                for i in range(8):
                    for char in d:
                        newGene = node[:i]+char+node[i+1:]
                        if newGene in bank and newGene not in visited:
                            queue.append(newGene)
            level+=1
        return -1
