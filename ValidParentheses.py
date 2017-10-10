class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #思路：利用栈来排查
        #从头到尾遍历字符串，如果当前字符是左括号，则加入栈中
        #如果当前括号是右括号，判断右括号对应的左括号是否与栈弹出的字符相等
        #这里有个由右括号找左括号的操作，用dict[右括号] = 左括号
        #最终判断stack是否为空
        stack = []
        dict ={"]": "[", ")": "(", "}": "{"}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop(): #stack == []主要是防止pop空stack报错
                    return False
            else:
                return False
        return stack == []
