class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        count = dict()
        for words in cpdomains:
            times, cpdomain = words.split(' ')
            times = int(times)
            keys = cpdomain.split('.')
            keys = ['.'.join(keys[i:]) for i in range(len(keys))]
            for key in keys:
                count[key] = times if count.get(key) is None else count[key] + times

        ans = ['{} {}'.format(count[key], key) for key in count.keys()]

        return ans