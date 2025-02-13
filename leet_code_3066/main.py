class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = 0
        heapq.heapify(nums)

        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            value = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, value)
            result += 1
        
        return result