class Solution(object):
    def spiralOrder(self, a):
        element = []
        m = len(a)
        n = len(a[0])
        top_row, first_col = 0, 0
        bottom_row, last_col = m - 1, n - 1

        while top_row <= bottom_row and first_col <= last_col:

            j = first_col
            while j <= last_col:
                element.append(a[top_row][j])
                j += 1
            top_row += 1

            i = top_row
            while i <= bottom_row:
                element.append(a[i][last_col])
                i += 1
            last_col -= 1

            if top_row <= bottom_row:
                j = last_col
                while j >= first_col:
                    element.append(a[bottom_row][j])
                    j -= 1
                bottom_row -= 1

            if first_col <= last_col:
                i = bottom_row
                while i >= top_row:
                    element.append(a[i][first_col])
                    i -= 1
                first_col += 1

        return element
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        