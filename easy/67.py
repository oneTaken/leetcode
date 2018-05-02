class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        length = max(len(a), len(b))
        # p = '{:0{}}'
        a = '0' * (length - len(a)) + a
        b = '0' * (length - len(b)) + b
        tmp = '0'
        ans = []

        def char_plus(c1, c2):
            if c1 == '1' and c2 == '1':
                return '1', '0'
            elif (c1 == '1' and c2 == '0') or (c1 == '0' and c2 == '1'):
                return '0', '1'
            else:
                return '0', '0'

        for i in range(length - 1, -1, -1):
            _tmp1, _ans = char_plus(a[i], b[i])
            _tmp2, _ans = char_plus(_ans, tmp)
            _, tmp = char_plus(_tmp1, _tmp2)
            ans.append(_ans)
        if tmp == '1':
            ans.append('1')

        return ''.join(ans[::-1])
