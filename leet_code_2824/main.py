class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        count=0
        nums.sort()
        while l<r:
            if nums[l]+nums[r]<target:
                count+=r-l
                l+=1
            else:
                r-=1
        return count