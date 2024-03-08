class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict(int)
        max_val = -1
        for num in nums:
            d[num]+=1
            max_val = max(max_val, d[num])
        res=0
        for val in d.values():
            if val==max_val:
                res+=1
        return res*max_val