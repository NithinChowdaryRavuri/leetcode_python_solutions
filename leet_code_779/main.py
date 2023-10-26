class Solution(object):
    def kthGrammar(self, n, k):
        def solve(n, k):
            if n == 1 and k == 1 or n == 2 and k == 1:
                return 0
            if n == 2 and k == 2:
                return 1
            mid = 2 ** (n - 2)
            if k <= mid:
                return solve(n - 1, k)
            else:
                return not solve(n - 1, k - mid)

        return 1 if solve(n, k) == True else 0
