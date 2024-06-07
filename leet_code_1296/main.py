class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n%k != 0: return False
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        nums.sort()
        for num in nums:
            if d[num] > 0:
                for curr in range(num, num+k):
                    if d[curr] == 0:
                        return False
                    d[curr] -= 1
        return True