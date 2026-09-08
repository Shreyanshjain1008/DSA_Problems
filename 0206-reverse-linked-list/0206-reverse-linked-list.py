# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        trail = None
        mid = None
        curr = head
        while curr != None:
                trail = mid
                mid = curr
                curr = curr.next
                mid.next = trail
        return mid
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        