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
        if x < 0 : 
            return False

        divVal = 1
        while x >= 10 * divVal:
            divVal *= 10

        while x > 0:
            lDigit = x // divVal
            rDigit = x % 10

            if  lDigit != rDigit: 
                return False

            # lChop = x % divVal
            # rChop = lChop // 10
            # x = rChop
            x = (x % divVal) // 10

            divVal = divVal // 100
        return True
    
# // is called Floor Division (or Integer Division)
# 10 // 3 = 3