class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = list([1 for _ in range(n)])
        for i in range(2, n):
            if num[i] == 1:
                for j in range(i + i, n, i):
                    num[j] = 0

        return max(sum(num) - 2, 0)
