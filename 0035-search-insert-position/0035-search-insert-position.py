class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        if target <= nums[0]:
            return 0
        if target > nums[n-1]:
            return n
        left = 0
        right = n-1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        