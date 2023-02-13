import collections
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        ans = []
        freqs_heap = []
        freqs = collections.Counter(nums)

        for f in freqs:
            heapq.heappush(freqs_heap,(-freqs[f],f))    #빈도수를 음수로 바꾸어 최소 힙에 push 하면 가장 큰 빈도수가 가장 작은 빈도수로 최소 힙의 root에 저장될 수 있음
        for i in range(k):
            ans.append(heapq.heappop(freqs_heap)[1])

        return ans


l = [1,1,1,2,2,3]
a = Solution()
print(a.topKFrequent(l,2))
# print(a)
