class Solution(object):
    def minMoves(self, nums):
        max_num = max(nums)
        moves = 0
        for i in nums:
            moves += (max_num - i)
        return moves
        """
        :type nums: List[int]
        :rtype: int
        """
        