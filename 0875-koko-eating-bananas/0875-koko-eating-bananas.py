class Solution(object):
        
    def minEatingSpeed(self, piles, h):
        s=1
        e=max(piles)
        ans=-1
        n=len(piles)
        while s<=e:
            mid=(s+e)//2
            if (self.helper(piles,n,mid))<=h:
                ans=mid
                e=mid-1
            else:
                s=mid+1
        return ans

    def helper(self,a,n,speed):
        hreq=0
        for i in range(n):
            hreq+=ceil(a[i]*1.0/speed*1.0)
        return hreq
    

        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        