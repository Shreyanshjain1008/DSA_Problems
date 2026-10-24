class Solution(object):
    def addStrings(self, num1, num2):
        carry = 0
        i = len(num1)-1
        j = len(num2)-1
        result = []

        while i>=0 or j>=0 or carry:

            a = int(num1[i]) if i >= 0 else 0
            b = int(num2[j]) if j >= 0 else 0

            sum_no = a + b + carry
            result.append(str(sum_no % 10))
            carry = sum_no // 10

            i -= 1
            j -= 1
        return ''.join(result[::-1])


        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        