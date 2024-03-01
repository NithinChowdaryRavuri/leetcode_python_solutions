class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        zeros, ones = 0,0
        for c in s:
            if c=='0': zeros+=1
            else: ones+=1
        array = ['1']
        ones-=1
        for _ in range(zeros):
            array.append('0')
        for _ in range(ones):
            array.append('1')
        array = array[::-1]
        return ''.join(array)