class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in map:
                map[s[i]] = 1
            else:
                map[s[i]] += 1
            
        for i in range(len(t)):
            if t[i] not in map:
                return False
            else:
                map[t[i]] -= 1
        
        return not any(map.values())