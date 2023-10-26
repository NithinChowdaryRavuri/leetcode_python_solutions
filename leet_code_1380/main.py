class Solution(object):
    def luckyNumbers (self, matrix):
        return list({min(row) for row in matrix } & {max(col) for col in zip(*matrix)})