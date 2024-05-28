class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        values = []
        for i in range(len(s)):
            values.append(abs(ord(s[i]) - ord(t[i])))
        window, ans = 0, 0
        left = 0
        for right in range(len(s)):
            window += values[right]
            while window > maxCost:
                window -= values[left]
                left += 1
            ans = max(ans, right-left+1)
        return ans

        