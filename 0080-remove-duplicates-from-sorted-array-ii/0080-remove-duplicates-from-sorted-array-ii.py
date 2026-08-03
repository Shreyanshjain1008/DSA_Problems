class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        i = 1
        cnt=1
        for j in range(1, len(nums)):
            if nums[j]==nums[j-1]:
                cnt+=1
            else:
                cnt=1
            if cnt<=2:
                nums[i] = nums[j]
                i += 1
        return i 
        
        """
        :type nums: List[int]
        :rtype: int
        """
        