class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binarySearch(nums, target):
            l, r = 0, len(nums)
            while l<r:
                m = (l+r)//2
                if nums[m]<target:
                    l = m+1
                else:
                    r = m
            return l
        nums.sort()
        start = binarySearch(nums, target)
        if start==len(nums) or nums[start]!=target:
            return []
        end = binarySearch(nums, target+1)
        return [i for i in range(start,end)]
