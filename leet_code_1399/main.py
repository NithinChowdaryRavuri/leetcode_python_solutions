class Solution:
    def countLargestGroup(self, n: int) -> int:
        sum_counter = Counter()
        max_value = 0
        max_count = 0

        for i in range(1, n+1):
            current_sum = 0

            while i:
                current_sum += i % 10
                i //= 10

            sum_counter[current_sum] += 1

            if max_value < sum_counter[current_sum]:
                max_value = sum_counter[current_sum]
                max_count = 1
            elif max_value == sum_counter[current_sum]:
                max_count += 1
            
        return max_count