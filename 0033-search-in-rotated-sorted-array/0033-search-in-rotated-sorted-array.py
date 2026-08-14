class Solution(object):
    def search(self, nums, target):
        n=len(nums)
        s=0
        e=n-1
        ans=-1
        while s<=e:
            mid=s+(e-s)//2
            if nums[mid]==target:
                return mid
            if nums[s]<=nums[mid]:
                if nums[s]<=target and nums[mid]>=target:
                    e=mid-1
                else:
                    s=mid+1
            else:
                if nums[mid]<=target and nums[e]>=target:
                    s=mid+1
                else:
                    e=mid-1
        return -1
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        