class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l = []
        while head:
            l.append(head.val)
            head = head.next

        sum_indices = {0: -1}
        curr_sum = 0

        for i, num in enumerate(l):
            if num==0:
                l[i]='a'
                continue
            curr_sum += num
            if curr_sum not in sum_indices:
                sum_indices[curr_sum] = i
            else:
                start_index = sum_indices[curr_sum] + 1
                end_index = i
                if l[start_index]!=None:
                    for j in range(start_index, end_index + 1):
                        l[j] = None
                sum_indices[curr_sum] = max(sum_indices[curr_sum], i)

        dummy = ListNode(0)
        current = dummy
        for num in l:
            if num is not None and num!='a':
                current.next = ListNode(num)
                current = current.next

        return dummy.next
