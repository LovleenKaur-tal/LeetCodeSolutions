class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        lt = [ord(i) - ord('a') for i in letters]
        t = ord(target) - ord('a')
        n = len(lt)
        l = 0
        r = len(lt) - 1
        res = 0

        while (l <= r):
            mid = (l + r) // 2

            if lt[mid] == t:
                while (mid < len(lt) and lt[mid] == t):
                    mid = mid + 1

                return chr(lt[(mid) % n] + ord('a'))

            elif lt[mid] < t:
                l = mid + 1
            else:
                res = lt[mid]
                r = mid - 1
        return chr(res + ord('a')) if res else letters[0]





