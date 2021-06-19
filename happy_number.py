class Solution:
    def isHappy(self, n: int) -> bool:

        l = []

        def func(n):
            if n == 1:
                return True
            if l.count(n) == 2:
                return False
            num = str(n)
            n = 0
            for x in num:
                n = n + int(x) * int(x)
            l.append(n)

            return func(n)

        return func(n)

