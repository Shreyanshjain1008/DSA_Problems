class Solution(object):
    def nextGreaterElement(self, n):
        lst = list(map(int,str(n)))
        length = len(lst)
        i = length-2
        while i>=0:
            if lst[i]<lst[i+1]:
                break
            i-=1
        if i<0:
            return -1
        j=length-1
        while j>=0:
            if lst[j]>lst[i]:
                break
            j-=1
        lst[i],lst[j]=lst[j],lst[i]
        j=length-1
        i+=1
        while i<=j:
            lst[i],lst[j]=lst[j],lst[i]
            i+=1
            j-=1
        ans=int(''.join(map(str,lst)))
        if ans>2**31-1:
            return -1
        return ans

        """
        :type n: int
        :rtype: int
        """
        