class Solution(object):
    def sortArrayByParity(self, nums):
        j=0
        n=len(nums)
        for i in range(n):
            if nums[i]%2==0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
        return nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        