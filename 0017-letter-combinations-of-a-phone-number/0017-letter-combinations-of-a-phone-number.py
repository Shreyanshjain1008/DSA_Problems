class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        mp = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        ans = []

        def backtrack(index, curr):
            if index == len(digits):
                ans.append(curr)
                return

            for ch in mp[digits[index]]:
                backtrack(index + 1, curr + ch)

        backtrack(0, "")

        return ans
        """
        :type digits: str
        :rtype: List[str]
        """
        