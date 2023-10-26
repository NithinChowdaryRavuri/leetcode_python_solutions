class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        l = 0
        current = 0
        for val in timeSeries:
            if val>=current:
                l+=duration
            else:
                l+=duration-(current-val)
            current = val + duration
        return l