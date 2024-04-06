class Solution(object):
    def minRemoveToMakeValid(self, s):
        stack = []
        remove = set()
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if not stack:
                    remove.add(i)
                else:
                    stack.pop()
        remove = remove.union(set(stack))
        return ''.join(c for i, c in enumerate(s) if i not in remove)
                    