class Solution(object):
    def maximumLengthSubstring(self, s):
        D = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            D[s[right]] = D.get(s[right], 0) + 1

            while D[s[right]] > 2:
                D[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans

        """
        :type s: str
        :rtype: int
        """
        