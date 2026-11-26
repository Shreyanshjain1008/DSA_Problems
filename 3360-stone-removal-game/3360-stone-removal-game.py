class Solution(object):
    def canAliceWin(self, n):
        move = 10
        count = 0

        while n >= move:
            n -= move
            move -= 1
            count += 1

        return count % 2 == 1
        
        """
        :type n: int
        :rtype: bool
        """
        