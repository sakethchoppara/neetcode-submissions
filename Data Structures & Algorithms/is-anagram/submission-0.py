class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        countt = {}
        for i in s:
            counts[i] = counts.get(i, 0) + 1
        for i in t:
            countt[i] = countt.get(i, 0) + 1
        
        if counts != countt:
            return False
        print(type(counts))
        for key, value in counts.items():
            if value != countt[key]:
                return False
        
        return True