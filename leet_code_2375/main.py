class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        res = []
        stack = []
        for i in range(len(pattern)):
            if pattern[i] == 'I':
                stack.append(i+1)
                while stack:
                    res.append(stack.pop())
            else:
                stack.append(i+1)
        stack.append(len(pattern)+1)
        while stack:
            res.append(stack.pop())
        return ''.join(map(str, res))