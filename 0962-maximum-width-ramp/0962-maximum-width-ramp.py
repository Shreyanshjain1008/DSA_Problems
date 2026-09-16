class Solution:
    def maxWidthRamp(self, nums):
        stack = []

        # Store indices where nums[i] is a new minimum
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        ans = 0

        # Traverse from right to left
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                ans = max(ans, j - stack.pop())

        return ans
        """
        :type nums: List[int]
        :rtype: int
        """
        