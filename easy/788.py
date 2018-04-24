class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        keys = set(['0', '1', '2', '5', '6', '8', '9'])
        data = dict()
        data['0'] = '0'
        data['1'] = '1'
        data['2'] = '5'
        data['5'] = '2'
        data['6'] = '9'
        data['8'] = '8'
        data['9'] = '6'

        rotate = lambda x: data[x]
        for i in range(1, N + 1):
            if set(str(i)).issubset(keys):
                number = int(''.join(list(map(rotate, str(i)))))
                count += int(number != i)

        return count