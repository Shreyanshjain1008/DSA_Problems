import re
class Solution(object):
    def countSegments(self, s):
        
        words = re.findall(r'\S+', s)
        return len(words)


        """
        :type s: str
        :rtype: int
        """
        