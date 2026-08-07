class Solution(object):
    def twoSum(self, nums, target):
        D = {}
        n = len(nums)
        for i in range(n):
            if target-nums[i] in D:
                return [i,D[target-nums[i]]]
            D[nums[i]] =  i
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        