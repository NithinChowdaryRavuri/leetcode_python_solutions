class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for row in grid:
            row.sort()
        max_num = 0
        for i in range(len(grid[0])):
            max_num += max([row[i] for row in grid])
        return max_num
        