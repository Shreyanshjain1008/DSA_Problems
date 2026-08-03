class Solution(object):
    def maxProduct(self, nums):
        nums.sort()
        return (nums[len(nums)-1]-1)*(nums[len(nums)-2]-1)
        
        """
        :type nums: List[int]
        :rtype: int
        """
        