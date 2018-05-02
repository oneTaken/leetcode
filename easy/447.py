# solution1
# exceed time 24/31
class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        length = len(points)
        count = 0
        dis = lambda i, j: (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
        for i in range(length):
            for j in range(length):
                for k in range(length):
                    if i != j and i != k and j != k:
                        if dis(i, j) == dis(i, k):
                            count += 1

        return count


# solution2
# exceed time 24/31
class Solution2:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        length = len(points)
        count = 0
        dis = lambda i, j: (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
        for i in range(length):
            j_range = [j for j in range(length) if j != i]
            for j in j_range:
                distant = dis(i, j)
                k_range = [k for k in j_range if k != j]
                valid_point = [dis(i, k) == distant for k in k_range]
                count += sum(valid_point)

        return count


# solution3
# exceed time 24/31
class Solution3:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        length = len(points)
        count = 0
        dis = lambda i, j: (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
        dis_xy = lambda k, x, y: (points[k][0] - x) ** 2 + (points[k][1] - y) ** 2
        for i in range(length):
            j_range = [j for j in range(length) if j != i]
            for j in j_range:
                distant = dis(i, j)
                k_range = [k for k in j_range if k != j]
                x, y = points[i]
                valid_point = [dis_xy(k, x, y) == distant for k in k_range]
                count += sum(valid_point)

        return count
