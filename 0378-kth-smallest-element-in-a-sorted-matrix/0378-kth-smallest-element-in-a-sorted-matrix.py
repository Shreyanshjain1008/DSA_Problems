class Solution(object):

    def helper(self,a,n,m,mid):
        i=0
        j=m-1
        cnt=0
        while i<n and j>=0:
            if a[i][j]<=mid:
                cnt+=j+1
                i+=1
            else:
                j-=1
        return cnt

    def kthSmallest(self, a, k):
        n = len(a)
        m = len(a[0])

        s = a[0][0]
        e = a[n-1][m-1]
        ans = -1

        while s<=e:
            mid = (s+e)//2
            if self.helper(a,n,m,mid)<k:
                s = mid+1
            else:
                ans = mid
                e=mid-1
        return ans


        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        