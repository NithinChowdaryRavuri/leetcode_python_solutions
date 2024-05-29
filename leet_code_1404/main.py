class Solution:
    def numSteps(self, s: str) -> int:
        num, count = int(s, 2), 0
        while num!=1:
            count+=1
            if num%2==0:
                num//=2
            else:
                num+=1
        return count