class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}    #방문한 문자의 index 저장
        max_length = start = 0

        for i in range(len(s)):
            if s[i] in visited and start <= visited[s[i]]:  #지금 방문한 문자가 중복이고 start가 visited에 저장된 index보다 작을 때(start가 전에 저장된 문자 index를 참조하지 않도록)
                start = visited[s[i]] + 1   #start 뒤로 한칸
                # visited[s[i]] = i

            max_length = max(max_length, i - start + 1) #max_length는 중복없는 부분문자열 길이와 기존 max_length의 최댓값

            visited[s[i]] = i   #문자를 방문할 때마다 visited에 저장된 value 수정
        return max_length

tmp = Solution()
res = tmp.lengthOfLongestSubstring("abcabcbb")
print(res)





