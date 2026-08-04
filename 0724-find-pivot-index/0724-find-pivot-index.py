class Solution(object):
    def pivotIndex(self, nums):
        n=len(nums)
        left_sum=[0] * n
        right_sum=[0] * n
        
        left_sum[0]= nums[0]
        for i in range(1, n):
            left_sum[i]= left_sum[i-1] + nums[i]

        right_sum[n-1]=nums[n-1]
        for i in range(n-2, -1, -1):
            right_sum[i]= right_sum[i+1] + nums[i]

        for i in range(n):
            if left_sum[i] == right_sum[i]:
                return i

        return -1
        """
        :type nums: List[int]
        :rtype: int
        """
        