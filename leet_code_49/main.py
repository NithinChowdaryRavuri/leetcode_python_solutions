class Solution(object):
    def groupAnagrams(self, strs):
        dup = []
        check = dict()
        result = []
        for _ in strs:
            temp = ''.join(sorted(_))
            dup.append(temp)
        for i in range(len(dup)):
            if dup[i] in check.keys():
                check[dup[i]].append(strs[i])
            else:
                check[dup[i]] = [strs[i]]
        for _ in check.values():
            result.append(_)
        return result