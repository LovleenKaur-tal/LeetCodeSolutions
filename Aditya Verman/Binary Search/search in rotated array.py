class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        n = len(nums)
        r = n - 1

        def get_min_idx(nums):

            l = 0
            n = len(nums)
            r = n - 1

            if nums[0] < nums[r]:
                return 0
            while (l <= r):

                mid = (l + r) // 2
                prev = (mid + n - 1) % n
                nxt = (mid + 1) % n
                if nums[mid] <= nums[prev] and nums[mid] <= nums[nxt]:
                    return mid
                elif nums[0] <= nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

        idx = get_min_idx(nums)

        def bs(ar):

            l = 0

            r = len(ar) - 1

            while (l <= r):

                mid = (l + r) // 2

                if ar[mid] == target:
                    return mid
                elif target > ar[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        print(idx)

        if nums[idx] == target:
            return idx
        if idx >= 0 and idx < len(nums):
            x = bs(nums[0:idx])

            if x == -1:
                y = bs(nums[idx + 1:])
                if y == -1:
                    return y
                return y + (idx + 1)
            return x
        elif idx == 0 and target == nums[idx]:
            return 0
        return -1









