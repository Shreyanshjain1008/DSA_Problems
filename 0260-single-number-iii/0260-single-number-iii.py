class Solution(object):
    def singleNumber(self, arr):
        n=len(arr)
        xor=0
        a,b=0,0
        for i in range( n ):
            xor^=arr[i]
        pos=0
        while True:
            if (xor>>pos)&1 == 1:
                break
            pos+=1
        for i in range( n ):
            if (arr[i]>>pos)&1 == 0:
                a = a^arr[i]
            else:
                b = b^arr[i]
        # res=[a,b]
        # res.sort()
        return sorted([a,b])
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        