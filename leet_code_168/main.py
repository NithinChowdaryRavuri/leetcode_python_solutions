class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        output = ""
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        while columnNumber:
            r = columnNumber % 26
            output = s[r-1] + output
       
            columnNumber = columnNumber // 26
            if r == 0:
                columnNumber -= 1

        return output
        