class Solution(object):
    def diagonalSum(self, mat):
        sum = 0
        l = len(mat)
        j=0
        for i in range(l//2):
            if i<=(l+1)/2:
                sum+=mat[i][j]+mat[i][l-j-1]+mat[l-i-1][j]+mat[l-i-1][l-j-1]
                j+=1
        if l%2!=0:
            num = (l-1)//2
            sum+=mat[num][num]
        return sum