class Solution(object):
    def missingNumber(self, A):
        N=len(A)
        # if N==1:
        #     return 0

        A.sort()

        if A[0]!=0:
            return 0
        if A[N-1]!=N:
            return N

        for i in range(1, N+1):
            if A[i]-A[i-1]>1:
                return i
        """
        :type nums: List[int]
        :rtype: int
        """
        