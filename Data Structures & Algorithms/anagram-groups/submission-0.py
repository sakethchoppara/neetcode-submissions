from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups_dict = defaultdict(list)
        for w in strs:
            groups_dict[''.join(sorted(w))].append(w)
        
        result = [groups_dict[length] for length in sorted(groups_dict)]
        return result