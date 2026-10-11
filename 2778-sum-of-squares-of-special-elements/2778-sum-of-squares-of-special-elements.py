class Solution(object):
    def sumOfSquares(self, nums):

        n = len(nums)
        special_sum = 0
        for i in range(1, n+1):
            if n % i == 0 :
                special_sum += nums[i-1]**2
                print(special_sum)
        return special_sum

        """
        :type nums: List[int]
        :rtype: int
        """
        