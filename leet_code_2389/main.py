class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        def binarySearch(arr, val):
            l,r = 0, len(arr)
            while l<r:
                m = (l+r)//2
                if arr[m]<val:
                    l = m+1
                else:
                    r = m
            if l==len(nums):
                return l
            return l if arr[l]!=val else l+1
        nums.sort()
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        res = []
        for q in queries:
            res.append(binarySearch(nums, q))
        return res
