class Solution(object):
    def maxSubArray(self, nums):
        running_sum= 0
        max_sum= float('-inf')
        for idx in range( len(nums) ):
                running_sum= max( running_sum + nums[idx], nums[idx])
                max_sum= max(max_sum, running_sum)
        return max_sum
        """
        :type nums: List[int]
        :rtype: int
        """
        