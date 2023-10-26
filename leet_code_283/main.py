class Solution(object):
    def moveZeroes(self, nums):
        if len(nums)==1:
            return nums
        i = 0
        count = 0
        for num in nums:
            if num==0:
                count+=1
            else:
                nums[i] = num
                i+=1
        j = len(nums)-1
        while count>0:
            nums[j]=0
            j-=1
            count-=1