# solution1
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bx = '{:>031}'.format(bin(x)[2:])
        by = '{:>031}'.format(bin(y)[2:])

        return sum([bx[i] != by[i] for i in range(31)])