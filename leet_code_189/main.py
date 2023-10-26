class Solution(object):
    def rotate(self, nums, k):
        if len(nums)==2:
            if k%2!=0:
               nums[:] =  nums[::-1]
        else:
            nums[:] = nums[len(nums)-k::] + nums [:len(nums)-k:]