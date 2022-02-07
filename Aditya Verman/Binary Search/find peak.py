class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        N = len(nums)

        while (l <= r):
            mid = (l + r) // 2
            prev = (mid - N - 1) % N
            nxt = (mid + 1) % N

            if nums[mid] >= nums[prev] and nums[mid] >= nums[nxt]:
                return mid
            elif mid == 0:
                if nums[0] > nums[1]:
                    return 0
                else:
                    return 1
            elif mid == N - 1:
                if nums[N - 1] > nums[N - 2]:
                    return N - 1
                else:
                    return N - 2
            elif nums[mid] < nums[prev]:
                r = (mid - 1)

            elif nums[mid] < nums[nxt]:
                l = (mid + 1)

        return -1


