class Solution(object):
    def lengthOfLastWord(self, s):
        a = s.strip().split(" ")
        return len(a[len(a)-1])

        """
        :type s: str
        :rtype: int
        """
        