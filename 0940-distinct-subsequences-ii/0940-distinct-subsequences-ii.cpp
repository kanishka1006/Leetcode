
class Solution {
public:
    int distinctSubseqII(std::string s) {
        int MOD = 1e9 + 7;
        std::vector<int> ends(26, 0);
        int total = 0;
        
        for (char c : s) {
            int idx = c - 'a';
            
            // Number of subsequences that will now end with `c`
            int new_ends = (total + 1) % MOD;
            
            // In C++, modulo of negative numbers can be negative, 
            // so we add MOD before taking the final modulo.
            total = ((total - ends[idx]) % MOD + MOD) % MOD;
            total = (total + new_ends) % MOD;
            
            ends[idx] = new_ends;
        }
        
        return total;
    }
};