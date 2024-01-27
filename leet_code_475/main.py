class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        max_radius = 0
        for house in houses:
            pos = bisect.bisect_left(heaters, house)
            if pos==0:
                distance = heaters[0]-house
            elif pos==len(heaters):
                distance = house - heaters[-1]
            else:
                distance = min(heaters[pos]-house, house - heaters[pos-1])
            max_radius = max(max_radius, distance)
        return max_radius