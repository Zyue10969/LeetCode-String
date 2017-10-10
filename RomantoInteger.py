class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #1. 相同的数字连写，所表示的数等于这些数字相加得到的数，如 III=3；
        # 2. 小的数字在大的数字的右边，所表示的数等于这些数字相加得到的数，如 VIII=8、XIII=12；
        # 3. 小的数字（限于 I、X 和 C）在大的数字的左边，所表示的数等于大数减小数得到的数，如 IV=4、IX=9；
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        num =  roman[s[-1]]
        for i in xrange(len(s) - 1, 0, -1):
            cur = s[i]
            per = s[i - 1]
            if per >= cur:
                num += per
            else:
                num -= per
        return num
