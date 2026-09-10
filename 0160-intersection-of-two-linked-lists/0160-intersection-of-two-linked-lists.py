# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):

        D = {}

        ptr1 = headA

        while ptr1:
            D[ptr1] = True
            ptr1 = ptr1.next

        ptr2 = headB

        while ptr2:
            if ptr2 in D:
                return ptr2
            ptr2 = ptr2.next

        return None


        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        