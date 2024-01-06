from collections import deque
class Solution(object):
    def slidingPuzzle(self, board):
        init_pos = tuple(tuple(line) for line in board)
        target = ((1,2,3),(4,5,0))
        if init_pos==target:
            return 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        moves_map={init_pos:0}
        moves_queue=deque([init_pos])
        while moves_queue:
            top = moves_queue.popleft()
            row,col=0,0
            for i in range(2):
                for j in range(3):
                    if top[i][j]==0:
                        row,col=i,j
                        break
            for dr,dc in directions:
                new_row = row+dr
                new_col = col+dc
                if 0<=new_row<2 and 0<=new_col<3:
                    new_state = list(list(line) for line in top)
                    new_state[new_row][new_col],new_state[row][col] = new_state[row][col],new_state[new_row][new_col]
                    new_tuple = tuple(tuple(line) for line in new_state)
                    if new_tuple not in moves_map:
                        moves_map[new_tuple] = moves_map[top]+1
                        moves_queue.append(new_tuple)
                        if new_tuple==target:
                            return moves_map[new_tuple]
        return -1
        