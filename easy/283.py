class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)

        def next_index(index=0, is_zero=True):
            for i in range(index, length):
                if bool(nums[i]) ^ is_zero:
                    return i

            return None

        index_zero = next_index(0)
        index_no_zero = 0
        if index_zero is not None:
            index_no_zero = next_index(index_zero, is_zero=False)

        while index_zero is not None and index_no_zero is not None:
            nums[index_zero] = nums[index_no_zero]
            nums[index_no_zero] = 0

            index_zero = next_index(index_zero + 1)
            if index_zero is not None:
                index_no_zero = next_index(index_zero, is_zero=False)