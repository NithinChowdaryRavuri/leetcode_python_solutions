class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        result, n = [], len(part)
        
        for index, value in enumerate(s):
            result.append(value)
            if len(result) >= n and ''.join(result[-n:]) == part:
                for _ in range(n):
                    result.pop()
                    
        return ''.join(result)  