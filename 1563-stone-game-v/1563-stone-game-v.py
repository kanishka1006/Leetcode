class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        if n == 1:
            return 0
        
        # Build prefix sum array for O(1) range sum queries
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        dp = [[0] * n for _ in range(n)]
        max_l = [[0] * n for _ in range(n)]
        max_r = [[0] * n for _ in range(n)]
        
        # Base cases
        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]
            
        m_arr = list(range(n))
        
        # Compute bottom-up by increasing length of the subarray
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Monotonically advance the pivot m_arr[i]
                while m_arr[i] + 1 < j and (prefix[m_arr[i] + 2] - prefix[i]) * 2 <= prefix[j + 1] - prefix[i]:
                    m_arr[i] += 1
                
                m = m_arr[i]
                left_sum2 = (prefix[m + 1] - prefix[i]) * 2
                total_sum = prefix[j + 1] - prefix[i]
                
                if left_sum2 <= total_sum:
                    if left_sum2 == total_sum:
                        # left == right at the pivot, Alice chooses the maximum between both caches
                        ans = max(max_l[i][m], max_r[m + 1][j])
                    else:
                        # leftSum < rightSum up to pivot `m`
                        ans = max_l[i][m]
                        if m + 1 < j:
                            # Account for possibilities beyond pivot where rightSum < leftSum
                            ans = max(ans, max_r[m + 2][j])
                else:
                    # Very heavy left side, always default to right part choices
                    ans = max_r[i + 1][j]
                    
                dp[i][j] = ans
                
                # Update our choice caches
                max_l[i][j] = max(max_l[i][j - 1], total_sum + ans)
                max_r[i][j] = max(max_r[i + 1][j], total_sum + ans)
                
        return dp[0][n - 1]