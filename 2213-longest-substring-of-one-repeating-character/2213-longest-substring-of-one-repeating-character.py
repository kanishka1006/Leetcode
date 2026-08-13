from typing import List

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        
        # Flat arrays to represent properties of segment tree nodes
        sz = [0] * (4 * n)
        pref_c = [''] * (4 * n)
        suff_c = [''] * (4 * n)
        pref_l = [0] * (4 * n)
        suff_l = [0] * (4 * n)
        max_l = [0] * (4 * n)
        
        def push_up(node: int):
            left = 2 * node
            right = 2 * node + 1
            
            # Segment size
            sz[node] = sz[left] + sz[right]
            
            # Prefix/Suffix Characters
            pref_c[node] = pref_c[left]
            suff_c[node] = suff_c[right]
            
            # Prefix Length
            pref_l[node] = pref_l[left]
            if pref_l[left] == sz[left] and pref_c[left] == pref_c[right]:
                pref_l[node] += pref_l[right]
                
            # Suffix Length
            suff_l[node] = suff_l[right]
            if suff_l[right] == sz[right] and suff_c[left] == suff_c[right]:
                suff_l[node] += suff_l[left]
                
            # Maximum Length
            max_l[node] = max(max_l[left], max_l[right])
            if suff_c[left] == pref_c[right]:
                max_l[node] = max(max_l[node], suff_l[left] + pref_l[right])

        def build(node: int, l: int, r: int):
            if l == r:
                sz[node] = 1
                pref_c[node] = s[l]
                suff_c[node] = s[l]
                pref_l[node] = 1
                suff_l[node] = 1
                max_l[node] = 1
                return
            
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            push_up(node)
            
        def update(node: int, l: int, r: int, idx: int, char: str):
            if l == r:
                pref_c[node] = char
                suff_c[node] = char
                return
            
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx, char)
            else:
                update(2 * node + 1, mid + 1, r, idx, char)
            push_up(node)
            
        # Build the initial segment tree based on string `s`
        build(1, 0, n - 1)
        
        ans = []
        for char, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, char)
            ans.append(max_l[1]) # The root node always holds the answer for the entire string
            
        return ans