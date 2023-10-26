class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        next_greater = {}
        stack = []

        # Find the next greater element for each number in nums2
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        # Assign -1 for remaining elements in the stack
        while stack:
            next_greater[stack.pop()] = -1
        # Build the result list using the dictionary
        result = []
        for num in nums1:
            result.append(next_greater[num])

        return result