#coding:utf-8

'''
一步一步自己调试出来的，真心不易。
Given a string, find the length of the longest substring without repeating characters.

Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #临时存储单个字符
        lis = []
        #最长的字符串的长度
        max = 0
        # 当输入的字符串长度小于2时
        if len(s) <= 1:
            return len(s)
        #遍历每个列表元素
        for i in s:
            if i not in lis:
                 lis.append(i)
            else:
                #将较大的字符串长度赋值给max
                if len(lis) > max:
                     max = len(lis)
                for j in range(0,lis.index(i)+1):
                    lis.pop(0)
                lis.append(i)
        if len(lis) > max:
            max = len(lis)    
        return max
