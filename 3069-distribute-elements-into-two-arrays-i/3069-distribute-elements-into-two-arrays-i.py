class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        
        # Iterate through the remaining elements in nums
        for i in range(2, len(nums)):
            # If the last element of arr1 is strictly greater than the last element of arr2
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
                
        # Concatenate and return the result
        return arr1 + arr2