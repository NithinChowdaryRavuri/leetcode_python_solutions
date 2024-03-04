class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()
        i, j = 0, len(tokens)-1
        score = 0
        while i<=j:
            if tokens[i]<=power:
                score+=1
                power-=tokens[i]
                i+=1
            elif score>0 and j>i:
                score-=1
                power+=tokens[j]
                j-=1
            else:
                break
        return score