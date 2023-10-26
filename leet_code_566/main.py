class Solution(object):
    def matrixReshape(self, mat, r, c):
            rows = len(mat)
            cols = len(mat[0])
            if rows * cols != r * c:
                return mat
            l = [mat[i][j] for i in range(rows) for j in range(cols)]
            l=l[::-1]
            result = []
            for i in range(r):
                b=[]
                for j in range(c):
                    b.append(l.pop())
                result.append(b)
            return result