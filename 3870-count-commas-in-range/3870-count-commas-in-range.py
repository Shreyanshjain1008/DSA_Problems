class Solution(object):
    def countCommas(self, n):
        if n < 1000:
            return 0
        cnt=0
        for i in range(1000, n+1):
            cnt+=1
        return cnt
        """
        :type n: int
        :rtype: int
        """
        