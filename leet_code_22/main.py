class Solution(object):
    def generateParenthesis(self, n):
        open, close = n, n
        result = []
        def gen(result,open, close):
            l=[]
            while open==0 and close!=0:
                result+=[')']
                close-=1
            if open==0 and close==0:
                l.append(''.join(result))
                return l
            if close>open:
                l.extend(gen(result+['('],open-1,close))
                l.extend(gen(result+[')'],open,close-1))
            else:
                l.extend(gen(result+['('],open-1,close))
            return l
        return gen(result, open, close)