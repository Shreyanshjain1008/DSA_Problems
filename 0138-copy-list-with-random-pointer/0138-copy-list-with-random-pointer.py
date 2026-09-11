"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):

        D = {}
        curr = head
        while curr:
                copy = Node(curr.val,None,None)
                D[curr] = copy
                curr = curr.next
        curr = head
        while curr:
                copy = D.get(curr)
                copy.next = D.get(curr.next)
                copy.random = D.get(curr.random)
                curr = curr.next
        return D.get(head)

        """
        :type head: Node
        :rtype: Node
        """
        