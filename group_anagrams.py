import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = collections.defaultdict(list)
        for string in strs:
            sorted_str = ''.join(sorted(string))
            res[sorted_str].append(string)
        return res.values()

ss = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print('=== Given strs  : {}'.format(strs))

res = ss.groupAnagrams(strs)

print('=== result is : {}'.format(res))
