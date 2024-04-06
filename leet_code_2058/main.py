# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        criticals = []
        min_distance = float('inf')

        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] > nums[i + 1] or nums[i - 1] > nums[i] < nums[i + 1]:
                criticals.append(i)
                if len(criticals) >= 2:
                    d = criticals[-1] - criticals[-2]
                    if d < min_distance:
                        min_distance = d

        if len(criticals) < 2:
            return [-1, -1]

        max_distance = criticals[-1] - criticals[0]
        return [min_distance, max_distance]