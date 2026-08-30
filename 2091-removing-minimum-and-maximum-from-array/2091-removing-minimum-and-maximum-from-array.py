class Solution(object):
    def minimumDeletions(self, nums):
        
        min_val = min(nums)
        max_val = max(nums)
        n = len(nums)

        min_idx = 0
        max_idx = 0

        for i in range(n):
            if nums[i] == min_val:
                min_idx = i

            if nums[i] == max_val:
                max_idx = i

        # Remove both from the front
        front = max(min_idx, max_idx) + 1

        # Remove both from the back
        back = n - min(min_idx, max_idx)

        # Remove one from front and one from back
        
        if max_idx < min_idx:
            front_back = max_idx + 1 + n - min_idx
        else:
            front_back = min_idx + 1 + n - max_idx

        return min(front, back, front_back)
        """
        :type nums: List[int]
        :rtype: int
        """
        