from Queue import PriorityQueue
class Solution(object):
    def findKthLargest(self, nums, k):
        pq = PriorityQueue()
        for i in nums:
            pq.put(-i)
        for _ in range(k):
            largest = -pq.get() 
        return largest   
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        