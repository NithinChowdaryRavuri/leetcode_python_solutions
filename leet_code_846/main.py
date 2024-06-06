class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0: return False
        def findGroup(i,n):
            next_val = hand[i] + 1
            hand[i] = -1
            count = 1
            i += 1
            while i < n and count < groupSize:
                if hand[i] == next_val:
                    next_val = hand[i] + 1
                    hand[i] = -1
                    count += 1
                i += 1
            return count == groupSize
        hand.sort()
        for i in range(n):
            if hand[i] >= 0:
                if not findGroup(i,n):
                    return False
        return True
        