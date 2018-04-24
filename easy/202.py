class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = dict()
        square = lambda x: int(x) * int(x)
        sum_str = lambda x: sum(list(map(square, x)))
        flag = True

        while n != 1:
            print(n, nums.get(n))
            if nums.get(n) is None:
                nums[n] = 1
            else:
                flag = False
                break
            n = sum_str(str(n))

        return flag