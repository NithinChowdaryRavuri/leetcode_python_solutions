class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if length<3:
            return False
        stack = []
        max_third = float('-inf')
        for i in range(length-1,-1,-1):
            curr = nums[i]
            if curr<max_third:
                return True
            while stack and stack[-1]<curr:
                max_third = stack.pop()
            stack.append(curr)
        return False

        