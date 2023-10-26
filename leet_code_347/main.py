from collections import *
class Solution(object):
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        res = counter.most_common(k)
        result = []
        for _ in res:
            result.append(_[0])
        return result