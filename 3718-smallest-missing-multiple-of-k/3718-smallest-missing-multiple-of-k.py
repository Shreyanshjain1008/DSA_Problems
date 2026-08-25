class Solution(object):
    def missingMultiple(self, nums, k):
        n=len(nums)
        for i in range( 1, n+1 ):
            if k*i not in nums:
                return k*i
        return k*(i+1)
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        