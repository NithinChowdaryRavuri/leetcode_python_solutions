class Solution(object):
    def subsets(self, nums, output=[], index=0):
        l = []
        if index==len(nums):
            l.append(output)
            return l
        l.extend(self.subsets(nums, output, index+1))
        l.extend(self.subsets(nums,output+[nums[index]], index+1))
        return l