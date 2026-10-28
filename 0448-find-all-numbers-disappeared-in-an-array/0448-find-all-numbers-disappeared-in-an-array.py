class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)

        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])

        ans = []
        for i in range(n):
            if nums[i] > 0:
                ans.append(i + 1)

        return ans
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        