class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        count = 0
        nums = [1]
        visit = dict()
        while len(nums) > 0:
            num = nums.pop(0)
            count += 1
            if visit.get(num * 2) is None:
                nums.append(num * 2)
                visit[num * 2] = 1
            if visit.get(num * 3) is None:
                nums.append(num * 3)
                visit[num * 3] = 1
            if visit.get(num * 5) is None:
                nums.append(num * 5)
                visit[num * 5] = 1

            nums = sorted(nums)
            if count + 3 > n:
                break

        return nums[n - count - 1]