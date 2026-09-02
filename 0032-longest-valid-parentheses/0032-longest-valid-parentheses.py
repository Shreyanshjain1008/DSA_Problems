class Solution(object):
    def longestValidParentheses(self, s):
        length = 0
        st = []
        st.append(-1)
        for i in range ( len(s) ):
            if s[i] == '(':
                st.append(i)
            else:
                st.pop()
                if len(st) == 0:
                    st.append(i)
                else:
                    length = max(length, i-st[-1])
        return length
        """
        :type s: str
        :rtype: int
        """
        