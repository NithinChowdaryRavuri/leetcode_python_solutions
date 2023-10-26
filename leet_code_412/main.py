class Solution(object):
    def fizzBuzz(self, n):
        out = []
        for i in range(1,n+1):
            res = ""
            if i%3 == 0:
                res+="Fizz"
            if i%5 == 0:
                res+="Buzz"
            if res == "":
                res+=str(i)
            out.append(res)
        return out