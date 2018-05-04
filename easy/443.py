# solution1
# not in-place
class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        ans = []
        start = chars[0]
        length = 1

        for i in range(1, len(chars)):
            if chars[i] == start:
                length += 1
            else:
                if length == 1:
                    ans.append(start)
                else:
                    ans.extend(start + str(length))
                    start = chars[i]
                    length = 1

        if length == 1:
            ans.append(start)
        else:
            ans.extend(start + str(length))
            start = chars[i]
            length = 1

        return len(ans)