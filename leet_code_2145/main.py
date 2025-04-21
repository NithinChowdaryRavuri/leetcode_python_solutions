class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min, max, curr = 0, 0, 0

        for num in differences:
            curr += num
            if curr < min : 
                min = curr
            if curr > max:
                max = curr

        result  = (upper - lower) - (max - min) + 1

        return result if result >= 0 else 0
        