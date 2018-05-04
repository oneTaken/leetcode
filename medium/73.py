class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        visit = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0 and visit[i][j] == 0:
                    for l in range(n):
                        if matrix[i][l] != 0:
                            matrix[i][l] = 0
                            visit[i][l] = 1
                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = 0
                            visit[k][j] = 1


