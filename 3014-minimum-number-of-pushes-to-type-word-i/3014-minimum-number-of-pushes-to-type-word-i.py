class Solution(object):
    def minimumPushes(self, word):
        push=0
        for i in range(len(word)):
            push+=i//8+1
        return(push)
            
        

        """
        :type word: str
        :rtype: int
        """
        