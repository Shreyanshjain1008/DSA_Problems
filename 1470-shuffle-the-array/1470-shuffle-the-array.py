class Solution(object):
    def shuffle(self, nums, n):
        result = []
        i = 0
        j = n
        while j < 2*n:
            result.append(nums[i])
            i += 1
            result.append(nums[j])
            j += 1
        return result

        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        