class Solution(object):
    def productExceptSelf(self, nums):
        l = len(nums)
        sol = [1]*l
        pre = 1
        pos = 1
        for i in range(l):
            sol[i] *= pre
            pre *= nums[i]
            sol[l-i-1] *= pos
            pos *= nums[l-i-1]
        return sol 