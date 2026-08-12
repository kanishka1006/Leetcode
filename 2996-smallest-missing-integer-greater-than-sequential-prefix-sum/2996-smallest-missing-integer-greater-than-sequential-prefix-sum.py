class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum = nums[0]
        
        for i in range(1, len(nums)):
            # Check if the sequence continues
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                # The moment the sequence breaks, stop
                break
                
        # 2. Convert to a set for O(1) lookups
        num_set = set(nums)
        
        # 3. Find the smallest missing integer >= prefix_sum
        while prefix_sum in num_set:
            prefix_sum += 1
            
        return prefix_sum
        