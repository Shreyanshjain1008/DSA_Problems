class Solution(object):
    def wiggleSort(self, nums):
        n = len(nums)
        nums.sort()
        mid = (n - 1) // 2
        end = n - 1
        temp = nums[:]
        j = 0
        for i in range(mid, -1, -1):
            nums[j] = temp[i]
            j += 2
        j = 1
        for i in range(end, mid, -1):
            nums[j] = temp[i]
            j += 2
        return nums
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        