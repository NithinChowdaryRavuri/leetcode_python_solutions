class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0

        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        num = 0
        for c in s:
            if not c.isdigit():
                break
            num = num * 10 + int(c)

        num = sign * num
        num = max(-2**31, num)
        num = min(2**31 - 1, num)
        return num