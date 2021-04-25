class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for st in s:
            print("St is", st)
            t = t.replace(st, "", 1)

        return t

    