#include<vector>
#include<algorithm>
#include<climits>
class Solution {
public:
    int minimumSumSubarray(vector<int>& nums, int l, int r) {
        int n = nums.size();
        vector<int> prefix(n + 1, 0);
        for(int i = 0; i < n; ++i){
            prefix[i + 1] = prefix[i] + nums[i];

        }
        int min_positive_sum = INT_MAX;

        for(int length = l; length <= r; ++length){
            for(int i = 0; i <= n - length; ++i){
                int subarray_sum = prefix[i + length] - prefix[i];
                if (subarray_sum > 0){
                    min_positive_sum = min(min_positive_sum, subarray_sum);
                }
            }
        }
        return (min_positive_sum == INT_MAX)? -1 : min_positive_sum;
        
    }
};