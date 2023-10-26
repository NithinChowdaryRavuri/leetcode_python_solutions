class Solution(object):
    def countNegatives(self, grid):
        count = 0
        for i in grid:
            for x in i:
                if x < 0:
                    count += 1

        return count