class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r, m = defaultdict(int), defaultdict(int)
        for c in magazine:
            m[c] += 1
        for c in ransomNote:
            r[c] += 1
            if r[c] > m[c]: return False
        return True