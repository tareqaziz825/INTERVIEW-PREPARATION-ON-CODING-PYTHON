# https://leetcode.com/problems/palindrome-number/

# using String approach
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        strr = str(x)

        # revStr = ""
        # for char in strr:
        #     revStr = char + revStr

        # if strr == revStr:
        #     return True
        
        # string[start : stop : step]
        # [::-1] Reverses a String
        # if strr == strr[::-1]:
        #     return True
        return strr == strr[::-1]

# using Numerical approach
class Solution:
    def isPalindrome(self, x: int) -> bool:
