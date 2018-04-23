class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for x in range(left, right + 1):
            keys = list(set(str(x)))
            if '0' in keys:
                continue
            add_flag = True
            for key in keys:
                if x % int(key) != 0:
                    add_flag = False
                    break
            if add_flag:
                ans.append(x)

        return ans