class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        answer = [0]*n
        prefix = [0]*n
        suffix = [0]*n

        prefix[n-1] = 1
        for i in range( n-2, -1, -1):
            prefix[i]=prefix[i+1]*nums[i+1]

        suffix[0] = 1
        for i in range ( 1, n):
            suffix[i]=suffix[i-1]*nums[i-1]
        
        for i in range(n):
            answer[i]=prefix[i]*suffix[i]
            
        return answer

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        