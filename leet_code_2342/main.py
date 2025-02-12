class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        count  = {}

        for num in nums:
            number = num
            val = 0
            while num > 0:
                val += num%10
                num = num // 10
            if val not in count:
                count[val] = [number]
            else:
                heapq.heappush(count[val], number)
                if len(count[val]) > 2:
                    heapq.heappop(count[val])
        
        result = -1
        for value in count.values():
            if len(value) == 2:
                result = max(result, value[0] + value[1])
        
        return result
