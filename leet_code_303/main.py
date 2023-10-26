class NumArray(object):
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        result = sum(self.nums[left:right + 1])
        return result

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)