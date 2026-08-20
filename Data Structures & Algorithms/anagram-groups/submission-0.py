class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for i in range(len(strs)):
            sorted_str = "".join(sorted(strs[i]))
            if sorted_str not in map:
                map[sorted_str] = [strs[i]]
            else:
                map[sorted_str].append(strs[i])
        ret = []
        for value in map.values():
            ret.append(value)
        return ret