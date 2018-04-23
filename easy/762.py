class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        import math
        count = 0

        def isprime(n):
            if n < 2:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True

        for num in range(L, R + 1):
            number = bin(num).count('1')
            count += int(isprime(number))

        return count