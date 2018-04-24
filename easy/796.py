class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:
            return True
        if len(A) != len(B):
            return False
        if len(A) == 1:
            return A == B

        move = lambda x: x[1:] + x[0]
        for i in range(len(A)):
            if move(A) == B:
                return True
            else:
                A = move(A)

        return False