class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        pos = 0
        for i in range(n):
            if nums[i] > 0:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
        for i in range(pos):
            index = abs(nums[i])
            if 1 <= index <= pos:
                nums[index - 1] = -abs(nums[index - 1])
        for i in range(pos):
            if nums[i] > 0:
                return i + 1

        return pos + 1
        """
        :type nums: List[int]
        :rtype: int
        """
        