class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        val = defaultdict(int)
        for c in s:
            val[c]+=1
        res = []
        for key,value in val.items():
            res.append([key, value])
        res = sorted(res, key=lambda x: x[1], reverse=True)
        string = []
        for e in res:
            for _ in range(e[1]):
                string.append(e[0])
        return ''.join(string)