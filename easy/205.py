# use part function of problem 290
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        def get_p(string):
            p = []
            keys = []
            for word in string:
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

            return ''.join(p)

        return get_p(s) == get_p(t)
