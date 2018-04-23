class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        m = len(image)
        n = len(image[0])
        color = image[sr][sc]

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
                if image[x][y] == color and visit[x][y] == 0:
                    points.append((x, y))
                    image[x][y] = newColor
                    visit[x][y] = 1

            return points

        points = [(sr, sc)]
        image[sr][sc] = newColor
        visit[sr][sc] = 1

        while len(points):
            x, y = points.pop()
            points.extend(get_neighbor(x, y))

        return image