class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        def get_neighbors(node):
            res = []
            for i, val in enumerate(node):
                num = int(val)
                res.append(node[:i]+str((num-1)%10)+node[i+1:])
                res.append(node[:i]+str((num+1)%10)+node[i+1:])
            return res
        queue = deque(['0000'])
        visited = set(deadends)
        depth = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node==target:
                    return depth
                if node in visited:
                    continue
                visited.add(node)
                queue.extend(get_neighbors(node))
            depth+=1
        return -1