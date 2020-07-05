"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def isValid(self, s: str) -> bool:
        # using stack O(n) time O(n) space
        if not s: return True
        dit = {"(":")"}
        stack = []
        for item in s:
            if item in dit:
                stack.append(item)
            else:
                if not stack or item != dit[stack[-1]]:
                    return False
                else:
                    stack.pop()
        return True if not stack else False

    def longestValidParentheses(self, s: str) -> int:
        # 依旧使用栈的思想，每个满足的子窜可以获得一个长度
        # 好像比较麻烦
        # 不如转化为寻找最长回文串，最长的回文串就是最长有效子串
        # 1， 使用中心扩展法，不过只能死两个字符作为中心，n-1个中心
        # 只有两种中西可以继续想外扩展-》1： (), 2: )(
        # 但是往外扩展的时候情况有些复杂，不能简单的通过判断新加的字符来判断
        #　新的字符串是否为满足条件的子串
        # 使用动态规划，res[i][j]表示是否为有效子串
        # 先使用暴力法，从最长的开始找起，找到的第一个满足的就是最长有效串
        # if len(s) < 2: return 0
        # max_length = 0
        # for length in range(len(s), 1, -1):
        #     for i in range(len(s)):
        #         if i + length > len(s):
        #             continue
        #         if self.isValid(s[i:i+length]):
        #             return length
        # return max_length
        # 暴力法超出时间限制
        # 使用动态规划算法
        if len(s) < 2: return 0
        dp = [0 for _ in range(len(s)+1)]
        # 加一个为了方便处理刚开始的异常情况
        for i in range(1,len(s)):
            if s[i] == ")":
                # 两种情况
                if s[i-1] == "(":
                    dp[i] = dp[i-2] + 2 + (dp[i-dp[i-2]-1] if i-dp[i-2]-1>=0 else 0)# 这里也可以加上前面满足的子串的长度，这样两种情况就比较清楚
                else:
                    if i-dp[i-1]-1 >= 0:
                        if s[i-dp[i-1]-1] == "(":
                            dp[i] = dp[i-1] + 2 + (dp[i-2-dp[i-1]] if i-2-dp[i-1]>=0 else 0)
                            # dp[i] = dp[i-1] + 2
        return max(dp)