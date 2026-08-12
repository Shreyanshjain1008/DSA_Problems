class Solution(object):
    def merge(self, nums):
        nums.sort(key=lambda x:x[0])
        n=len(nums)
        ans=[]
        s=nums[0][0]
        e=nums[0][1]
        for i in range(1,n):
            if e>=nums[i][0]:
                e=max(e,nums[i][1])
            else:
                ans.append([s,e])
                s=nums[i][0]
                e=nums[i][1]
        ans.append([s,e])
        return ans
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        