class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #strStr(x, y)判断y是否是x的子串
        # if not needle:
        #     return 0
        # for i in range(0, len(haystack) - len(needle) + 1): #注意这是是+1
        #     if haystack[i: i + len(needle)] == needle:
        #         return i
        # return -1
        #思路二：str.find()函数
        return haystack.find(needle)
