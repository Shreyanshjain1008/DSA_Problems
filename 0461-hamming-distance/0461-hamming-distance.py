class Solution(object):
    def hammingDistance(self, x, y):
        n = x ^ y
        count = 0

        while n:
            n = n & (n - 1)
            count += 1

        return count
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        