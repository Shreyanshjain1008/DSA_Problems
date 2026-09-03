class Solution(object):
    def longestPalindrome(self, s):
        D = {}
        for i in range (len(s)):
            D[s[i]] = D.get(s[i],0)+1
        n=0
        for i in D:
            if D[i]%2 == 0:
                n+=D[i]
            else:
                n+=(D[i]-1)
        if n<len(s):
            n+=1
        return n
        """
        :type s: str
        :rtype: int
        """
        