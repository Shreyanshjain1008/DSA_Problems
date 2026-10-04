class Solution(object):
    def groupAnagrams(self, words):

        groups = {}

        for word in words:
            key = ''.join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
        
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        