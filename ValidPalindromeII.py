class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #回文判断条件: s == s[::-1]
        #思路一：根据题意有两个情况：
        #1.去掉中间的一个元素s[i],使s[:i] + s[i + 1:]回文
        #2.不去掉任何一个元素,s直接回文
        #但是这个方法的时间限制超时
        # for i in range(len(s)):
        #     t = s[:i] + s[i + 1:]
        #     if t  == t[::-1]:
        #         return True
        # return s == s[::-1]
        #思路二：通过两个指针left和right遍历
        #如果发现有一处指针对应元素不相等
        #则需去掉left或者right，任何判断未遍历元素是否回文
        left = 0
        right =  len(s) - 1
        while left <right:
            if s[left]  == s[right]:
                left += 1
                right -= 1
            else:
                return s[left: right] == s[left: right][::-1] or s[left + 1: right + 1] ==  s[left + 1: right + 1][::-1]
        return True
