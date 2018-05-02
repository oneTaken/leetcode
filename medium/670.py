class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        number = [int(s) for s in str(num)]
        for i in range(len(number)):
            if number[i] == max(number[i:]):
                continue
            else:
                max_number = max(number[i + 1:])
                max_index = [x for x in range(len(number[i + 1:])) if number[i + 1:][x] == max_number]
                index = i + 1 + max(max_index)

                tmp = number[i]
                number[i] = number[index]
                number[index] = tmp
                return int(''.join([str(x) for x in number]))

        return num
