class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        def find(nums, target):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l

        if target <= nums[len(nums) - 1]:
            s = find(nums[l:], target)
            return s + l if nums[s + l] == target else -1
        elif nums[0] <= target:
            s = find(nums[:l], target)
            return s if nums[s] == target else -1
        else:
            return -1
