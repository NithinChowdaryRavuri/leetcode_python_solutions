class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = defaultdict(int)
        n, result = len(nums), 0

        for i in range(n-1):
            for j in range(i+1, n):
                prod = nums[i] * nums[j]
                count[prod] += 1

        for key, value in count.items():
            if value > 1:
                result += value * (value-1) * 4
        
        return result