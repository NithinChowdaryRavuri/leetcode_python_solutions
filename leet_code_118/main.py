class Solution(object):
    def generate(self, numRows):
        result = [[1], [1,1]]
        last = result[-1]
        if numRows==1:
            return [[1]]
        if numRows==2:
            return result
        for i in range(3,numRows+1):
            temp = []
            for j in range(len(last)-1):
                temp+= [last[j]+last[j+1]]
            temp = [1]+temp+[1]
            last = temp
            result.append(temp)
        return result