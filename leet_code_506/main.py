class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        res = []
        arr = score[:]
        val = defaultdict(str)
        arr = sorted(arr, reverse = True)
        for i in range(len(score)):
            if i<3:
                if i==0: val[arr[i]] = 'Gold Medal'
                elif i==1: val[arr[i]] = 'Silver Medal'
                else: val[arr[i]] = 'Bronze Medal'
            else: val[arr[i]] = str(i+1)
        
        for s in score:
            res.append(val[s])
        return res