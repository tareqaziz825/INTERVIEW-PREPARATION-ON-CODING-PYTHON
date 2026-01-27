# https://leetcode.com/problems/roman-to-integer/

# A Dictionary is Python's specific implementation of a Hash Map.

class Solution:
    def romanToInt(self, s: str) -> int:
        romanVal = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0

        for i in range(len(s)):
            if i+1 < len(s) and \
            romanVal[s[i]] < romanVal[s[i+1]]:
                total -= romanVal[s[i]]
            else:
                total += romanVal[s[i]]

        return total
    
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        # 1. Create your 'translation' dictionary
        roman_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        total = 0
        
        # 2. Loop through the string
        for i in range(len(s)):
            current_val = roman_values[s[i]]
            
            # Check if there is a 'next' character
            if i + 1 < len(s):
                next_val = roman_values[s[i+1]]
                
                # Compare current and next
                if current_val < next_val:
                    # Logic for subtraction (e.g., 'IV')
                    total -= current_val
                else:
                    # Logic for addition (e.g., 'VI' or 'II')
                    total += current_val
            else:
                # This is the last character, always add it
                total += current_val
                
        return total
"""