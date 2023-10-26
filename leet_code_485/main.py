class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count, max = 0, 0
        for num in nums:
            if num==1:
                count+=1
            elif num==0:
                if count>max:
                    max=count
                count=0
        if count>max:
            max=count
        return max