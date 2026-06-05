class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1 = {}
        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            if key in map1:
                map1[key].append(strs[i])
            else:
                map1[key] = [strs[i]]
        return list(map1.values())