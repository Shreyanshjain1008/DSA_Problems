class Solution(object):
    def lengthOfLongestSubstring(self, s):
        D = {}
        ans = 0
        left = 0
        for right in range( len(s) ):
            if s[right] in D and D[s[right]]>=left:
                left = D[s[right]]+1
            D[s[right]]=right
            ans=max(ans,right-left+1)
        return ans
        """
        :type s: str
        :rtype: int
        """
        