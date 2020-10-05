class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        for interval in sorted(intervals, key=lambda x: x[0]):
            if not ans or interval[0] > ans[-1][-1]:
                ans.append(interval)
            else:
                ans[-1][-1] = max(ans[-1][-1], interval[-1])
        return ans

ss = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print('=== Given intervals : {}'.format(intervals))

res = ss.merge(intervals)

print('=== result is : {}'.format(res))
