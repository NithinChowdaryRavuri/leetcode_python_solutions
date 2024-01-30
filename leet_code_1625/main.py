class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        def get_neighbors(node):
            res = []
            res.append(node[-b:]+node[:-b])
            temp=''
            for i,val in enumerate(node):
                if i%2==0:
                    temp+=val
                else:
                    temp+=str((int(val)+a)%10)
            res.append(temp)
            return res
        queue = [s]
        visited = set()
        result = None
        while queue:
            node = queue.pop()
            if not result or int(node)<int(result):
                result = node
            if node in visited:
                continue
            visited.add(node)
            queue.extend(get_neighbors(node))
        return result
        