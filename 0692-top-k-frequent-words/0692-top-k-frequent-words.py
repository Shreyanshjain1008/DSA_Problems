class Solution(object):
    def topKFrequent(self, words, k):

        D = {}
        for w in words:
            D[w] = D.get(w, 0)+1

        arr = list(D.items())

        arr.sort(key=lambda x: (-x[1],x[0]))

        ans=[]
        for i in range(k):
            ans.append(arr[i][0])
        return ans

        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        