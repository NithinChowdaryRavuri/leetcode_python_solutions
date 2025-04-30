class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            value = str(num)
            if len(value) % 2 == 0:
                result += 1
        
        return result