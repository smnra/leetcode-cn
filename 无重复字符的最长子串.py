#!usr/bin/env python  
#-*- coding:utf-8 _*-  

""" 
@author:SMnRa
@file: 无重复字符的最长子串.py 
@time: 2018/12/{DAY} 
描述:
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


"""


class Solution(object):
    def lengthOfLongestSubstring(self, tmpStr):
        """
        :type s: str
        :rtype: int
        """
        strLen = len(tmpStr)
        if strLen==0:
            maxLen = 0
        else:
            maxLen = 1

        for k in range(0,strLen-1):
            l = strLen - k
            ind = 0
            while ind+l <= strLen:
                tmp = tmpStr[ind:ind+l]
                if len(tmp) == len(list(set(tmp))):
                    maxLen = len(tmp)
                    return maxLen
                ind += 1
        return maxLen
if __name__=='__main__':
    so = Solution()
    max = so.lengthOfLongestSubstring("abcabcbb")  #  aaswes  5
    print(max)

