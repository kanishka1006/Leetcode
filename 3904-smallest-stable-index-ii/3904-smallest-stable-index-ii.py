class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        suffMin = [0] * n
        suffMin[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffMin[i] = min(nums[i], suffMin[i+1])
        preMax = nums[0]

        for i in range(n):
            preMax = max(preMax, nums[i])
            if preMax - suffMin[i] <= k:
                return i

        return -1
        