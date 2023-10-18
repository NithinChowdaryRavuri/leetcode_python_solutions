class Solution(object):
    def removeElement(self, nums, val):
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                count+=1
                nums[i] = 100
        nums.sort()
        return len(nums)-count