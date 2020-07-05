"""
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 首先暴力法
        # 暴力法有点难啊－－
        # 采用动态规划
        # 1，重复子问题->假设res[i][j]为word1中到i的子串到word2中到j的子串的编辑距离，这里假设已经求出了上一个状态的编辑距离（最短编辑距离）
        # 2，状态定义-》采用升维构造DP数组，将两个字符串分别作为横列和竖列，但是需要考虑其中一个为空的情况，所有上面和左面均增加一行
        # 3，DP方程-》if s1[i] == s2[j]:
        #               res[i][j] = res[i-1][j-1]
        #            else:
        #               res = min(res[i-1][j],res[i][j-1],res[i-1][j-1]) + 1
        if not word1 or not word2: return len(word1) if len(word1) > 0 else len(word2)
        res = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        # base case
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if i==0:
                    res[i][j] = j
                if j==0:
                    res[i][j] = i
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    res[i][j]=res[i-1][j-1]
                else:
                    res[i][j] = min(res[i-1][j],res[i][j-1],res[i-1][j-1]) + 1
        return res[-1][-1]