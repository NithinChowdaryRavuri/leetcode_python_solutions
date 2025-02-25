class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd, even, total, result = 0, 1, 0, 0

        for num in arr:
            total += num
            if total % 2 == 0:
                result = (result + odd) 
                even += 1
            else:
                result = (result + even)
                odd += 1
        
        return result % MOD