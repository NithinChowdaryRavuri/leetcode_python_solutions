class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_val = min(nums)
        max_val = max(nums)
        count = [0]*(max_val-min_val+1)

        for num in nums:
            count[num-min_val]+=1

        for i in range(len(count)-1,-1,-1):
            k-=count[i]
            if k<=0:
                return i+min_val