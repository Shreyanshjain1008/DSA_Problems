
class Solution(object):
    def maxProfit(self, prices):
        mini=prices[0]
        ans=0
        for i in range(1,len(prices)):
            ans=max(ans,prices[i]-mini)
            mini=min(prices[i],mini)
        return ans
        """
        :type prices: List[int]
        :rtype: int
        """
        