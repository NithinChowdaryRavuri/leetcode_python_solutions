class Solution(object):
    def longestPalindrome(self, string):
        divalue = {}
        for char in string:
            if char not in divalue.keys():
                divalue.update({char: 1})
            else:
                divalue[char] += 1
        value, count = 0, 0
        for x,y in divalue.items():
            if y%2==0:
                value+=y
            else:
                if count==0:
                    value+=y
                    count+=1
                else:
                    value+=y-1
        return value