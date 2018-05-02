class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        tmp = 1

        def plus(x, tmp):
            ans = x + tmp
            tmp = ans // 10
            return tmp, ans % 10

        ans = []
        for i in range(len(digits) - 1, -1, -1):
            tmp, _ans = plus(digits[i], tmp)
            ans.append(_ans)

        if tmp == 1:
            ans.append(1)

        return ans[::-1]
