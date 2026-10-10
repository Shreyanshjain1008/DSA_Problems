class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        last_seen = {}
        i = 0

        while i < len(nums):
            num = nums[i]

            if num in last_seen:
                if i - last_seen[num] <= k:
                    return True

            last_seen[num] = i
            i += 1
        return False

        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        