class Solution(object):
    def diagonalSum(self, mat):
        
        sum_diag = 0
        n = len(mat)

        for i in range(n):

            sum_diag += mat[i][i]
            sum_diag += mat[i][n-i-1]

        if n % 2 == 1:
            sum_diag -= mat[n//2][n//2]
            
        return sum_diag

        """
        :type mat: List[List[int]]
        :rtype: int
        """
        