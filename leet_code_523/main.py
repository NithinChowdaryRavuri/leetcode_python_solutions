class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        remainder_dict = {0:-1}
        for index, value in enumerate(nums):
            prefix += value
            remainder = prefix % k
            if remainder in remainder_dict and index - remainder_dict[remainder] >=2:
                return True
            if remainder not in remainder_dict:
                remainder_dict[remainder] = index
        return False