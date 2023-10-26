class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        a = set()
        i, j = 0, 0
        while j<len(nums):
            if nums[j] not in a:
                a.add(nums[j])
            else:
                return True
            if j-i<k:
                j+=1
            else:
                a.remove(nums[i])
                i+=1
                j+=1
        return False