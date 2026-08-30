class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return n

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        i = min(min_idx, max_idx)
        j = max(min_idx, max_idx)

        delete_front = j+1
        delete_back = n - i
        delete_both = (i+1) + (n - j)

        return min(delete_front, delete_back, delete_both)