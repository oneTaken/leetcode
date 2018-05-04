class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        status = [[None for _ in range(n)] for _ in range(m)]
        valid = lambda i, j: i >= 0 and i < m and j >= 0 and j < n

        def change(i, j):
            live_cell = [board[k][l] for k in [i - 1, i, i + 1] for l in [j - 1, j, j + 1] if
                         not (k == i and l == j) and valid(k, l)]
            num = sum(live_cell)

            return num in [2, 3] if board[i][j] == 1 else num == 3

        for i in range(m):
            for j in range(n):
                status[i][j] = int(change(i, j))

        for i in range(m):
            for j in range(n):
                board[i][j] = status[i][j]
