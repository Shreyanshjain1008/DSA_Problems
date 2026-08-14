class Solution(object):
    def searchRange(self, arr, k):
        n=len(arr)
        s,e=0,n-1
        lb,ub=-1,-1
        while s<=e:
            mid=s+(e-s)//2
            if arr[mid]<k:
                s=mid+1
            else:
                e=mid-1
        if s<n and arr[s]==k:
            lb=s

        s,e=0,n-1
        while s<=e:
            mid=s+(e-s)//2
            if arr[mid]>k:
                e=mid-1
            else:
                s=mid+1
        if e>=0 and arr[e]==k:
            ub=e
        return [lb,ub]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        