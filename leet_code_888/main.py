class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        suma=sum(aliceSizes)
        sumb=sum(bobSizes)
        set_b=set(bobSizes)
        target_sum=(suma+sumb)//2
        for candy in aliceSizes:
            diff=target_sum-(suma -candy)
            if diff in set_b:
                return[candy,diff]
        return[]        