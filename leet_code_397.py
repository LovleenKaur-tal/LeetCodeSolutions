class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0

        def func(n, count):
            if n == 1:
                return count
            elif n % 2 == 0:
                count = func(int(n / 2), count + 1)
            else:
                count = min(func(n + 1, count + 1), func(n - 1, count + 1))

            return count

        count = func(n, count)
        return count
