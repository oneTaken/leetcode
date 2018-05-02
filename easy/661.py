class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(M)
        n = len(M[0])

        def smooth_ij(i, j):
            data = []
            neighbors = [(x, y) for x in [i - 1, i, i + 1] for y in [j - 1, j, j + 1]]
            for (x, y) in neighbors:
                if x >= 0 and x < m and y >= 0 and y < n:
                    data.append(M[x][y])

            return sum(data) // len(data)

        smooth = []
        for i in range(m):
            _smooth = []
            for j in range(n):
                new_data = smooth_ij(i, j)
                _smooth.append(new_data)
            smooth.append(_smooth)

        return smooth
