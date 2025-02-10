class Solution:
    def clearDigits(self, s: str) -> str:
        result = []

        for char in s:
            if char in "1234567890":
                result.pop()
            else:
                result.append(char)
        
        return ''.join(result)
        