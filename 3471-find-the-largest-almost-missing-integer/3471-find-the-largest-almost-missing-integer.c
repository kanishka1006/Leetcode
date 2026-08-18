#include <stdio.h>

int largestInteger(int* nums, int numsSize, int k) {
    int ans = -1;
    
    // Based on the constraints, the numbers are only between 0 and 50.
    // We can just check every possible number in that range.
    for (int x = 0; x <= 50; x++) {
        int count = 0;
        
        // Iterate over all starting positions of subarrays of size k
        for (int i = 0; i <= numsSize - k; i++) {
            int found = 0;
            
            // Check if 'x' is present in the current subarray
            for (int j = i; j < i + k; j++) {
                if (nums[j] == x) {
                    found = 1;
                    break;
                }
            }
            
            if (found) {
                count++;
            }
        }
        
        // If the number appears in exactly one subarray, it is a candidate
        if (count == 1) {
            if (x > ans) {
                ans = x;
            }
        }
    }
    
    return ans;
}