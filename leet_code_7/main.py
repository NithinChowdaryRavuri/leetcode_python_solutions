class Solution(object):
    def reverse(self, x):
        r = []
        s = str()
        if x == 0:
            return 0
        for i in str(x):
            r.append(i)
        while r[-1]==str(0):
            r.pop()
        if r[0]== "-":
            r=r[1::]
            s+='-'
        for i in r[::-1]:
            s+=i
        return int(s) if -2147483648<=int(s)<=2147483647 else 0