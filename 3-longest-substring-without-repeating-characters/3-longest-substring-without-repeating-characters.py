class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_num, start = 0,0
        used = {}
        for i in range(len(s)):
            if s[i] in used and start <= used[s[i]]:
                start = used[s[i]] + 1
            else:
                max_num = max(max_num, i- start+1)
            used[s[i]] = i 
        return max_num