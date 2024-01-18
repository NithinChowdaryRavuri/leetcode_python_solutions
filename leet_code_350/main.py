class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1, d2 = defaultdict(int), defaultdict(int)
        res = []
        c1, c2 = 0, 0
        for num in nums1:
            c1+=1
            d1[num]+=1
        for num in nums2:
            c2+=1
            d2[num]+=1
        if c1<c2:
            for key in d1.keys():
                if key in d2:
                    res.extend([key]*(min(d1[key], d2[key])))
        else:
            for key in d2.keys():
                if key in d1:
                    res.extend([key]*(min(d1[key], d2[key])))
        return res