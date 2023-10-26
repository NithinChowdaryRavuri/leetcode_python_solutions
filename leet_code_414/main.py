class Solution(object):
    def thirdMax(self, nums):
        first = second = third = float('-inf')

        for n in nums:
            if n > first:
                third = second
                second = first
                first = n
            elif n > second and n < first:
                third = second
                second = n
            elif n > third and n < second:
                third = n

        if third != float('-inf'):
            return third
        else:
            return first