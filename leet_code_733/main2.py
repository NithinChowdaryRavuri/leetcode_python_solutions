class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        cur = image[sr][sc]
        if cur == color:
            return image
        def dfs(image,r,c):
            if r<0 or c<0 or r>=len(image) or c>=len(image[0]) or image[r][c]!=cur:
                return
            if image[r][c] == cur:
                image[r][c] = color
            dfs(image,r+1,c)
            dfs(image,r-1,c)
            dfs(image,r,c+1)
            dfs(image,r,c-1)
        dfs(image,sr,sc)
        return image
        