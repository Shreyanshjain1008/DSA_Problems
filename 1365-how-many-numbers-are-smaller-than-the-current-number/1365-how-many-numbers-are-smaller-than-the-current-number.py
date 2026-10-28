class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        cnt = [0]*101
        for num in nums:
            cnt[num] += 1
        for i in range(1, 101):
            cnt[i] += cnt[i-1]
        
        ans = []
        for i in nums:
            if i == 0:
                ans.append(0)
            else:
                ans.append(cnt[i-1])
        return ans
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        