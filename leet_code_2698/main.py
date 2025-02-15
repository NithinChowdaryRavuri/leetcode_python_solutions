class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_split_to_original(num_str: str, start_index: int, target_sum: int) -> bool:
            num_length = len(num_str)
            if start_index >= num_length:
                return target_sum == 0
            
            current_num = 0

            for j in range(start_index, num_length):
                current_num = current_num * 10 + int(num_str[j])
                if current_num > target_sum:
                    break
                if can_split_to_original(num_str, j + 1, target_sum - current_num):
                    return True
            return False
            
        result = 0

        for i in range(1, n+1):
            square = i * i
            if can_split_to_original(str(square), 0, i):
                result += square
        
        return result