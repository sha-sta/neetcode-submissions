class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            temp_hours = 0
            k = int((left + right) / 2)
            for pile in piles:
                temp_hours += -(pile // -k)
            if (temp_hours <= h):
                right = k
            elif (temp_hours > h):
                left = k + 1
        return left