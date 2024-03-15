class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos, neg, res = [], [], []
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        return res