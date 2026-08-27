class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        from collections import Counter

        if len(s1) > len(s2):
            return False
        ref = Counter(s1)
        window = Counter()

        for i, ch in enumerate(s2):
            window[ch] += 1
            if i >= len(s1):
                rem = s2[i-len(s1)]
                window[rem] -= 1
                if window[rem] == 0:
                    window.pop(rem)
            if ref == window:
                return True
            
        return False

            
