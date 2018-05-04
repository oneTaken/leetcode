class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        import math
        root = math.sqrt(num)
        return root == int(root)