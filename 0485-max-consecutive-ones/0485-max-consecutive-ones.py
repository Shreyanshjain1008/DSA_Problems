class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_cnt = 0
        cnt = 0

        if nums[0] == 1:
            cnt = 1
            max_cnt = 1

        for i in range (len(nums)-1):
            if nums[i+1] == 0:
                cnt = 0
            else:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
        return max_cnt


        """
        :type nums: List[int]
        :rtype: int
        """
        