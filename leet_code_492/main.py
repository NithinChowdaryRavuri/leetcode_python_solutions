class Solution(object):
    def constructRectangle(self, area):
        l = [area, 1]
        d = l[0] - l[1]
        i = 2
        x = 0
        while i * i <= area:
            if area % i == 0:
                x = area // i
                if x - i <= d:
                    l = [x, i]
            i += 1
        return l