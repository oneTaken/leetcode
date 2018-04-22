# solution 1
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        number = [S.count(J[i]) for i in range(len(J))]

        return sum(number)

# solution2
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        origin_length = len(S)
        for i in J:
            S = S.replace(i, '')

        return origin_length - len(S)

# solution3
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        num = dict().fromkeys(list(J), 0)
        for i in S:
            if num.get(i) is not None:
                num[i] += 1
        count = sum(list(num.values()))

        return count