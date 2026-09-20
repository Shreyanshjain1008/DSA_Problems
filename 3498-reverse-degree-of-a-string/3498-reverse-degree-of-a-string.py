class Solution(object):
    def reverseDegree(self, s):
        D = {}
        sum = 0

        for i in range(26,0,-1):
            D[chr(123-i)] = i

        for i in range(len(s)):
            sum += (D[s[i]] * (i+1) )

        return sum
        """
        :type s: str
        :rtype: int
        """
        