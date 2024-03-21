class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        q, res = deque([]), []
        open, close = 0, 0
        for b in s:
            if b == '(':
                open += 1
            else:
                close += 1
            q.append(b)
            if open == close:
                q.popleft()
                q.pop()
                res += q
                q = deque([])
        return "".join(res)