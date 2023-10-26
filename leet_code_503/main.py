class Solution(object):
    def nextGreaterElements(self, nums):
        l = len(nums)
        r = [-1] * l
        stack = []
        for i in range(l):
            while stack and nums[i] > nums[stack[-1]]:
                r[stack.pop()] = nums[i]
            stack.append(i)
        for i in range(l):
            while stack and nums[i] > nums[stack[-1]]:
                r[stack.pop()] = nums[i]
        return r