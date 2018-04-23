# solution1
# exceed time 400/460
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True
        for i in range(len(s)):
            new_s = s[:i] + s[i+1:]
            if new_s == new_s[::-1]:
                return True
        return False


# solution2
# exceed time 402/460
class Solution2:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True

        keys = list(set(s))
        data = dict().fromkeys(keys, 0)
        for c in s:
            data[c] += 1
        false_flag = [data[key] % 2 for key in keys]
        if sum(false_flag) > 2:
            return False

        for i in range(len(s)):
            new_s = s[:i] + s[i + 1:]
            if new_s == new_s[::-1]:
                return True
        return False