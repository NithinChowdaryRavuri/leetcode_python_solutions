class Solution(object):
    def updateBoard(self, board, click):
        rows = len(board)
        cols = len(board[0])
        def check(i,j):
            count = 0
            directions = [(-1,-1), (-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
            for d in directions:
                nr = i+d[0]
                nc = j+d[1]
                if 0<=nr<rows and 0<=nc<cols:
                    if board[nr][nc]=='M':
                        count+=1
            return count
        if board[click[0]][click[1]]=='M':
            board[click[0]][click[1]]='X'
            return board
        queue = deque([(click[0], click[1])])
        directions = [(-1,-1), (-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        visited = set()
        while queue:
            r,c = queue.popleft()
            if check(r,c)==0:
                board[r][c]='B'
                for d in directions:
                    nr = r+d[0]
                    nc = c+d[1]
                    if 0<=nr<rows and 0<=nc<cols and board[nr][nc]=='E' and (nr,nc) not in visited:
                        queue.append((nr,nc))
                        visited.add((nr,nc))
            else: board[r][c]=str(check(r,c))
        return board