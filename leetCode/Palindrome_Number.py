#!coding:utf-8

"""
Determine whether an integer is a palindrome. Do this without extra space.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        string = str(x)
        if string == string[::-1]:
            return True
        else:
            return False
        
