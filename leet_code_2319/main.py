class Solution(object):
    def checkXMatrix(self, grid):
        length = len(grid)
        for i in range(length):
            if grid[i][i] == 0 or grid[i][length - i - 1] == 0:
                return False
            else:
                grid[i][i], grid[i][length - i - 1] = 0, 0
        return grid == [[0 for _ in range(length)] for _ in range(length)]
