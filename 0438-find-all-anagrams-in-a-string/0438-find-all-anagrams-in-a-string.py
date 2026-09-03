class Solution(object):
    def findAnagrams(self, s, p):

        pmap = {}
        wmap = {}

        for i in range (len(p)):
            pmap[p[i]] = pmap.get(p[i],0)+1

        ans = []
        i=0
        j=0
        while j<len(s):
            wmap[s[j]] = wmap.get(s[j],0)+1
            if j-i+1 == len(p):
                if pmap == wmap:
                    ans.append(i)
                wmap[s[i]]-=1
                if wmap[s[i]] == 0:
                    del wmap[s[i]]
                i+=1
            j+=1
        return ans

        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        