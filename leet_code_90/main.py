class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def rec(nums, start_index, output):
            if start_index == len(nums):
                if output not in res:
                    res.append(output)
                return
            rec(nums, start_index+1, output)
            rec(nums, start_index+1, output+[nums[start_index]])
        res = []
        nums.sort()
        rec(nums, 0, [])
        return res
        