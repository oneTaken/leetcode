# solution1
# exceed time 13/15
class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = 0

        def is_same_minus(x):
            d = x[1] - x[0]
            for i in range(2, len(x)):
                if x[i] - d != x[i - 1]:
                    return False
            return True

        for p in range(0, len(A) - 2):
            for q in range(p + 2, len(A)):
                count += is_same_minus(A[p:q + 1])

        return count


# solution2
class Solution2:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = 0

        def is_same_minus(x):
            d = x[1] - x[0]
            for i in range(2, len(x)):
                if x[i] - d != x[i - 1]:
                    return False
            return True

        for p in range(0, len(A) - 2):
            for q in range(p + 2, len(A)):
                if is_same_minus(A[p:q + 1]):
                    count += 1
                else:
                    break

        return count
