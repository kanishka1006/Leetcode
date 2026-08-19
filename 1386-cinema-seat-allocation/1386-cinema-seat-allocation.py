import collections
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Map to store the bitmask of reserved seats for each row
        # Key: row_number, Value: bitmask
        row_masks = collections.defaultdict(int)
        
        for row, seat in reservedSeats:
            # Set the bit corresponding to the seat number
            row_masks[row] |= (1 << seat)
            
        # Assume all rows are completely empty initially (2 groups per row)
        total_groups = 2 * n
        
        # Bitmasks for the critical blocks
        # Left block (seats 2, 3, 4, 5): 111100 in binary -> 60 in decimal
        # Right block (seats 6, 7, 8, 9): 1111000000 in binary -> 960 in decimal
        # Middle block (seats 4, 5, 6, 7): 11110000 in binary -> 240 in decimal
        
        for row, mask in row_masks.items():
            # Since this row has reservations, subtract the 2 assumed groups
            total_groups -= 2
            
            # Check availability of blocks using bitwise AND
            left_free = (mask & 60) == 0
            right_free = (mask & 960) == 0
            middle_free = (mask & 240) == 0
            
            if left_free and right_free:
                total_groups += 2
            elif left_free or right_free or middle_free:
                total_groups += 1
                
        return total_groups