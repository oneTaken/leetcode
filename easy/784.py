class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        numbers = list(map(str, range(10)))
        c_length = len(S)
        indexs = [i for i in range(c_length) if S[i] not in numbers]
        length = len(indexs)
        max_number = 2 ** length
        choice = lambda i, c: c.upper() if i == '1' else c.lower()

        ans = []
        for i in range(max_number):
            _ans = []
            rep = '{:0>{}}'.format(bin(i)[2:], length)
            for j, c_index in enumerate(indexs):
                choice_c = choice(rep[j], S[c_index])
                _ans.append(choice_c)

            choice_str = []
            for i in range(c_length):
                if i in indexs:
                    i_index = indexs.index(i)
                    choice_str.append(_ans[i_index])
                else:
                    choice_str.append(S[i])

            ans.append(''.join(choice_str))

        return ans
