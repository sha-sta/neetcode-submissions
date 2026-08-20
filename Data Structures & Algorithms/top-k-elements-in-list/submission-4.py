class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        if len(nums) == 0:
            return []
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = 1
            else:
                map[nums[i]] += 1
        sorted_vals = sorted(map, key=map.get)
        ret = []
        for i in range(k):
            ret.append(sorted_vals[-1 - i])
        return ret