class Solution(object):
    def containsDuplicate(self, nums):
        dict1 = {}
        for i in nums:
            dict1[i] = dict1.get(i,0)+1
        for i in dict1:
            if dict1[i] >= 2:
                return True
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        