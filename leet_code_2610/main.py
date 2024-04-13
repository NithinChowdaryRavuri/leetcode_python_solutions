class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        
        ans = []
        while d:
            temp = []
            to_erase = []
            for f, s in d.items():
                temp.append(f)
                s -= 1
                if s == 0:
                    to_erase.append(f)
                d[f] = s
            ans.append(temp)
            for i in to_erase:
                del d[i]
        return ans