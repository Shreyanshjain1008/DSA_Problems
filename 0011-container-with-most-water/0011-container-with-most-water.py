class Solution(object):
    def maxArea(self, height):
        ans = 0
        n=len(height)
        i=0
        j=n-1
        while i<j:
            ans=max(ans,(j-i)*min(height[i],height[j]))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return ans
        """
        :type height: List[int]
        :rtype: int
        """
        