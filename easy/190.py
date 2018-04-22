class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        data = '{:>032}'.format(bin(n)[2:])

        return int(data[::-1], 2)