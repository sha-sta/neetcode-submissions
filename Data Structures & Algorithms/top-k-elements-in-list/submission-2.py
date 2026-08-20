class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        if len(nums) == 0:
            return []
        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i], 0) + 1
        sorted_vals = sorted(map, key=map.get)
        ret = []
        for i in range(k):
            ret.append(sorted_vals[-1 - i])
        return ret