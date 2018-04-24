class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        length = len(ops)
        count = [-1 for _ in range(length)]
        keys = ['+', 'D', 'C']
        flag_number = 0

        def last_turn(index):
            for i in range(index - 1, -1, -1):
                if count[i] != flag_number:
                    return i

            return None

        for i, op in enumerate(ops):
            if op not in keys:
                count[i] = int(op)
            elif op == '+':
                index1 = last_turn(i)
                index2 = last_turn(index1)
                count[i] = count[index1] + count[index2]
            elif op == 'D':
                index = last_turn(i)
                count[i] = count[index] * 2
            else:
                index = last_turn(i)
                count[i] = flag_number
                count[index] = 0

        return sum(count)