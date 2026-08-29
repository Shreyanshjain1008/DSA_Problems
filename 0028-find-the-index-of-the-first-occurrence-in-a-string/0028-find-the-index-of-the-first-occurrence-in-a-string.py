class Solution(object):
    def strStr(self, haystack, needle):
        i = 0
        j = 0
        k = 0

        while i < len(haystack):

            if haystack[i] == needle[j]:
                i += 1
                j += 1

                if j == len(needle):
                    return k

            else:
                i = k + 1
                k = i
                j = 0

        return -1
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        