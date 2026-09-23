class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        total = sum(nums)
        target = total -x

        #If target is negative , we cannot keep any valid subarray.
        if target < 0:
            return -1


        #if target is 0, we have to remove everything
        if target == 0:
            return len(nums)

        left = 0
        currentSum = 0
        maxLength = -1

        for right in range(len(nums)):
            currentSum += nums[right]

            while currentSum  > target:
                currentSum -= nums[left]
                left += 1
            if currentSum == target:
                maxLength = max(
                    maxLength,
                    right - left +1
                )
        if maxLength == -1:
            return -1
        return len(nums) - maxLength