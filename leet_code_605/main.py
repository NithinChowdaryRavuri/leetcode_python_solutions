class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        emptyspots = 0
        for i in range(len(flowerbed)):
            if (i == 0 or flowerbed[i - 1] == 0) and flowerbed[i] == 0 and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                emptyspots += 1
        if emptyspots >= n:
            return True
        return False