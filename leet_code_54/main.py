class Solution(object):
    def spiralOrder(self, matrix):
        m, n = len(matrix), len(matrix[0])
        r = []
        top, left, bottom, right = 0, 0, m - 1, n - 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                r.append(matrix[top][i])
            top += 1
            for i in range(top, bottom + 1):
                r.append(matrix[i][right])
            right -= 1
            if top<=bottom:
                for i in range(right, left - 1, -1):
                    r.append(matrix[bottom][i])
                bottom -= 1
            if left<=right:
                for i in range(bottom, top - 1, -1):
                    r.append(matrix[i][left])
                left += 1
        return r