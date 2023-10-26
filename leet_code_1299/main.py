class Solution(object):
    def replaceElements(self, arr):
        maxNum = -1
        for i in range(len(arr)-1, -1,-1):
            temp = arr[i]
            arr[i] = maxNum
            if temp > maxNum:
                maxNum = temp
        return arr