# solution1
# exceed time
class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        count = 0
        for i in range(1, num):
            if num % i == 0:
                count += i
                if count > num:
                    return False

        return num == count

# solution2
# exceed time
class Solution2:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        count = 0
        for i in range(1, num // 2 + 1):
            if num % i == 0:
                count += i
                if count > num:
                    return False

        return num == count

# solution3
# exceed time
class Solution3:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        count = 1
        end = num // 2 + 1
        start = 2
        while end > start:
            if num % start == 0:
                count += start + num // start
                if count > num:
                    return False
                end = num // start

            start += 1

        return num == count