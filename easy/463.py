class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        def check(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return True
            return not grid[x][y]

        def water_neighbor(i, j):
            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            status = [check(n[0], n[1]) for n in neighbors]

            return sum(status)

        count = [water_neighbor(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]

        return sum(count)