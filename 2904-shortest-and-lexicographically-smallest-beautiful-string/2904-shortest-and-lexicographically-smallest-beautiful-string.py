class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # Step 1: Collect indices of all '1's
        ones = [i for i, char in enumerate(s) if char == '1']
        
        # Step 2: If there are fewer than k '1's, no beautiful substring exists
        if len(ones) < k:
            return ""
        
        min_len = float('inf')
        best_str = ""
        
        # Step 3: Check all windows of exactly k '1's
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            
            # Extract the candidate substring
            candidate = s[start:end+1]
            candidate_len = end - start + 1
            
            # Update the shortest and lexicographically smallest string
            if candidate_len < min_len:
                min_len = candidate_len
                best_str = candidate
            elif candidate_len == min_len:
                # If lengths are tied, pick the lexicographically smaller one
                best_str = min(best_str, candidate)
                
        return best_str