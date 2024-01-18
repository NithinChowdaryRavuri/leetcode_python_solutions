class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums)-1
        while l<=r:
            while l<r and nums[l]==nums[l+1]:
                l+=1
            while l<r and nums[r]==nums[r-1]:
                r-=1
            m = (l+r)//2
            if nums[m]==target:
                return True
            elif nums[l]<=nums[m]:
                if nums[m]>=target and nums[l]<=target:
                    r = m-1
                else:
                    l = m+1
            else:
                if target>=nums[m] and target<=nums[r]:
                    l = m+1
                else:
                    r = m-1
        return False