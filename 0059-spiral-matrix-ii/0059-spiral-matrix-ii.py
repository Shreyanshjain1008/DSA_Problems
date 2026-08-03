class Solution(object):
    def generateMatrix(self, n):
        a=[[0]*n for _ in range(n)]
        top_row,first_col=0,0
        bottom_row,last_col=n-1,n-1
        cnt=1
        while cnt<=n*n:
            j=first_col
            while j<=last_col:
                a[top_row][j]=cnt
                cnt+=1
                j+=1
            top_row+=1
            i=top_row
            while i<=bottom_row:
                a[i][last_col]=cnt
                cnt+=1
                i+=1
            last_col-=1
            j=last_col
            while j>=first_col:
                a[bottom_row][j]=cnt
                cnt+=1
                j-=1
            bottom_row-=1
            i=bottom_row
            while i>=top_row:
                a[i][first_col]=cnt
                cnt+=1
                i-=1
            first_col+=1
        return a
        """
        :type n: int
        :rtype: List[List[int]]
        """
        