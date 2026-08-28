from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for word in strs:
            anagram_groups[tuple(sorted(word))].append(word)
        
        return list(anagram_groups.values())