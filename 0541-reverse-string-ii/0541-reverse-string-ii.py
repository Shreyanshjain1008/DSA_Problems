class Solution(object):
    def reverseStr(self, s, k):
        arr = list(s)

        for i in range(0, len(arr), 2*k):
            arr[i:i+k] = arr[i:i+k][::-1]

        return ''.join(arr)
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        