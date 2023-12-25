class Solution(object):
    def minEatingSpeed(self, piles, h):
        def feasible(piles, h, speed):
            return sum((pile - 1) // speed + 1 for pile in piles) <= h
        if h == len(piles):
            return max(piles)
        low, high, ans = 1, max(piles), -1
        while low<=high:
            mid = (low + high) // 2
            if feasible(piles, h, mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans