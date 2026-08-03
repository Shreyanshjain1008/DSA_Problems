class Solution(object):
    def majorityElement(self, nums):
        
        nums.sort()
        D={}
        majority=0
        element=0
        for i in nums:
            D[i]=D.get(i,0)+1
        for i in D:
            if D[i]>majority:
                majority=D[i]
                element=i
        return element




        
        """
        :type nums: List[int]
        :rtype: int
        """
        