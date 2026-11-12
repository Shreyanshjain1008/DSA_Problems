class Solution(object):
    def longestMonotonicSubarray(self, nums):
        inc = desc = 1
        ans = 1
        for i in range (1, len(nums)):

            if nums[i] > nums[i-1]:
                inc += 1
                desc = 1
            elif nums[i] < nums[i-1]:
                inc = 1
                desc += 1
            else:
                inc = desc = 1
            ans = max(ans,inc, desc)
        return ans

        """
        :type nums: List[int]
        :rtype: int
        """
        