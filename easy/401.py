class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        import itertools
        def get_num(i, count=4):
            number = ['1'] * i + ['0'] * (count - i)
            data = list(itertools.permutations(number, count))
            data = list(set(data))
            data = [''.join(x) for x in data]

            return [int(x, 2) for x in data]

        time = []
        func1 = lambda x: x < 12
        func2 = lambda x: x < 60
        for i in range(num + 1):
            hours = get_num(i, 4)
            hours = list(filter(func1, hours))
            seconds = get_num(num - i, 6)
            seconds = list(filter(func2, seconds))
            time.extend(['{}:{:02}'.format(h, s) for h in hours for s in seconds])

        return time