class Solution(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        return max(max(amount), (sum(amount) + 1) // 2)