class Solution(object):
    def findDifference(self, nums1, nums2):
        return [set(nums1).difference(set(nums2)), set(nums2).difference(set(nums1))]