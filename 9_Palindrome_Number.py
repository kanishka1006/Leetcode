class Solution(object):
    def isPalindrome(self, x):
       
        """
        :type x: int
        :rtype: bool
        """
  
        original = x
        rev = 0
        while x >0:
            digit = x % 10
            rev  = rev *10 +digit
            x = x //10
        if original == rev:
            return True
        return False