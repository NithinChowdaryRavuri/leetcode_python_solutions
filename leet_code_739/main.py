class Solution(object):
    def dailyTemperatures(self, nums):
        l = [0] * len(nums)
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                curr = stack.pop()
                l[curr] = i - curr
            stack.append(i)
        return l