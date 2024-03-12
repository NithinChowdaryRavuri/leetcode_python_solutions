class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        first = []
        for c in s:
            if c!='#':
                first.append(c)
            else:
                if first:
                    first.pop()
        second = []
        for c in t:
            if c!='#':
                second.append(c)
            else:
                if second:
                    second.pop()
        return ''.join(first)==''.join(second)