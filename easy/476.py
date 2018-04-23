class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        flip = lambda x:'1' if x=='0' else '0'
        data = ''.join([flip(x) for x in bin(num)[2:]])
        return int(data, 2)