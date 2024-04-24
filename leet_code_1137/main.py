class Solution:
    def tribonacci(self, n: int) -> int:
        zero, one, two, val = 0, 1, 1, 0
        if n in [0,1]:
            return n
        if n == 2: return 1
        num = 3
        while num<=n:
            val = zero + one + two
            zero, one, two = one, two, val
            num += 1
        return val      