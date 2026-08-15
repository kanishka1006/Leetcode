class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_xor = 0
        all_zeros = True
        
        for num in nums:
            total_xor ^= num
            if num != 0:
                all_zeros = False
                
        # If all elements are 0, no non-zero XOR subsequence is possible
        if all_zeros:
            return 0
            
        # If total XOR is non-zero, the whole array is the answer
        if total_xor != 0:
            return len(nums)
            
        # If total XOR is 0 but there are non-zero elements, remove exactly one non-zero element
        return len(nums) - 1
        