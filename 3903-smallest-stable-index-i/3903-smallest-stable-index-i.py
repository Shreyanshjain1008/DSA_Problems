class Solution(object):
    def firstStableIndex(self, nums, k):

        for num in range(len(nums)):

            max_val = 0
            min_val = float('inf')

            i = 0
            j = num

            while i <= num:
                max_val = max(max_val, nums[i])
                i += 1

            while j < len(nums):
                min_val = min(min_val, nums[j])
                j += 1

            if max_val - min_val <= k:
                return num

        return -1


        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        