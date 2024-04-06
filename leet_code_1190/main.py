class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in s:
            if i == ")":
                temp = ""
                while stack[-1] != "(":
                    temp += stack.pop()
                stack.pop()
                for j in temp:
                    stack.append(j)
            else:
                stack.append(i)
        return "".join(stack)