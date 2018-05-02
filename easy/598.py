# solution1
# exceed time 6/69
class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        M = [[0 for _ in range(n)] for _ in range(m)]
        for (a, b) in ops:
            for i in range(a):
                for j in range(b):
                    M[i][j] += 1

        max_number = max([max(M[i]) for i in range(m)])
        count = sum([M[i][j] == max_number for i in range(m) for j in range(n)])

        return count


# solution2
class Solution2:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if len(ops) == 0:
            return m * n
        min_a = 40001
        min_b = 40001
        for (a, b) in ops:
            min_a = min(min_a, a)
            min_b = min(min_b, b)

        return min_a * min_b
