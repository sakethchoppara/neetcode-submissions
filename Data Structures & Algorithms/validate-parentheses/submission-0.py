class Solution:
    def isValid(self, s: str) -> bool:
        closed = set(['{', '[', '('])
        l = []
        for i in s:
            if i in closed:
                l.append(i)
            elif i == '}' and l and l[-1] == '{':
                l.pop()
            elif i == ']' and l and l[-1] == '[':
                l.pop()
            elif i == ')' and l and l[-1] == '(':
                l.pop()
            else:
                return False  # opening bracket with no match
        return len(l) == 0