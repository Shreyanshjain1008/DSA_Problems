class Solution(object):
    def minSubArrayLen(self, target, nums):
        
        i = 0
        current_sum = 0
        size = float('inf')

        for j in range(len(nums)):
            current_sum += nums[j]

            while current_sum >= target:
                size = min(size, j - i + 1)

                current_sum -= nums[i]
                i += 1

        return size if size != float('inf') else 0
        

        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        