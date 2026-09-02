class Solution(object):
    def maximumSubarraySum(self, nums, k):

        D={}
        max_sum = 0
        ans = 0
        i,j = 0,0
        n = len(nums)

        while j<n:
            D[nums[j]] = D.get(nums[j],0)+1
            ans+=nums[j]
            if j-i+1 == k:
                if len(D) == k:
                    max_sum = max(max_sum, ans)
                D[nums[i]]-=1
                if D[nums[i]] == 0:
                    del D[nums[i]]
                ans-=nums[i]
                i+=1
            j+=1
        return max_sum
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        