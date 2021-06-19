class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        start = 0
        nxt = 1
        l = []
        while (start < len(s)):
            nxt = start + 1
            if nxt == len(s):
                l.append(d[s[start]])
                break
            elif s[start] == 'I' and s[nxt] == 'V':
                l.append(4)
                start = start + 2
            elif s[start] == 'I' and s[nxt] == 'X':
                l.append(9)
                start = start + 2
            elif s[start] == 'X' and s[nxt] == 'L':
                l.append(40)
                start = start + 2
            elif s[start] == 'X' and s[nxt] == 'C':
                l.append(90)
                start = start + 2
            elif s[start] == 'C' and s[nxt] == 'D':
                l.append(400)
                start = start + 2
            elif s[start] == 'C' and s[nxt] == 'M':
                l.append(900)
                start = start + 2
            else:
                l.append(d[s[start]])
                start = start + 1
        return sum(l)




