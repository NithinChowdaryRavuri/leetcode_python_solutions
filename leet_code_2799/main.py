class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique_count = len(set(nums))
        freq_count = Counter()
        total_subarrays, length = 0, len(nums)

        start_index = 0

        for end_index, value in enumerate(nums):
            freq_count[value] += 1

            while len(freq_count) == unique_count:
                total_subarrays += length - end_index

                freq_count[nums[start_index]] -= 1

                if freq_count[nums[start_index]] == 0:
                    freq_count.pop(nums[start_index])

                start_index += 1
        
        return total_subarrays