class Solution(object):
    def isPalindrome(self, s):
        str_1 = ""
        for i in s:
            if i.isalnum():
                str_1 += i.lower()
        if str_1 == str_1[::-1]:
            return True

        return False

        """
        :type s: str
        :rtype: bool
        """
        