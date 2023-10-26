class Solution(object):
    def buddyStrings(self, s, goal):
        count = 0
        d = []
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)
        for i in range(len(s)):
            if s[i] != goal[i]:
                count += 1
                d.append(i)
        if count != 2:
            return False
        return s[d[0]] == goal[d[1]] and s[d[1]] == goal[d[0]]

