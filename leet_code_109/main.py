# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        
        def convert_to_array(head):
            arr = []
            while head:
                arr.append(head.val)
                head = head.next
            
            return arr
        
        def dfs(l, r):
            if l > r:
                return None
            
            mid = (l+r)/2
            root = TreeNode(arr[mid])
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root
        
        arr = convert_to_array(head)
        return dfs(0, len(arr)-1)