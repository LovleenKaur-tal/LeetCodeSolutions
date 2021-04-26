class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 1
        sum = 0
        if not nums:
            return 0
        for i in range(0, len(nums) - 1):

            if nums[i] < nums[i + 1]:
                count = count + 1
                print("Alpha", nums[i], nums[i + 1], count)
                if sum <= count:
                    sum = count
            else:
                count = 1
        if not sum and count:
            return count
        if not sum:
            return 1
        return int(sum)

