from collections import Counter
class Solution(object):
    def smallestPalindrome(self, s):
        freq = Counter(s)

        first = []
        middle = ""

        for ch in sorted(freq):
            first.append(ch * (freq[ch] // 2))

            if freq[ch] % 2:
                middle = ch

        first = "".join(first)

        return first + middle + first[::-1]


        """
        :type s: str
        :rtype: str
        """
        