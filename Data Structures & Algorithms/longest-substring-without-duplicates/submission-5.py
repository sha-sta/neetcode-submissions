class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        longest = 0
        left = 0
        map = {}

        for i in range(len(s)):
            if s[i] in map:
                left = max(left, map[s[i]] + 1)
            map[s[i]] = i
            if i - left + 1 > longest:
                longest = i - left + 1
        return longest