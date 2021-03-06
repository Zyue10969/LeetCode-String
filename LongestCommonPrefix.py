import os
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #思路一：os.path.commonprefix(list)
        #return os.path.commonprefix(strs)
        #思路二：reduce()函数
        if not strs:
            return ""
        else:
            return reduce(self.lcp, strs)
    def lcp(self, str1, str2):
        i = 0
        while i < len(str1) and i < len(str2):
            if str1[i] == str2[i]:
                i += 1
            else:
                break
        return str1[:i]
