class Solution(object):
    def sortColors(self, nums):
        num_zero = len([i for i in nums if i ==0])
        num_one = len([i for i in nums if i ==1])
        num_two = len([i for i in nums if i ==2])

        nums[:] = [0]*num_zero+ [1]*num_one + [2]* num_two