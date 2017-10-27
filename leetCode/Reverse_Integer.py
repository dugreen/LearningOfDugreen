#!coding:utf-8


"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        temp = 0

        if x < 0:
            x = -x
            flag = -1
        while x > 0:
            temp = temp*10 + x%10
            x = x//10

        if temp > 0x7FFFFFFF:
            return 0
        return flag*temp
