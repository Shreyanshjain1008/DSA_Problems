# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        cnt = 0
        ptr = head
        #count nodes
        while ptr != None:
            cnt += 1
            ptr = ptr.next

        # remove head node
        if cnt == n:
            return head.next

        #nth node
        ptr=head
        for i in range( cnt-n-1 ):
            ptr = ptr.next
        ptr.next = ptr.next.next

        return head
        
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        