# solution1
# exceed time 10/45
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        def get_number(n):
            if n == 0 or n == 1:
                return 1
            else:
                return get_number(n - 1) + get_number(n - 2)

        return get_number(n)