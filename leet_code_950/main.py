class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        n = len(deck)
        q = collections.deque()
        for i in range(n-1, -1, -1):
            if q:
                q.appendleft(q.pop())
            q.appendleft(deck[i])
        return list(q)