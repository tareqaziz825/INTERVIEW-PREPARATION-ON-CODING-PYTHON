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
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : 
            return False

        divisor = 1
        while x >= 10 * divisor:
            divisor *= 10

        while x > 0:
            lDigit = x // divisor
            rDigit = x % 10

            if  lDigit != rDigit: 
                return False

            # lChop = x % divisor #removes the left digit
            # rChop = lChop // 10 #removes the right digit
            # x = rChop
            x = (x % divisor) // 10

            divisor = divisor // 100
        return True
    
# // is called Floor Division (or Integer Division)
# 10 // 3 = 3