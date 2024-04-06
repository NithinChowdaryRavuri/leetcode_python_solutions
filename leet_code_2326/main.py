# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        # get the length of the linked list
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
            
        # create the matrix
        matrix = [[-1 for i in range(n)] for j in range(m)]
        i = 0
        j = 0
        row = 0
        col = 0
        row_end = m - 1
        col_end = n - 1
        while row <= row_end and col <= col_end:
            # move right
            for j in range(col, col_end + 1):
                if head:
                    matrix[row][j] = head.val
                    head = head.next
            row += 1
            # move down
            for i in range(row, row_end + 1):
                if head:
                    matrix[i][col_end] = head.val
                    head = head.next
            col_end -= 1
            # move left
            if row <= row_end:
                for j in range(col_end, col - 1, -1):
                    if head:
                        matrix[row_end][j] = head.val
                        head = head.next
                row_end -= 1
            # move up
            if col <= col_end:
                for i in range(row_end, row - 1, -1):
                    if head:
                        matrix[i][col] = head.val
                        head = head.next
                col += 1
        return matrix
        