"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) < 2: return len(s)
        # 可以使用暴力法，分别判断一个字符到二个字符到整个字符是否为回文
        # 需要两个循环 n的平方
        total_num = 0
        for length in range(1, len(s)+1):
            for i in range(len(s)):
                if i + length > len(s):
                    continue
                temp = s[i:i+length]
                if temp == temp[::-1]:
                    total_num += 1
        return total_num
        # 暴力法时间复杂度很高
        # 使用动态规划
        # 三个基本问题->1,从最小的字符扩展到较长的字符串，类似于中心扩展定义，
        # 2，使用新的状态定义数组, res[i][j]标示ij之间的子窜是否为回文串
        # 3，DF方程，分三种情况，一个字符；两个字符的；大于两个字符的
        # res = [[False]*len(s) for _ in range(len(s))]
        # length = len(s)
        # for i in range(length):
        #     for j in range(length):
        #         if i == j:
        #             res[i][j] = True
        # for j in range(length):
        #     for i in range(0,j):
        #         # 遍历右上角
        #         if j - i == 1:
        #             if s[i] == s[j]:
        #                 res[i][j] = True
        #         else:
        #             # 长度大于2
        #             if s[i] == s[j]:
        #                 res[i][j] = res[i+1][j-1]
        # return sum((1 for i in range(length) for j in range(length) if res[i][j]))
        # 用动态规划和用暴力法时间基本一样
        # 也可以使用中心扩展方法，从每个可能的回文串的中心店进行扩展，其实有点类似于暴力法，但是
        # 解决了频繁判断选出的子串是否为回文的麻烦