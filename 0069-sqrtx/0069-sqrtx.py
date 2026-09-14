class Solution(object):
    def mySqrt(self, x):
        if x <= 1:
            return x
        l = 2
        r = x//2
        while l <= r:
            mid = (l + r)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                l = mid + 1
            else:
                r = mid - 1
        return r
        """
        :type x: int
        :rtype: int
        """
        