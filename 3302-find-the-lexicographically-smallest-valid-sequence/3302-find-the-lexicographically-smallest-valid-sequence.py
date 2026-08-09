class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        from typing import List
        """


        m, n = len(word1), len(word2)
        
        # R[j] holds the max index in word1 where word2[j:] can be exactly matched
        R = [-1] * (n + 1)
        R[n] = m 
        
        # 1. Right-to-Left Suffix Mapping (The Oracle)
        ptr = m - 1
        for j in range(n - 1, -1, -1):
            while ptr >= 0 and word1[ptr] != word2[j]:
                ptr -= 1
            if ptr >= 0:
                R[j] = ptr
                ptr -= 1
            else:
                break # Remaining suffixes cannot be matched
                
        ans = []
        used_skip = False
        j = 0
        
        # 2. Left-to-Right Greedy Selection
        for i in range(m):
            if j == n:
                break
                
            if word1[i] == word2[j]:
                # Exact match: greedily take it
                ans.append(i)
                j += 1
            elif not used_skip and i + 1 <= R[j + 1]:
                # Mismatch: use the skip ONLY IF the remainder can fit in the future
                used_skip = True
                ans.append(i)
                j += 1
                
        return ans if j == n else []
        