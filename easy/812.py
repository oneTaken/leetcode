# 直角坐标系中
# A(x0,y0), B(x1,y1), C(x2,y2)
# S= abs(((x1-x0)*(y2-y0)-(x2-x0)*(y1-y0))/2)
class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        get_area = lambda x0, y0, x1, y1, x2, y2: abs(((x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)) / 2)

        length = len(points)
        max_area = 0
        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                for k in range(j + 1, length):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    area = get_area(x1, y1, x2, y2, x3, y3)
                    max_area = max(area, max_area)

        return max_area
