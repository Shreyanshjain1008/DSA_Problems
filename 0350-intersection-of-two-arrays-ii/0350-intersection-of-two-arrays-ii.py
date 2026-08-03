class Solution(object):
    def intersect(self, nums1, nums2):
        D1={}
        D2={}
        arr3=[]
        for i in nums1:
            D1[i]=D1.get(i,0)+1
        for j in nums2:
            D2[j]=D2.get(j,0)+1
        for x in D1:
            if x in D2:
                arr3.extend([x] * min(D1[x], D2[x]))
        return arr3
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        