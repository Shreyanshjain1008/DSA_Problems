class Solution(object):
    def reverseWords(self, s):
        str_lst=s.split()
        n=len(str_lst)
        rev=""
        for i in range(n-1,-1,-1):
            rev+=str_lst[i]+" "
        rev=rev.strip()
        return rev
        """
        :type s: str
        :rtype: str
        """
        