class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for w in strs:
            key = tuple(sorted(w))
            groups[key].append(w)
        return list(groups.values())