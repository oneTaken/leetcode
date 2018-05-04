# solution1
# exceed time 400/502
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count_2 = 0
        count_5 = 0

        def get_num(x, k):
            count = 0
            while x / k == x // k:
                count += 1
                x //= k

            return count

        for i in range(1, n + 1):
            count_2 += get_num(i, 2)
            count_5 += get_num(i, 5)

        return min(count_2, count_5)


# solution2
# exceed time 420/502
class Solution2:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count_2 = 0
        count_5 = 0

        def get_num(x, k):
            count = 0
            while x / k == x // k:
                count += 1
                x //= k

            return count

        for i in range(1, n + 1):
            if i % 2 == 0 or i % 5 == 0:
                count_2 += get_num(i, 2)
                count_5 += get_num(i, 5)

        return min(count_2, count_5)


# solution3
# exceed time 500/502
class Solution3:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        def get_num(x, k):
            count = 0
            while x / k == x // k:
                count += 1
                x //= k

            return count

        count_2 = [get_num(i, 2) for i in range(2, n + 1, 2)]
        count_5 = [get_num(i, 5) for i in range(5, n + 1, 5)]

        return min(sum(count_2), sum(count_5))


# solution4
# exceed time 500/502
class Solution4:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        def num_k(num, k):
            count = 0
            while num / k == num // k:
                count += 1
                num //= k

            return count

        def get_num(k):
            mod = 0
            count = 0
            for i in range(k, n + 1, k):
                mod += 1
                count += num_k(i, k) if mod % k == 0 else 1

            return count

        count_2 = get_num(2)
        count_5 = get_num(5)

        return min(count_2, count_5)


# solution5
# exceed time 500/502
class Solution5:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 5:
            return 0

        def get_num(x, k):
            count = 0
            while x / k == x // k:
                count += 1
                x //= k

            return count

        count_5 = [get_num(i, 5) for i in range(5, n + 1, 5)]

        return sum(count_5)


# solution6
class Solution6:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 5:
            return 0

        count = 0
        for i in range(1, n):
            start = 5 ** i
            if start > n:
                break
            count += (n - start) // start + 1

        return count
