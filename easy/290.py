class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        def recode_p(input_p):
            keys = []
            code = []
            for c in input_p:
                if len(keys) == 0:
                    keys.append(c)
                    code.append('a')
                else:
                    add_flag = True
                    for i in range(len(keys)):
                        if c == keys[i]:
                            code.append(code[i])
                            add_flag = False
                            break
                    if add_flag:
                        keys.append(c)
                        code.append(chr(ord(code[-1]) + 1))
            return ''.join(code)

        p = []
        keys = []
        for word in str.split():
            if len(keys) == 0:
                keys.append(word)
                p.append('a')
            else:
                add_flag = True
                for i in range(len(keys)):
                    if word == keys[i]:
                        p.append(p[i])
                        add_flag = False
                        break

                if add_flag:
                    keys.append(word)
                    p.append(chr(ord(p[-1]) + 1))

        return ''.join(p) == recode_p(pattern)
