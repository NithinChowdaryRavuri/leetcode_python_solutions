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
        def get_neighbours(r,c):
            row, col = r,c
            move_r = [-1,0,1,0]
            move_c = [0,1,0,-1]
            res = []
            for i in range(4):
                nr = row + move_r[i]
                nc = col + move_c[i]
                if nr<0 or nc<0 or nr>=rows or nc>=cols:
                    continue
                res.append((nr,nc))
            return res
        def bfs(image, sr, sc):
            queue = deque([(sr,sc)])
            while len(queue)>0:
                node = queue.popleft()
                image[node[0]][node[1]] = color
                for r, c in get_neighbours(*node):
                    if image[r][c]!=cur:
                        continue
                    queue.append((r,c))
        rows = len(image)
        cols = len(image[0])
        bfs(image,sr,sc)
        return image
        