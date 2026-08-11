class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        counts = {}
        countt = {}
        for i in s:
            counts[i] = counts.get(i, 0) + 1
        for i in t:
            countt[i] = countt.get(i, 0) + 1
        
        if counts != countt:
            return False
        
        for key, value in counts.items():
            if value != countt[key]:
                return False
        
        return True