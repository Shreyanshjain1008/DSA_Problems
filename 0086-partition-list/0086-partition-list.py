# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def add(self,node):
        self.tail.next = node
        self.tail = node
        
class Solution(object):
    def partition(self, head, x):

        L1 = LinkedList()
        L2 = LinkedList()
        curr = head

        while curr:
            if curr.val < x:
                L1.add(curr)
            
            else:
                L2.add(curr)
            curr = curr.next

        L2.tail.next = None
        L1.tail.next = L2.head.next
        
        return L1.head.next
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        