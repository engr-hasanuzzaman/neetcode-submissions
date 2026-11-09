from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = defaultdict(list)
        for s in strs:
            anagram_group["".join(sorted(s))].append(s)
        return list(anagram_group.values())
        