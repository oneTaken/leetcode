class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        not_same = lambda x: x != [x[0]] * len(x)
        m = len(matrix)
        n = len(matrix[0])
        i = m - 1
        j = 0

        def next_ij(i, j):
            if i > 0:
                return i - 1, j
            elif i == 0 and j < n - 1:
                return i, j + 1
            else:
                return None, None

        def get_data(i, j):
            data = []
            while i < m and j < n:
                data.append(matrix[i][j])
                i += 1
                j += 1
            return data

        while i is not None:
            if not_same(get_data(i, j)):
                return False
            i, j = next_ij(i, j)
        return True