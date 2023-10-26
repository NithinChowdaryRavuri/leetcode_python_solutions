class Solution(object):
    def findDisappearedNumbers(self, nums):
        l = len(nums)
        c = set(nums)
        result = [i for i in range(1, l + 1) if i not in c]
        return result