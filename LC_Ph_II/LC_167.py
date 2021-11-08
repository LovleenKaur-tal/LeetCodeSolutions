class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        l = 0
        r = len(numbers) - 1

        while (l < r and r < len(numbers)):
            num1 = numbers[l]

            num2 = numbers[r]

            s = num1 + num2

            if s == target:
                return [l + 1, r + 1]
            elif s > target:
                r = r - 1
            else:
                l = l + 1

