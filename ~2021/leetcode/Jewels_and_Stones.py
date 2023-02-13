# from collections import defaultdict
import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        #freqs = {}
        freqs = collections.defaultdict(int)

        for char in stones:
            freqs[char] += 1
            # if char not in freqs:
            #    freqs[char] = 1
            # else :
            #    freqs[char] += 1

        cnt = 0

        for char in jewels:
            #if char in freqs:
            cnt += freqs[char]

        return cnt


tmp = Solution()
res = tmp.numJewelsInStones("aA", "aAABBBB")
print(res)