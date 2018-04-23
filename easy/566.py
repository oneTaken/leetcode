class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(nums)
        n = len(nums[0])
        if r * c != m * n:
            return nums

        return [[nums[(i + j * c) // n][(i + j * c) % n] for i in range(c)] for j in range(r)]
