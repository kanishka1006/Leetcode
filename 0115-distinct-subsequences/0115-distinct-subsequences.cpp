class Solution {
public:
    int numDistinct(string s, string t) {
        int m = s.length();
        int n = t.length();
        vector<unsigned int> dp(n+1, 0);

        dp[0] = 1;

        for(int j = 1; j <=m; ++j){

            for(int i = n; i >= 1; --i){
                if (s[j - 1] == t[i - 1]){
                    dp[i] += dp[i - 1];
                }
            }
        }
        return dp[n];
    }
};