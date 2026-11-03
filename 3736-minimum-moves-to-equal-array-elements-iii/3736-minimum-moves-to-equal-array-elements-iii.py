class Solution(object):
    def minMoves(self, nums):
        #  Approch-1  :
        
        max_num = max(nums)
        moves = 0
        for i in nums:
            moves += (max_num - i)
        return moves
        
        #  Approch-2  :
        """
        max_num = max(nums)
        total = sum(nums)
        return max_num * len(nums) - total
        """

        """
        :type nums: List[int]
        :rtype: int
        """
        