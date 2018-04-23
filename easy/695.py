class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if sum([sum(x) for x in grid]) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])
        max_area = 0

        visit = []
        for i in range(m):
            visit.append([0 for i in range(n)])

        def get_neighbor(i, j):
            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            points = []
            for neighbor in neighbors:
                x, y = neighbor
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                if grid[x][y] == 1 and visit[x][y] == 0:
                    points.append((x, y))
                    visit[x][y] = 1

            return points

        def get_area(i, j):
            points = [(i, j)]
            visit[i][j] = 1
            area = 0
            while len(points):
                x, y = points.pop()
                area += 1
                points.extend(get_neighbor(x, y))

            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visit[i][j] == 0:
                    area = get_area(i, j)
                    max_area = max(area, max_area)

        return max_area