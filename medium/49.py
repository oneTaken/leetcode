# solution1
# exceed time 100/101
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # problem 242 solution
        def isAnagram(s, t):
            """
            :type s: str
            :type t: str
            :rtype: bool
            """
            if len(s) != len(t):
                return False

            data = dict().fromkeys(list(set(s)), 0)
            for c in s:
                data[c] += 1

            for c in t:
                if data.get(c) is None or data[c] <= 0:
                    return False
                else:
                    data[c] -= 1

            return True

        ans = []
        for s in strs:
            if len(ans) == 0:
                ans.append([s])
            else:
                add_flag = True
                for j in range(len(ans)):
                    if isAnagram(s, ans[j][0]):
                        ans[j].append(s)
                        add_flag = False
                        break
                if add_flag:
                    ans.append([s])

        return ans


# solution2
# exceed time 95/101
class Solution2:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from copy import deepcopy
        def isAnagram(data_dict, t):
            for c in t:
                if data_dict.get(c) is None or data_dict[c] <= 0:
                    return False
                else:
                    data_dict[c] -= 1

            return sum(list(data_dict.values())) == 0

        def get_data_dict(s):
            data = dict().fromkeys(list(set(s)), 0)
            for c in s:
                data[c] += 1

            return data

        ans = []
        data_list = []
        for s in strs:
            if len(ans) == 0:
                ans.append([s])
                data_list.append(get_data_dict(s))
            else:
                add_flag = True
                for j in range(len(ans)):
                    if isAnagram(deepcopy(data_list[j]), s):
                        ans[j].append(s)
                        add_flag = False
                        break

                if add_flag:
                    ans.append([s])
                    data_list.append(get_data_dict(s))

        return ans


# solution3
# exceed time 98/101
class Solution3:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from copy import deepcopy
        def isAnagram(data_dict, t):
            for c in t:
                if data_dict.get(c) is None or data_dict[c] <= 0:
                    return False
                else:
                    data_dict[c] -= 1

            return True

        def get_data_dict(s):
            data = dict().fromkeys(list(set(s)), 0)
            for c in s:
                data[c] += 1

            return data

        ans = []
        data_list = []
        for s in strs:
            if len(ans) == 0:
                ans.append([s])
                data_list.append(get_data_dict(s))
            else:
                add_flag = True
                for j in range(len(ans)):
                    if len(s) == len(ans[j][0]) and isAnagram(deepcopy(data_list[j]), s):
                        ans[j].append(s)
                        add_flag = False
                        break

                if add_flag:
                    ans.append([s])
                    data_list.append(get_data_dict(s))

        return ans
