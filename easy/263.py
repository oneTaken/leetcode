class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        flag = True if num > 0 else False
        while num > 1:
            if num / 2 == num // 2:
                num //= 2
            elif num / 3 == num // 3:
                num //= 3
            elif num / 5 == num // 5:
                num //= 5
            else:
                flag = False
                break

        return flag